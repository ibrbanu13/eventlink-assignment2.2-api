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


CSS = """
:root {
  --bg: #f5f7fb; --card: #ffffff; --text: #1f2933; --muted: #5f6b7a;
  --accent: #2563eb; --border: #e3e8ef;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f172a; --card: #1e293b; --text: #e5e7eb; --muted: #9aa5b5;
    --accent: #60a5fa; --border: #334155;
  }
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--text); line-height: 1.6;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
main { max-width: 860px; margin: 0 auto; padding: 24px 16px 48px; }
h1 { margin: 0 0 8px; font-size: 2rem; }
h2 { margin: 0 0 12px; font-size: 1.25rem; }
.lead { color: var(--muted); margin: 0 0 16px; }
.card {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 12px; padding: 20px; margin-bottom: 16px;
}
.status { margin: 0; font-weight: 600; }
.dot {
  display: inline-block; width: 10px; height: 10px; margin-right: 8px;
  border-radius: 50%; background: #16a34a;
}
ul { list-style: none; margin: 0; padding: 0; }
li { padding: 10px 0; border-bottom: 1px solid var(--border); }
li:last-child { border-bottom: none; }
.method {
  display: inline-block; min-width: 68px; margin-right: 8px; padding: 2px 8px;
  border-radius: 6px; color: #fff; font-size: 0.8rem; font-weight: 700; text-align: center;
}
.get { background: #16a34a; } .post { background: #2563eb; }
.put { background: #d97706; } .delete { background: #dc2626; }
code { font-family: ui-monospace, Consolas, monospace; word-break: break-all; }
@media (max-width: 600px) {
  h1 { font-size: 1.6rem; }
  .card { padding: 16px; }
}
"""


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
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{PROJECT_NAME}</title>
  <style>{CSS}</style>
</head>
<body>
  <main>
    <header class="card">
      <h1>Welcome to {PROJECT_NAME}</h1>
      <p class="lead">{PROJECT_DESCRIPTION}</p>
      <p class="status"><span class="dot"></span>API is running &bull; Version {API_VERSION}</p>
    </header>
    <section class="card">
      <h2>Team</h2>
      <ul>{team_items}</ul>
    </section>
    <section class="card">
      <h2>Endpoints</h2>
      <ul>{endpoint_rows}</ul>
    </section>
  </main>
</body>
</html>"""


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