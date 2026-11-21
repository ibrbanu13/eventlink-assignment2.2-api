import pytest
from fastapi import HTTPException
from app.auth import get_current_user, is_admin, can_access_event

def test_valid_user_token():
    user = get_current_user("Bearer user-a-token")
    assert user["id"] == "user-a"

def test_admin_token():
    user = get_current_user("Bearer admin-token")
    assert is_admin(user) is True

def test_missing_token():
    with pytest.raises(HTTPException) as error:
        get_current_user(None)

    assert error.value.status_code == 401

def test_invalid_token():
    with pytest.raises(HTTPException) as error:
        get_current_user("Bearer wrong-token")

    assert error.value.status_code == 401

def test_owner_can_access_event():
    user = {"id": "user-a", "role": "organizer"}
    event = {"ownerId": "user-a"}

    assert can_access_event(user, event) is True

def test_other_user_cannot_access_event():
    user = {"id": "user-b", "role": "organizer"}
    event = {"ownerId": "user-a"}

    with pytest.raises(HTTPException) as error:
        can_access_event(user, event)

    assert error.value.status_code == 403

def test_admin_can_access_event():
    user = {"id": "admin", "role": "admin"}
    event = {"ownerId": "user-a"}

    assert can_access_event(user, event) is True
