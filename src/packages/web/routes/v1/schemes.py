from fastapi import APIRouter
from packages.web.models.scheme_api import SchemesAPI
from ...controllers import schemes_controller

schemes_router = APIRouter()


@schemes_router.get('/get-one/{id}', tags=["schemes"])
async def get_by_id(id):
    return schemes_controller.get_by_id(id)


@schemes_router.get('/get-all', tags=["schemes"])
async def get_all():
    return schemes_controller.get_all()


@schemes_router.post('/create-one', tags=["schemes"])
async def create_one(item: SchemesAPI):
    return schemes_controller.create(item)
