from ninja import Router
from .schemas import TicketSchema

router = Router()


@router.post("/select_seats", response=TicketSchema, tags=["Book Tickets"])
def select_seats(request, ticket: TicketSchema):
    # Implementation goes here
    return ticket


@router.post("/choose_date_time", tags=["Book Tickets"])
def choose_date_time(request):
    return {"message": "Date and time chosen"}


@router.post("/payment", tags=["Book Tickets"])
def payment(request):
    return {"message": "Payment processed"}
