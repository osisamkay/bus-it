from ..task import send_booking_confirmation
from ninja import Router
from typing import List
from .schemas import BookingSchema, CancelModifySchema
from ninja import router
from ninja_jwt.authentication import JWTAuth


router = Router()


@router.post("/create_booking", response=BookingSchema, tags=["Create Bookings"])
def create_booking(request, booking: BookingSchema):
    user_email = booking.email  # Replace with actual user email field in BookingSchema
    booking_details = booking.json()  # Replace with actual booking details
    send_booking_confirmation.delay(user_email, booking_details)
    return booking


@router.get("/view_bookings", response=List[BookingSchema], tags=["Manage Bookings"])
def view_bookings(request):
    # Implementation goes here
    return [{"booking_id": 1, "user_id": 1, "route_id": 2, "status": "confirmed", "date_time": "2024-07-14T10:00:00Z"}]


@router.post("/cancel_modify", response=BookingSchema, tags=["Manage Bookings"])
def cancel_modify(request, cancel_modify: CancelModifySchema):
    # Implementation goes here
    return {"booking_id": cancel_modify.booking_id, "user_id": 1, "route_id": 2, "status": cancel_modify.action, "date_time": cancel_modify.new_date_time or "2024-07-14T10:00:00Z"}
