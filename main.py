import settings
from app.api import api_router
from fastapi import FastAPI

api = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url= f"{settings.API_VERSION}/openapi.json"
)

api.include_router(api_router, prefix=settings.API_VERSION)
