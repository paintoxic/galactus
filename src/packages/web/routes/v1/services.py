from fastapi import APIRouter
from packages.web.models.service_api import ServiceAPI
from ...controllers import services_controller

services_router = APIRouter()


@services_router.get('/get-one/{id}', tags=["services"])
async def get_by_id(id):
    return services_controller.get_by_id(id)


@services_router.get('/get-all', tags=["services"])
async def get_all():
    return services_controller.get_all()


@services_router.post('/create-one', tags=["services"])
async def create_one(item: ServiceAPI):
    return services_controller.create(item)
