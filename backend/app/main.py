from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.errors import http_exception_handler, validation_exception_handler
from app.routers import events, greeting

app = FastAPI(title="EventLink API", version="v1")

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(events.router)
app.include_router(greeting.router)
