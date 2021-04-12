
class Mocks_responses():

    def __init__(self):
        pass

    def get_openWeather_Response(self):
        return {
            'coord': {'lon': -59.1357, 'lat': -37.3283},
            'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
            'base': 'stations',
            'main': {'temp': 289.37, 'feels_like': 288.85, 'temp_min': 289.37,'temp_max': 289.37, 'pressure': 1014, 'humidity': 69, 'sea_level': 1014, 'grnd_level': 991},
            'visibility': 10000,
            'wind': {'speed': 2.86, 'deg': 236, 'gust': 4.24},
            'clouds': {'all': 0}, 'dt': 1618174665,
            'sys': {'country': 'AR', 'sunrise': 1618136344, 'sunset': 1618176931},
            'timezone': -10800, 'id': 3427833, 'name': 'Tandil', 'cod': 200
        }

    def make_payload_response_mocked(self):
        return {
            'local_name': 'Tandil,AR',
            'temperature': 16.2,
            'wind': 'Gentle breeze,2.86 m/s,South Westerly',
            'pressure': '1014 hpa',
            'humidity': '69 %',
            'sunrise': '07:19',
            'sunset': '18:35',
            'geo_coordinates': '[-59.1357,-37.3283]',
            'requested_time': '2021-04-11 17:57:45',
            'cloudiness': ''
        }
