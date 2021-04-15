import pytest
import time
from tests.mocks.metrics import mocked_redis_class
from app.endpoints.services import metrics


def test_cache_response_time_metric():
    location = 'Tandil'
    response = metrics.cache_response_time(mocked_redis_class, location)
    assert int(response['response_time'].seconds) == 1