from typing import List
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum


class TripType(str, Enum):
    one_way_trip = 'one_way_trip'
    round_trip = 'round_trip'


class CreateRouteSchema(BaseModel):
    """BaseModel for creating a new route."""
    name: str
    description: str
    start_point: str
    end_point: str
    distance: float
    trip_type: Optional[TripType] = None


class RouteSchema(BaseModel):
    """BaseModel for representing a route."""
    id: UUID
    name: str
    description: str
    start_point: str
    end_point: str
    distance: float
    duration: int
    price: float
    trip_type: str


class PaginatedRoutesSchema(BaseModel):
    """BaseModel for representing a paginated response of routes."""
    total: int
    page: int
    size: int
    routes: List[RouteSchema]


class OneWayTripsSchema(BaseModel):
    """BaseModel for representing a list of one-way trips."""
    routes: List[RouteSchema]


class RoundTripsSchema(BaseModel):
    """BaseModel for representing a list of round trips."""
    routes: List[RouteSchema]


class SearchResponse(BaseModel):
    """BaseModel for representing the search response of routes."""
    routes: List[RouteSchema]


class ErrorResponse(BaseModel):
    """BaseModel for representing an error response."""
    detail: str
