import datetime
import json
from termcolor import colored

async def response_time(client, url):
        response = {}
        t0 = 0
        response_time = 0

        t0 = datetime.datetime.now()
        response = await client.get(url)
        response_time = datetime.datetime.now() - t0

        print('{} Async call to OpenWeatherAPI tooks: {}'.format(
            colored('[METRIC]', 'green'),
            colored(response_time, color='green')
        ))

        return {
        'response': response,
        'response_time': response_time
    }

def cache_response_time(client, city):
    response = {}
    t0 = 0
    response_time = 0
    
    t0 = datetime.datetime.now()
    response = client.get(city)
    response_time = datetime.datetime.now() - t0

    print('{} chache response tooks: {}'.format(
            colored('[METRIC]', 'green'),
            colored(response_time, color='green')
        ))

    return {
        'response': response,
        'response_time': response_time
    }
