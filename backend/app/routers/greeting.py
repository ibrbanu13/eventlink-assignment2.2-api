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

ENDPOINTS = [
    ("GET", "/api/v1/greeting", "This page."),
    ("GET", "/api/v1/events", "List events (admins see all, organizers see their own)."),
    ("GET", "/api/v1/events/{id}", "Get one event."),
    ("POST", "/api/v1/events", "Create an event."),
    ("PUT", "/api/v1/events/{id}", "Update an event."),
    ("DELETE", "/api/v1/events/{id}", "Delete an event."),
]

API_VERSION = "v1"

def render_page():
    team_items = "".join(
        f"<li><strong>{escape(m['name'])}</strong> ({escape(m['student_id'])})"
        f"<br>{escape(m['summary'])}</li>"
        for m in TEAM
    )
    endpoint_rows = "".join(
        f'<li><span class="method {method.lower()}">{method}</span> '
        f"<code>{escape(path)}</code> {escape(description)}</li>"
        for method, path, description in ENDPOINTS
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
  <h2>Endpoints</h2>
  <ul>{endpoint_rows}</ul>
  <p>Status: API is running &bull; Version {API_VERSION}</p>
</body>
</html>"""

@router.get("/greeting", response_class=HTMLResponse)
def greeting():
    return HTMLResponse(content=render_page())