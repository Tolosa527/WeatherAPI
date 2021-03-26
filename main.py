from fastapi import FastAPI
from app.api import api_router
import settings

api = FastAPI(
    title=settings.PROJECT_NAME,
    version='0.0.1',
    openapi_url= f"{settings.API_VERSION}/openapi.json"
)

api.include_router(api_router, prefix=settings.API_VERSION)
