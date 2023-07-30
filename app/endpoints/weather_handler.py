import json
import redis
import settings

from fastapi import APIRouter, Depends, HTTPException, status
from redis import exceptions
from typing import Dict
from termcolor import colored

from app.services import auth
from app.services.cache_handler import get_redis_client
from app.services.weather import Weather
from app.services import metrics
from app.models.weather import Location, WeatherResponse

EXPIRATION_TIME = settings.REDIS_EXPIRATION_TIME

router = APIRouter()


@router.post("/", response_model=WeatherResponse)
async def Wheater_by_city_state(
    location: Location = Depends(),
    client: redis = Depends(get_redis_client),
    username: str = Depends(auth.get_current_username),
) -> Dict:
    result = {}

    try:
        if client.get(f"{location.city}"):
            cache_data = {}
            if settings.METRICS_LOG:
                cache_data = metrics.cache_response_time(client, location.city)
            cache_data = json.loads(client.get(location.city))
            print(
                "{}{}".format(colored("[DATA FROM CACHE]", color="green"), cache_data)
            )
            return cache_data
    except exceptions.ConnectionError as e:
        print(
            "{} Error occurs trying to get data from cache: {}".format(
                colored("[WARNING]", color="yellow"), str(e)
            )
        )

    try:
        weahter_instance = Weather(city=location.city, country=location.country)
        result = await weahter_instance.get_from_open_weather()
        result_json = json.dumps(result)
    except KeyError as error:
        print(
            "{} Error traying to get from OPEN weather: {}".format(
                colored("[ERROR]", color="red"), error
            )
        )
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="City not found")
    except Exception as error:
        print(
            "{} Error traying to get from OPEN weather: {}".format(
                colored("[ERROR]", color="red"), error
            )
        )
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        )

    try:
        client.set(f"{location.city}", result_json, ex=EXPIRATION_TIME)
        print("{}{}".format(colored("[SAVED IN CACHE]", color="green"), result_json))
    except exceptions.ConnectionError as e:
        print(
            "{} Error occurs trying to save in cache: {}".format(
                colored("[WARNING]", color="yellow"), str(e)
            )
        )
    return result
