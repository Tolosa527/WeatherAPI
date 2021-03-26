from pydantic import BaseModel
import requests
import settings

class Weather(BaseModel):
    city: str
    country : str

    def get_from_open_weather(self):
        result_data = {}
        try:
            response = requests.get(
                f'{settings.OPENWEATHER_API_URL}?q={self.city},{self.country}&appid={settings.API_ID}'
            )
            json_response = response.json()

            result_data['local_name'] = "{},{}".format(
                json_response['name'],json_response['sys'].get('country')
            )
            result_data['temperature'] = self.__from_f_to_c(
                json_response['main'].get('temp')
            )
            # result_data['wind'] =
            # result_data['cloudiness'] =
            # result_data['pressure'] =
            # result_data['humidity'] =
            # result_data['sunrise'] =
            # result_data['sunset'] =
            # result_data['geo_coordinates'] =
            # result_data['requested_time'] =


        except Exception as e:
            raise e

        return result_data

    def __from_f_to_c(self, temperature):
        return temperature - 273.15
