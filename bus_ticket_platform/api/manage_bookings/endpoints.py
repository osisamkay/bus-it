from datetime import datetime
from uuid import UUID
from ..task import send_booking_confirmation
from ninja import Router
from ninja.errors import HttpError
from typing import List, Optional
from .schemas import BookingSchema, ErrorResponse
from ninja import router
from django.db import transaction
from .models import Booking
from ..auth.endpoints import AuthBearer


router = Router()


@router.post("/create_booking", response={200: BookingSchema, 400: ErrorResponse}, tags=["Bookings"], auth=AuthBearer())
def create_booking(request, payload: BookingSchema):
    # Get the authenticated user's email from the request
    user_email = request.auth.email
    booking_details = payload.dict()  # Get booking details as a dictionary

    try:
        with transaction.atomic():
            booking = Booking.objects.create(
                user=request.auth, **payload.dict())
            # send_booking_confirmation.delay(user_email, booking_details)  # Uncomment to enable email sending
        return BookingSchema.from_orm(booking)
    except Exception as e:
        raise HttpError(400, str(e))


@router.get("/view_bookings", response=List[BookingSchema], tags=["Bookings"], auth=AuthBearer())
def view_bookings(request):
    try:
        bookings = Booking.objects.filter(user=request.auth)
        return [BookingSchema.from_orm(booking) for booking in bookings]
    except Exception as e:
        raise HttpError(400, str(e))


@router.put("/cancel_modify", response={200: BookingSchema, 400: ErrorResponse}, tags=["Bookings"], auth=AuthBearer())
def cancel_modify(request, booking_id: UUID, action: str, new_date_time: Optional[datetime] = None):
    """
    Cancel or modify a booking.
    """
    try:
        booking = Booking.objects.get(id=booking_id, user=request.auth)
        if action == "cancel":
            booking.status = "canceled"
        elif action == "modify" and new_date_time:
            booking.departure_datetime = new_date_time
            booking.status = "modified"
        else:
            raise HttpError(
                400, "Invalid action or missing new_date_time for modification")
        booking.save()
        return BookingSchema.from_orm(booking)
    except Booking.DoesNotExist:
        raise HttpError(400, "Booking not found")
    except Exception as e:
        raise HttpError(400, str(e))


@router.post("/book_ticket", response={200: BookingSchema, 400: ErrorResponse}, tags=["Bookings"], auth=AuthBearer())
def book_ticket(request, payload: BookingSchema):
    """
    Book a ticket for a bus route.
    """
    if payload.trip_type == "round_trip" and not payload.return_datetime:
        raise HttpError(400, "Return datetime is required for round trips")

    try:
        with transaction.atomic():
            booking = Booking.objects.create(
                user=request.auth, **payload.dict())
        return BookingSchema.from_orm(booking)
    except Exception as e:
        raise HttpError(400, str(e))
