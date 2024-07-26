from ninja import Schema
from typing import List
from uuid import UUID


class CreateRouteSchema(Schema):
    """Schema for creating a new route."""
    name: str
    description: str
    start_point: str
    end_point: str
    distance: float
    trip_type: str


class RouteSchema(Schema):
    """Schema for representing a route."""
    id: UUID
    name: str
    description: str
    start_point: str
    end_point: str
    distance: float
    duration: int
    price: float
    trip_type: str


class PaginatedRoutesSchema(Schema):
    """Schema for representing a paginated response of routes."""
    total: int
    page: int
    size: int
    routes: List[RouteSchema]


class OneWayTripsSchema(Schema):
    """Schema for representing a list of one-way trips."""
    routes: List[RouteSchema]


class RoundTripsSchema(Schema):
    """Schema for representing a list of round trips."""
    routes: List[RouteSchema]


class SearchResponse(Schema):
    """Schema for representing the search response of routes."""
    routes: List[RouteSchema]


class ErrorResponse(Schema):
    """Schema for representing an error response."""
    detail: str
