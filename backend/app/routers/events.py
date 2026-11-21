from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, Query

from app import data
from app.auth import can_access_event, get_current_user, is_admin
from app.schemas import EventCreate, EventUpdate, parse_dt, success_response

router = APIRouter(prefix="/api/v1/events", tags=["events"])

def with_status(event):
    is_upcoming = parse_dt(event["startsAt"]) > datetime.now(timezone.utc)
    return {**event, "isUpcoming": is_upcoming}


@router.get("")
def list_events(
    page: int = Query(1, ge=1),
    perPage: int = Query(10, ge=1, le=100),
    user=Depends(get_current_user),
):
    events = data.list_events() if is_admin(user) else data.list_events(owner_id=user["id"])
    total = len(events)
    start = (page - 1) * perPage
    items = [with_status(e) for e in events[start:start + perPage]]
    return success_response(
        items,
        "Events retrieved successfully.",
        meta={"total": total, "page": page, "perPage": perPage},
    )

@router.get("/{event_id}")
def get_event(event_id: str, user=Depends(get_current_user)):
    event = data.get_event(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found.")
    can_access_event(user, event)
    return success_response(with_status(event), "Event retrieved successfully.")

@router.delete("/{event_id}")
def delete_event(event_id: str, user=Depends(get_current_user)):
    event = data.get_event(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found.")
    can_access_event(user, event)
    data.delete_event(event_id)
    return success_response(None, "Event deleted successfully.")

@router.post("", status_code=201)
def create_event(body: EventCreate, user=Depends(get_current_user)):
    if data.find_duplicate(user["id"], body.title, body.startsAt, body.endsAt, body.location):
        raise HTTPException(
            status_code=409,
            detail="You already have an event with the same title, start/end time and location.",
        )
    event = data.create_event(body.model_dump(), user["id"])
    return success_response(with_status(event), "Event created successfully.")

@router.put("/{event_id}")
def update_event(event_id: str, body: EventUpdate, user=Depends(get_current_user)):
    event = data.get_event(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found.")
    can_access_event(user, event)
    updated = data.update_event(event_id, body.model_dump())
    return success_response(with_status(updated), "Event updated successfully.")