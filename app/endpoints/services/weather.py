import datetime
import settings
import httpx
from app.endpoints.services import metrics
from termcolor import colored


class Weather():

    def __init__(self, country, city):
        self.country = country,
        self.city = city

    async def get_from_open_weather(self):
        result_data = {}
        url =  f'{settings.OPENWEATHER_API_URL}?q={self.city},{self.country}'
        url += f'&appid={settings.API_ID}'
        try:
            async with httpx.AsyncClient() as client:
                print('{} {}'.format(
                    colored("[REQUEST]", color="green"),
                    url
                ))
                if (settings.METRICS_LOG):
                    weather_response = await metrics.response_time(client, url)
                    response = weather_response.get('response', None)
                else:
                    response = await client.get(url)
                print('{} {}'.format(
                    colored("[RESPONSE]", color="green"),
                    response.json()
                ))
                result_data = self.__make_payload_response(response.json())
        except KeyError as error:
            raise KeyError(
                str(error)
            )
        except Exception as error:
            raise Exception(
                str(error)
            )
        return result_data


    def __from_f_to_c(self, temperature):
        result = temperature - 273.15
        result = round(result, ndigits=1)
        return result


    def __make_payload_response(self, json_object):

        payload = {}

        payload['local_name'] = "{},{}".format(
            json_object['name'],json_object['sys'].get('country')
        )
        payload['temperature'] = self.__from_f_to_c(
            json_object['main'].get('temp')
        )
        payload['wind'] = "{},{} m/s,{}".format(
            "Gentle breeze", # I have to replace this line
            json_object['wind'].get('speed'),
            self.__get_direction(json_object['wind'].get('deg'))
        )
        payload['pressure'] = "{} hpa".format(
            json_object['main'].get('pressure')
        )
        payload['humidity'] = "{} %".format(
            json_object['main'].get('humidity')
        )
        payload['sunrise'] = "{}".format(
            self.__get_time(json_object['sys'].get('sunrise'))
        )
        payload['sunset'] = "{}".format(
            self.__get_time(json_object['sys'].get('sunset'))
        )
        payload['geo_coordinates'] = "[{},{}]".format(
            json_object['coord'].get('lon'),
            json_object['coord'].get('lat')
        )
        payload['requested_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        payload['cloudiness'] = '' # I have to replace this

        return payload


    def __get_direction(self, degree):
        result = ''
        if   degree > 337.5 : result = 'Northerly'
        elif degree > 292.5 : result = 'North Westerly'
        elif degree > 247.5 : result = 'Westerly'
        elif degree > 202.5 : result = 'South Westerly'
        elif degree > 157.5 : result = 'Southerly'
        elif degree > 122.5 : result = 'South Easterly'
        elif degree > 67.5  : result = 'Easterly'
        elif degree > 22.5  : result = 'North Easterly'
        else: result = 'Northerly'
        return result


    def __get_time(self, data):
        return  datetime.datetime.fromtimestamp(data).strftime('%H:%M')
