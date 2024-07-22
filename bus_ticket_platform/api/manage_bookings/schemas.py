from typing import Optional
from pydantic import BaseModel


class BookingSchema(BaseModel):
    booking_id: int
    user_id: int
    route_id: int
    status: str  # e.g., "confirmed", "cancelled"
    date_time: str  # ISO 8601 date and time string


class CancelModifySchema(BaseModel):
    booking_id: int
    action: str  # e.g., "cancel", "modify"
    new_date_time: Optional[str] = None  # ISO 8601 date and time string
