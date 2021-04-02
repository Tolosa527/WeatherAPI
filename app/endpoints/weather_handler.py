import redis
import json
from fastapi import APIRouter, Depends
from app.models.weather import Location,WeatherResponse
from .services.weather import Weather

router = APIRouter()

client = redis.Redis(host='127.0.0.1', port=6379)

@router.get('/', response_model=WeatherResponse)
async def Wheater_by_city_state(location: Location = Depends()):
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
        client.set(f'{location.city}', result_json,ex=60*5)
    except Exception as e:
        print(e)
    return result
