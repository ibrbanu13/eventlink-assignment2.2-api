from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.testclient import TestClient
from app.errors import http_exception_handler, validation_exception_handler

def create_test_app():
    app = FastAPI()

    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)

    @app.get("/test-unauthorized")
    def unauthorized():
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token"
        )

    @app.get("/test-validation")
    def validation(page: int):
        return {"page": page}

    return app

def test_unauthorized_error():
    client = TestClient(create_test_app())
    response = client.get("/test-unauthorized")

    assert response.status_code == 401
    assert response.json() == {
        "success": False,
        "error": {
            "code": "UNAUTHORIZED",
            "message": "Invalid authentication token"
        }
    }

def test_validation_error():
    client = TestClient(create_test_app())
    response = client.get("/test-validation?page=abc")

    assert response.status_code == 400
    assert response.json()["error"]["code"] == "VALIDATION_ERROR"
