import pytest
from pydantic import ValidationError
from app.schemas import EventCreate, EventUpdate

def valid_event():
    return {
        "title": "AI Workshop",
        "category": "Workshop",
        "location": "B-204",
        "startsAt": "2026-11-25T14:00:00+04:00",
        "endsAt": "2026-11-25T16:00:00+04:00"
    }

def test_valid_event():
    event = EventCreate(**valid_event())
    assert event.title == "AI Workshop"
    assert event.description == []

def test_short_title():
    data = valid_event()
    data["title"] = "AB"

    with pytest.raises(ValidationError):
        EventCreate(**data)

def test_invalid_end_time():
    data = valid_event()
    data["endsAt"] = "2026-11-25T12:00:00+04:00"

    with pytest.raises(ValidationError):
        EventCreate(**data)

def test_missing_location():
    data = valid_event()
    del data["location"]

    with pytest.raises(ValidationError):
        EventCreate(**data)

def test_negative_capacity():
    data = valid_event()
    data["capacity"] = -5

    with pytest.raises(ValidationError):
        EventCreate(**data)

def test_partial_update():
    update = EventUpdate(title="Updated Workshop")

    assert update.title == "Updated Workshop"
    assert "location" not in update.model_dump(exclude_unset=True)
