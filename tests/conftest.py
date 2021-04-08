import pytest
from app.endpoints.services.weather import Weather


@pytest.fixture()
def weather():
    CITY    = 'Tandil'
    COUNTRY = 'Argentina'
    return Weather(CITY, COUNTRY)