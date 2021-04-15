import redis
import settings

def get_redis_client():
    client = redis.Redis(host='0.0.0.0', port=settings.REDIS_PORT)
    return client
