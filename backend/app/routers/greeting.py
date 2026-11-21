from html import escape

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/api/v1", tags=["greeting"])

PROJECT_NAME = "EventLink"
PROJECT_DESCRIPTION = (
    "EventLink helps university students discover campus and club events, "
    "and lets organizers publish and manage them."
)

TEAM = [
    {
        "name": "Banu Ibrahimli",
        "student_id": "24086",
        "summary": "Events CRUD endpoints, mock data and pagination.",
    },
    {
        "name": "Zahra Ahmadova",
        "student_id": "23945",
        "summary": "Token authentication, role checks, error handling and validation.",
    },
    {
        "name": "Fatima Hasanzada",
        "student_id": "23242",
        "summary": "Greeting page, API documentation, Postman collection and README.",
    },
]


def render_page():
    team_items = "".join(
        f"<li><strong>{escape(m['name'])}</strong> ({escape(m['student_id'])})"
        f"<br>{escape(m['summary'])}</li>"
        for m in TEAM
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{PROJECT_NAME}</title>
</head>
<body>
  <h1>Welcome to {PROJECT_NAME}</h1>
  <p>{PROJECT_DESCRIPTION}</p>
  <h2>Team</h2>
  <ul>{team_items}</ul>
</body>
</html>"""

@router.get("/greeting", response_class=HTMLResponse)
def greeting():
    return HTMLResponse(content=render_page())