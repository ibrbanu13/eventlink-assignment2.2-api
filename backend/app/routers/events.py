from datetime import datetime, timezone

from fastapi import APIRouter, Depends

from app import data
from app.auth import get_current_user, is_admin
from app.schemas import parse_dt, success_response

router = APIRouter(prefix="/api/v1/events", tags=["events"])

def with_status(event):
    is_upcoming = parse_dt(event["startsAt"]) > datetime.now(timezone.utc)
    return {**event, "isUpcoming": is_upcoming}


@router.get("")
def list_events(user=Depends(get_current_user)):
    events = data.list_events() if is_admin(user) else data.list_events(owner_id=user["id"])
    items = [with_status(e) for e in events]
    return success_response(items, "Events retrieved successfully.")