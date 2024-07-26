from ninja import Router
from ninja.errors import HttpError
from django.forms.models import model_to_dict
from .models import Route
from .schemas import CreateRouteSchema, PaginatedRoutesSchema, OneWayTripsSchema, RoundTripsSchema, SearchResponse, ErrorResponse, RouteSchema
from ..auth.endpoints import AuthBearer
from django.db.models import F
from typing import List
from uuid import UUID

router = Router()


@router.post("/create_route", tags=["Routes"], response={200: CreateRouteSchema, 400: ErrorResponse}, auth=AuthBearer())
def create_route(request, payload: CreateRouteSchema):
    """
    Create a new route.

    This endpoint creates a new route and associates it with the authenticated user.
    """
    user = request.auth  # Get the authenticated user from the request

    try:
        # Create a new route instance and save it to the database
        route = Route.objects.create(
            name=payload.name,
            description=payload.description,
            start_point=payload.start_point,
            end_point=payload.end_point,
            distance=payload.distance,
            trip_type=payload.trip_type,
            user=user
        )
        return route  # Return the created route object
    except Exception as e:
        raise HttpError(400, detail=str(e))


@router.get("/one_way_trips", response={200: PaginatedRoutesSchema, 400: ErrorResponse}, tags=["Search Routes"])
def one_way_trips(request, page: int = 1, size: int = 10):
    """
    Get a paginated list of one-way trips.

    This endpoint returns a paginated list of one-way trips where the trip_type is 'one_way_trip'.
    """
    try:
        routes_query = Route.objects.filter(trip_type='one_way_trip')
        total = routes_query.count()
        routes = routes_query[(page - 1) * size: page * size]
        paginated_routes = PaginatedRoutesSchema(
            total=total,
            page=page,
            size=size,
            routes=[RouteSchema.from_orm(route) for route in routes]
        )
        return paginated_routes.dict()
    except Exception as e:
        raise HttpError(400, str(e))


@router.put("/route/{route_id}", response={200: RouteSchema, 404: ErrorResponse}, tags=["Routes"], auth=AuthBearer())
def update_route(request, route_id: UUID, payload: CreateRouteSchema):
    """
    Update a route by its ID.

    This endpoint allows updating a specific route identified by its UUID.
    """
    try:
        route = Route.objects.get(id=route_id)
        for attr, value in payload.dict().items():
            setattr(route, attr, value)
        route.save()
        return RouteSchema.from_orm(route)
    except Route.DoesNotExist:
        return 404, {"detail": "Route not found"}
    except Exception as e:
        raise HttpError(400, str(e))


@router.delete("/route/{route_id}", response={204: None, 404: ErrorResponse}, tags=["Routes"], auth=AuthBearer())
def delete_route(request, route_id: UUID):
    """
    Delete a route by its ID.

    This endpoint allows deleting a specific route identified by its UUID.
    """
    try:
        route = Route.objects.get(id=route_id)
        route.delete()
        return 204, None
    except Route.DoesNotExist:
        return 404, {"detail": "Route not found"}
    except Exception as e:
        raise HttpError(400, str(e))


@router.get("/round_trips", response={200: PaginatedRoutesSchema, 400: ErrorResponse}, tags=["Search Routes"])
def round_trips(request, page: int = 1, size: int = 10):
    """
    Get a paginated list of round trips.

    This endpoint returns a paginated list of round trips 
    """
    try:
        routes_query = Route.objects.filter(trip_type='round_trip')
        total = routes_query.count()
        routes = routes_query[(page - 1) * size: page * size]
        paginated_routes = PaginatedRoutesSchema(
            total=total,
            page=page,
            size=size,
            routes=[RouteSchema.from_orm(route) for route in routes]
        )
        return paginated_routes.dict()
    except Exception as e:
        raise HttpError(400, str(e))


@router.get("/route/{route_id}", response={200: RouteSchema, 404: ErrorResponse}, tags=["Routes"])
def get_route_by_id(request, route_id: UUID):
    """
    Get a route by its ID.

    This endpoint returns the details of a specific route identified by its UUID.
    """
    try:
        route = Route.objects.get(id=route_id)
        return RouteSchema.from_orm(route)
    except Route.DoesNotExist:
        return 404, {"detail": "Route not found"}
    except Exception as e:
        raise HttpError(400, str(e))


@router.get("/popular_routes", response={200: PaginatedRoutesSchema, 400: ErrorResponse}, tags=["Search Routes"])
def popular_routes(request, page: int = 1, size: int = 10):
    """
    Get a paginated list of popular routes.

    This endpoint returns a paginated list of popular routes.
    """
    try:
        # Example implementation, adjust according to your criteria for popularity
        routes_query = Route.objects.all()  # Adjust the query as needed
        total = routes_query.count()
        routes = routes_query[(page - 1) * size: page * size]
        return {
            "total": total,
            "page": page,
            "size": size,
            "routes": [{"id": str(route.id), "name": route.name, "description": route.description, "start_point": route.start_point, "end_point": route.end_point, "distance": route.distance, "duration": route.duration, "price": route.price} for route in routes]
        }
    except Exception as e:
        raise HttpError(400, detail=str(e))


@router.get("/search", response={200: PaginatedRoutesSchema, 400: ErrorResponse}, tags=["Search Routes"])
def search_routes(request, query: str, page: int = 1, size: int = 10):
    """
    Search for routes based on a query.

    This endpoint searches for routes where the name contains the query string.
    """
    try:
        # Search routes based on the query
        routes_query = Route.objects.filter(name__icontains=query)
        total = routes_query.count()
        routes = routes_query[(page - 1) * size: page * size]
        return {
            "total": total,
            "page": page,
            "size": size,
            "routes": [{"id": str(route.id), "name": route.name, "description": route.description, "start_point": route.start_point, "end_point": route.end_point, "distance": route.distance, "duration": route.duration, "price": route.price} for route in routes]
        }
    except Exception as e:
        raise HttpError(400, detail=str(e))
