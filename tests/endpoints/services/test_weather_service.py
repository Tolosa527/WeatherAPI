import asyncio
import pytest
import settings
from unittest.mock import AsyncMock, patch, Mock
from app.endpoints.services.weather import Weather
from tests.mocks.mocked_responses import Mocks_responses

def test_instance(weather):
    assert isinstance(weather, Weather)
    with pytest.raises(TypeError):
        weather = Weather()

@patch('app.endpoints.services.weather.httpx.get')
@pytest.mark.asyncio
async def test_get_from_open_weather(test_asyncClient_class, weather):
    # test_asyncClient_class = AsyncMock()
    # mocked_responses = Mocks_responses()
    # test_asyncClient_class.reponse.return_value = mocked_responses.get_openWeather_Response()
    # response = await weather.get_from_open_weather()
    # assert type(response) == type(mocked_responses.get_openWeather_Response())
    # assert response == mocked_responses.make_payload_response_mocked()
    pass

# print(test_asyncClient_class.reponse.return_value)
# test_asyncClient_class.result_data.return_value = mocked_responses.make_payload_response_mocked()
# mock_responses = Mocks_responses()
# mocked_json_response = mock_responses.get_openWeather_Response()
# test_asyncClient_instance.return_value = mocked_json_response
# test_asyncClient_class.result_data.return_value = test_asyncClient_instance
