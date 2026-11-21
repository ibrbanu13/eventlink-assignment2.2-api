# EventLink
 
EventLink helps university students discover campus and club events, and lets organizers publish and manage them. This repository holds the Assignment 2 prototype: a REST API with mocked data, token authentication and role-based access.
 
- **Demo video:** [TODO: add the YouTube link, 5 minutes at most]
- **API documentation:** [documentation/API.md](documentation/API.md)
- **Postman collection:** [documentation/postman/eventlink.postman_collection.json](documentation/postman/eventlink.postman_collection.json)

## Installation and running the backend

### Requirements

- Python 3.12 or 3.13
- Git

### Setup

1. Clone the repository and go into the backend folder:

   ```bash
   git clone https://github.com/ibrbanu13/eventlink-assignment2.2-api.git
   cd eventlink-assignment2.2-api/backend
   ```

2. Create and activate a virtual environment:

   ```powershell
   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   ```bash
   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

### Run

From the `backend/` folder:

```bash
python -m uvicorn app.main:app --reload
```

The API runs at `http://127.0.0.1:8000`

| URL | What it is |
|---|---|
| `http://127.0.0.1:8000/api/v1/greeting` | HTML welcome page |
| `http://127.0.0.1:8000/docs` | Interactive Swagger UI |
| `http://127.0.0.1:8000/api/v1/events` | Events API (needs a token) |

### Mock tokens

Send the token in the `Authorization` header: `Authorization: Bearer <token>`

| Role | Token |
|---|---|
| ADA SITE| `user-a-token` |
| ADA MUN Club | `user-b-token` |
| Student Services | `admin-token` |


### Notes

- Data is stored in memory and **resets every time the server restarts**.
- Full endpoint documentation, error codes and examples: [documentation/API.md](documentation/API.md).
- To try the requests, import the Postman collection and run the folders in order.