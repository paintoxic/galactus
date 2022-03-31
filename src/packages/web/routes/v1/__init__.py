from fastapi import APIRouter
from .schemes import schemes_router

api_v1 = APIRouter()

api_v1.include_router(schemes_router, prefix='/schemes')
