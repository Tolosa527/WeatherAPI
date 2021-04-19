import pytest
import time
from tests.mocks.mocked_classes import redis_class, httpx_class
from app.endpoints.services import metrics
import settings


def test_cache_response_time_metric():
    location = "Tandil"

    # SUCCES RESPONSE
    response = metrics.cache_response_time(redis_class, location)
    assert int(response["response_time"].seconds) == 1
    assert response.get("response") != None


@pytest.mark.asyncio
async def test_response_time_success():
    city = "Tandil"
    country = ""

    url = f"{settings.OPENWEATHER_API_URL}?q={city},{country}"
    url += f"&appid={settings.API_ID}"

    # SUCCES RESPONSE
    response = await metrics.response_time(httpx_class, url)
    assert int(response["response_time"].seconds) == 1
    assert response.get("response") != None


@pytest.mark.asyncio
async def test_response_time_failed():
    city = "Tandil"
    country = ""

    # url =  f'{settings.OPENWEATHER_API_URL}?q={city},{country}'
    # url += f'&appid={settings.API_ID}'
    url = ""
    # SUCCES RESPONSE
    response = await metrics.response_time(httpx_class, url)
    assert int(response["response_time"].seconds) == 1
    assert response.get("response") != None
