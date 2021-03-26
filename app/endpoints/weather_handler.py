from fastapi import APIRouter
from app.models.weather import Weather

router = APIRouter()

@router.get('/')
async def Wheater_by_city_state(
        city:str, country:str
    ) -> Weather:
        weahter_instance = Weather(city=city, country=country)
        result = weahter_instance.get_from_open_weather()
        
        return result
