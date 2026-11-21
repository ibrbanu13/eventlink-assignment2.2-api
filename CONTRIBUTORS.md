# Contributors

| Name | Student ID | GitHub | Branch |
|---|---|---|---|
| Banu Ibrahimli | 24086 | [@ibrbanu13] | `feature/events-api` |
| Zahra Ahmadova | 23945 | [@ZahraAhmadova] | `feature/auth` |
| Fatima Hasanzada | 23242 | [@fhasanzade2007-cpu] | `feature/docs-greeting` |

## Responsibilities

### Banu Ibrahimli: events API and mock data

- Project skeleton: backend folder structure, `requirements.txt`, FastAPI app entry point (`main.py`)
- Mock users and events (`data.py`), kept in memory
- Success response helper (`schemas.py`)
- Events CRUD endpoints in `routers/events.py`: list with pagination, get one, create, update, delete
- Ownership rules in the routes (404 for missing events, 403 for another user's event, 409 for duplicates)

### Zahra Ahmadova: authentication, errors and validation

- Token authentication and role checks (`auth.py`): 401 for missing or invalid tokens, admin and owner access
- Error handling (`errors.py`): the error envelope and handlers for 400, 401, 403, 404, 405 and 409
- Request validation models in `schemas.py`: field types and lengths, unknown fields, dates and registration deadline

### Fatima Hasanzada: greeting page, documentation and demo

- HTML greeting endpoint (`routers/greeting.py`): project, team, endpoint list, status and version, styled for desktop and mobile
- API documentation (`documentation/API.md`)
- Postman collection (`documentation/postman/`)
- `README.md`: installation guide, `git shortlog` output and work summary
- Demo video

## Shared work

- `main.py` is edited by all three members, each registering their own part (events router, error handlers, greeting router).
- The final integration check and the demo run-through were done together.

## Git workflow

- Small, focused commits with imperative messages, for example `Add 403 check for event update`
- One feature branch per area, merged into `main` through a pull request
- Merge commits (no squashing), so the individual commits stay visible
- `.gitignore` keeps virtual environments, caches and secrets out of the repository