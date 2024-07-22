from pydantic import BaseModel
from typing import List, Optional


class SeatSchema(BaseModel):
    seat_number: str
    available: bool


class PaymentSchema(BaseModel):
    payment_method: str
    amount: float


class TicketSchema(BaseModel):
    user_id: int
    route_id: int
    seats: List[SeatSchema]
    payment: PaymentSchema
    date_time: str  # ISO 8601 date and time string
