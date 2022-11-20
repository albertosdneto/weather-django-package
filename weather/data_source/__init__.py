import requests
from django.conf import settings

OPEN_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'


def get_weather(city):
    response = requests.get(OPEN_WEATHER_URL.format(city, settings.OPEN_WEATHER_API_KEY)).json()
    city_weather = {
        'city': city,
        'temperature': response.get('main', {}).get('temp', None),
        'description': response.get('weather', [{}])[0].get('description', None),
        'icon': response.get('weather', [{}])[0].get('icon', None),
    }
    return city_weather
