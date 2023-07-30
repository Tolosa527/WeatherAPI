import redis
import settings


def get_redis_client():
    """
    This method will return a redis client instance
    """
    client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    return client
