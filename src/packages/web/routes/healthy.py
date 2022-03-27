from fastapi import APIRouter
from ..controllers import healthy_controller

healthy_router = APIRouter()


@healthy_router.get('/', tags=["healthy"])
async def root():
    return healthy_controller.root()


@healthy_router.get('/healthy', tags=["healthy"])
async def healthy():
    return healthy_controller.healthy()


@healthy_router.get('/liveness', tags=["healthy"])
async def liveness():
    return healthy_controller.liveness()
