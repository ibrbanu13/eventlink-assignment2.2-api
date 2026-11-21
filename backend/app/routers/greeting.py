from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/api/v1", tags=["greeting"])

PROJECT_NAME = "EventLink"
PROJECT_DESCRIPTION = (
    "EventLink helps university students discover campus and club events, "
    "and lets organizers publish and manage them."
)


def render_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{PROJECT_NAME}</title>
</head>
<body>
  <h1>Welcome to {PROJECT_NAME}</h1>
  <p>{PROJECT_DESCRIPTION}</p>
</body>
</html>"""

@router.get("/greeting", response_class=HTMLResponse)
def greeting():
    return HTMLResponse(content=render_page())