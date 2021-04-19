import time
from tests.mocks import mocked_responses


class redis_class:
    def __init__(self):
        pass

    def get(self):
        response = mocked_responses.Mocks_responses()
        time.sleep(1)
        return response.make_payload_response_mocked()


class httpx_class:
    def __init__(self):
        pass

    async def get(self):
        mock = mocked_responses.Mocks_responses()
        response = await mock.get_openWeather_Response()
        time.sleep(1)
        return response
