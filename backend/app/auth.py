from fastapi import Header, HTTPException
from app.data import get_user_by_token

def get_current_user(authorization: str | None = Header(default=None)):
    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Authorization token is missing"
        )
    parts = authorization.split()

    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization header"
        )
    token = parts[1]
    user = get_user_by_token(token)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token"
        )

    return user
def can_access_event(user, event):
    return user["role"] == "admin" or event["ownerId"] == user["id"]
