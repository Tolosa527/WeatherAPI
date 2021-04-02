import redis
import json
from fastapi import APIRouter, Depends
from app.models.weather import Location,WeatherResponse
from .services.weather import Weather
from .services.cache_handler import get_redis_client

router = APIRouter()

EXPIRATION_TIME = 60*5 # five minutes

@router.get('/', response_model=WeatherResponse)
async def Wheater_by_city_state(
        location: Location = Depends(),
        client: redis = Depends(get_redis_client)
    ):
    result = ''
    if client.get(f'{location.city}'):
        cache_data = json.loads(client.get(location.city))
        print(f'DATA FROM CACHE:\n{cache_data}')
        return cache_data
    try:
        weahter_instance = Weather(
            city=location.city,
            country=location.country
        )
        result = weahter_instance.get_from_open_weather()
        result_json = json.dumps(result)
        print(f'THIS DATA WAS SAVED IN CACHE:\n{result_json}')
        client.set(f'{location.city}', result_json,ex=EXPIRATION_TIME)
    except Exception as e:
        print(e)
    return result
