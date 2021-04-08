import pytest
from app.endpoints.services.weather import Weather
from tests.mocks.mocked_responses import get_openWeather_Response
import settings

url =  f'{settings.OPENWEATHER_API_URL}?q=Tandil,'
url += f'Argentina'
url += f'&appid={settings.API_ID}'

def test_instance(weather):
    assert isinstance(weather, Weather)
    with pytest.raises(TypeError):
        weather = Weather()
