from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict, model_validator

def parse_dt(value):
    if isinstance(value, datetime):
        return value
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

class EventCreate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str = Field(min_length=3, max_length=200)
    description: list[str] = Field(default_factory=list)
    category: str = Field(min_length=1)
    location: str = Field(min_length=2, max_length=100)
    startsAt: datetime
    endsAt: datetime
    capacity: int | None = Field(default=None, gt=0)
    registrationDeadline: datetime | None = None

    @model_validator(mode="after")
    def check_dates(self):
        if self.endsAt <= self.startsAt:
            raise ValueError("endsAt must be later than startsAt")
        return self

class EventUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str | None = Field(default=None, min_length=3, max_length=200)
    description: list[str] | None = None
    category: str | None = Field(default=None, min_length=1)
    location: str | None = Field(default=None, min_length=2, max_length=100)
    startsAt: datetime | None = None
    endsAt: datetime | None = None
    capacity: int | None = Field(default=None, gt=0)
    registrationDeadline: datetime | None = None

    @model_validator(mode="after")
    def check_dates(self):
        if self.startsAt is not None and self.endsAt is not None:
            if self.endsAt <= self.startsAt:
                raise ValueError("endsAt must be later than startsAt")
        return self

def success_response(data, message, meta=None):
    body = {"success": True, "message": message, "data": data}
    if meta is not None:
        body["meta"] = meta
    return body