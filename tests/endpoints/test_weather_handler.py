import pytest
import main
import settings
import json
from httpx import AsyncClient

# from async_asgi_testclient import TestClient


@pytest.mark.asyncio
async def test_weather_handler():
    async with AsyncClient(
        app=main.api, base_url=f"http://localhost{settings.API_VERSION}"
    ) as client:

        tandil = "Tandil"
        paris = "Paris"
        token = settings.API_TOKEN

        # BAD TOKEN
        response = await client.get(f"/weather/?city={tandil}&token_id=123")
        assert response.status_code == 401
        assert response.json() == {"detail": "Incorrect token authorization"}

        # CORRECT TOKEN
        response = await client.get(f"/weather/?city={tandil}&token_id={token}")
        assert response.status_code == 200
        assert response.json()["local_name"] == "Tandil,AR"

        response = await client.get(f"/weather/?city={paris}&token_id={token}")
        assert response.status_code == 200
        assert response.json()["local_name"] == "Paris,FR"
