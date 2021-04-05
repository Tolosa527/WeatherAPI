import redis
import json
from redis import exceptions as redis_exceptions
from fastapi import APIRouter, Depends, HTTPException
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
    try:
        if client.get(f'{location.city}'):
            cache_data = json.loads(client.get(location.city))
            print(f'DATA FROM CACHE:\n{cache_data}')
            return cache_data
    except redis_exceptions.ConnectionError as redis_error:
        print(f'[WARNING] - ERROR TRYING TO GET INFO FROM CACHE: {redis_error}')
    try:
        weahter_instance = Weather(
            city=location.city,
            country=location.country
        )
        result = weahter_instance.get_from_open_weather()
        result_json = json.dumps(result)
        if result:
            try:
                client.set(f'{location.city}', result_json,ex=EXPIRATION_TIME)
                print(f'THIS DATA WAS SAVED IN CACHE:\n{result_json}')
            except redis_exceptions.ConnectionError as redis_error:
                print(f'[WARNING] - ERROR TRYING TO GET INFO FROM CACHE: {redis_error}')
    except ValueError as e:
        print(e)
        raise HTTPException(
            status_code=404,
            detail='data not found'
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail='Connection error'
        )
    return result
