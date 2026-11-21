from fastapi import FastAPI

from app.errors import register_error_handlers
from app.routers import events

app = FastAPI(title="EventLink API", version="v1")

register_error_handlers(app)

app.include_router(events.router)