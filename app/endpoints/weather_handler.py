from fastapi import APIRouter, Depends
from app.models.weather import Location,WeatherResponse
from .views.weather_view import Weather

router = APIRouter()

@router.get('/', response_model=WeatherResponse)
async def Wheater_by_city_state(location: Location = Depends()):
    result = ''
    try:
        weahter_instance = Weather(
            city=location.city,
            country=location.country
        )
        result = weahter_instance.get_from_open_weather()
    except Exception as e:
        print(e)

    return result
