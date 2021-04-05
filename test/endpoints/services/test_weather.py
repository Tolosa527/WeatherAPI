import pytest
from app.endpoints.services import weather

def test_weather_instance():
    assert type(weather.Weather('Tandil', '')).__name__ == 'Weather'
    # Error assertion

def test_get_from_open_weather():
    pass

