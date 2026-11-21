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

### Mock tokens

Send the token in the `Authorization` header: `Authorization: Bearer <token>`

| Role | Token |
|---|---|
| ADA SITE| `user-a-token` |
| ADA MUN Club | `user-b-token` |
| Student Services | `admin-token` |


### Notes

- Data is stored in memory and **resets every time the server restarts**.
- Full endpoint documentation: [documentation/API.md](documentation/API.md).
- Example requests: `documentation/postman/eventlink.postman_collection.json`.