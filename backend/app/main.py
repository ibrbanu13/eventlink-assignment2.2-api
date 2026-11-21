from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.errors import http_exception_handler, validation_exception_handler
from app.routers import events

app = FastAPI(title="EventLink API", version="v1")

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(events.router)
