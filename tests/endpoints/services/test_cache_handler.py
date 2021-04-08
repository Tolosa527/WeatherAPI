import pytest
from app.endpoints.services import cache_handler

def test_redis_client():
    client = cache_handler.get_redis_client()
    assert type(client).__name__ == 'Redis'
