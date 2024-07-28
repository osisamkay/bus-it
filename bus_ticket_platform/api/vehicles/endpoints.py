# endpoints.py
from ninja import Router
from ninja.errors import HttpError
from typing import List
from .schema import ErrorResponse, VehicleSchema
from .models import Vehicle
from ..auth.endpoints import AuthBearer

router = Router()


@router.post("/create_vehicle", response={200: VehicleSchema, 400: ErrorResponse}, tags=["Vehicles"], auth=AuthBearer())
def create_vehicle(request, payload: VehicleSchema):
    try:
        vehicle = Vehicle.objects.create(**payload.dict())
        return VehicleSchema.from_orm(vehicle)
    except Exception as e:
        raise HttpError(400, str(e))


@router.get("/view_vehicles", response=List[VehicleSchema], tags=["Vehicles"], auth=AuthBearer())
def view_vehicles(request):
    try:
        vehicles = Vehicle.objects.all()
        return [VehicleSchema.from_orm(vehicle) for vehicle in vehicles]
    except Exception as e:
        raise HttpError(400, str(e))
