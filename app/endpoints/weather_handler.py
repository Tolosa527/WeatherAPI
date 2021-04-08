import json
import redis
import settings
from .services.cache_handler import get_redis_client
from .services.weather import Weather
from app.models.weather import Location,WeatherResponse
from fastapi import APIRouter, Depends, HTTPException
from redis import exceptions

expiration_time = settings.REDIS_EXPIRATION_TIME

router = APIRouter()

@router.get('/', response_model=WeatherResponse)
async def Wheater_by_city_state(
        location: Location = Depends(),
        client: redis = Depends(get_redis_client)
    ):
    result = {}
    try:
        if client.get(f'{location.city}'):
            cache_data = json.loads(client.get(location.city))
            print(f'DATA FROM CACHE:\n{cache_data}')
            return cache_data
    except exceptions.ConnectionError as e:
        print('[Warning]-Error occurs trying to get from the cache')

    try:
        weahter_instance = Weather(
            city=location.city,
            country=location.country
        )
        result = await weahter_instance.get_from_open_weather()
        result_json = json.dumps(result)
    except Exception as e:
        print(e)
        raise HTTPException(500)

    try:
        client.set(f'{location.city}', result_json,ex=expiration_time)
        print(f'THIS DATA WAS SAVED IN CACHE:\n{result_json}')
    except exceptions.ConnectionError as e:
        print('[Warning]-Error occurs trying to save in cache')

    return result
