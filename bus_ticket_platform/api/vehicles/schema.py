# schemas.py
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from uuid import UUID


class VehicleSchema(BaseModel):
    id: UUID
    name: str
    capacity: int
    plate_number: str
    company: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True


class ErrorResponse(BaseModel):
    detail: str
