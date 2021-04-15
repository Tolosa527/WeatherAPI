import pytest
from app.endpoints.services.weather import Weather
import time

@pytest.fixture()
def weather():
    CITY    = 'Tandil'
    COUNTRY = 'Argentina'
    return Weather(CITY, COUNTRY)

@pytest.fixture()
def get_request_timer():
    time.sleep(1)
    return True
