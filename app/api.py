from fastapi import APIRouter
from .endpoints import weather_handler

api_router = APIRouter()

api_router.include_router(weather_handler.router, prefix='/weather')
