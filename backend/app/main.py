from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from app.errors import http_exception_handler, validation_exception_handler

from app.errors import register_error_handlers
from app.routers import events

app = FastAPI(title="EventLink API", version="v1")

register_error_handlers(app)

app.include_router(events.router)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Routers will be registered here in later commits
