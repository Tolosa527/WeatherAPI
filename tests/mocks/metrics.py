import time
from tests.mocks import mocked_responses

class mocked_redis_class:
    
    def __init__(self):
        pass
    
    def get(self):
        response = mocked_responses.Mocks_responses()
        time.sleep(1)
        return response.make_payload_response_mocked()

