import pytest
import main
from fastapi.testclient import TestClient
#from async_asgi_testclient import TestClient

client = TestClient(main.api)

data = {'city': 'Tandil'}

#@pytest.mark.asyncio
def test_weather_handler():
    response = client.get("/weather/?city=Tandil")
    assert response.status_code == 200
