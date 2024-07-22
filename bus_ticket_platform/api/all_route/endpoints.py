from ninja import Router
from ninja.errors import HttpError
from .models import Route
from .schemas import CreateRouteSchema, OneWayTripsSchema, RoundTripsSchema, SearchResponse
from ..auth.endpoints import AuthBearer

router = Router()


@router.post("/create_route", tags=["Routes"], response=CreateRouteSchema, auth=AuthBearer())
def create_route(request, response: CreateRouteSchema):
    user = request.auth  # Ensure `request.auth` provides the user object

    try:
        # Create a new route instance and save it to the database
        route = Route.objects.create(
            name=response.name,
            description=response.description,
            start_point=response.start_point,
            end_point=response.end_point,
            distance=response.distance,
            user=user  # Associate the route with the authenticated user
        )
        return route  # Return the created route object
    except Exception as e:
        raise HttpError(400, str(e))


@router.get("/one_way_trips", response=OneWayTripsSchema, tags=["Search Routes"])
def one_way_trips(request):
    # Replace with actual implementation
    return {"routes": [{"origin": "City A", "destination": "City B", "duration": 120, "price": 20.0}]}


@router.get("/round_trips", response=RoundTripsSchema, tags=["Search Routes"])
def round_trips(request):
    # Replace with actual implementation
    return {"routes": [{"origin": "City A", "destination": "City B", "duration": 120, "price": 35.0}]}


@router.get("/popular_routes", tags=["Search Routes"])
def popular_routes(request):
    return {"message": "List of popular routes"}


@router.get("/search", response=SearchResponse, tags=["Search Routes"])
def search_routes(request, query: str):
    # Replace with actual search implementation
    return {"message": "Search results for query: " + query}
