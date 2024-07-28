from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from uuid import UUID


class BookingSchema(BaseModel):
    contact_info: str = Field(..., max_length=255)
    trip_type: str = Field(..., max_length=255)
    route_id: UUID
    departure_datetime: datetime
    return_datetime: Optional[datetime]
    seat_number: int
    number_of_seats: int
    payment_method: str
    payment_details: str
    special_requests: Optional[str]
    discount_code: Optional[str]
    status: Optional[str] = "confirmed"
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    @validator('contact_info')
    def validate_contact_info(cls, value):
        if not value.isdigit() or not (9 <= len(value) <= 15):
            raise ValueError('Invalid contact info format')
        return value

    @validator('trip_type')
    def validate_trip_type(cls, value):
        if value not in ['one_way_trip', 'round_trip']:
            raise ValueError('Invalid trip type')
        return value

    @validator('return_datetime', always=True)
    def validate_return_datetime(cls, value, values):
        if values.get('trip_type') == 'round_trip' and not value:
            raise ValueError('Return datetime is required for round trips')
        return value

    class Config:
        orm_mode = True
        from_attributes = True


class ErrorResponse(BaseModel):
    """Schema for representing an error response."""
    detail: str
