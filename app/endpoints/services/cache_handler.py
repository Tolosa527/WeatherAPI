import redis
import settings

def get_redis_client():
    #settings.REDIS_HOST
    client = redis.Redis(host='6379', port=settings.REDIS_PORT)
    return client
