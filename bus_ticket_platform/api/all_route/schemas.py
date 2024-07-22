
from pydantic import BaseModel
from typing import List

from ninja import Schema


class CreateRouteSchema(Schema):
    name: str
    description: str
    start_point: str
    end_point: str
    distance: float


class RouteSchema(BaseModel):
    origin: str
    destination: str
    duration: int  # duration in minutes
    price: float


class OneWayTripsSchema(BaseModel):
    routes: List[RouteSchema]


class RoundTripsSchema(BaseModel):
    routes: List[RouteSchema]


class SearchResponse(BaseModel):
    routes: List[RouteSchema]
