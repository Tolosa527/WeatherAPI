import redis
from redis import exceptions as redis_exceptions

def get_redis_client():
    try:
        client = redis.Redis(host='redis', port=6379)
        return client
    except redis_exceptions.ConnectionError as redis_error:
        raise
        print(f'[WARNING] - ERROR TRYING TO CONNECT WITH REDIS CACHE STORE: {redis_error}')
