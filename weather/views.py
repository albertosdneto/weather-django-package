import requests
from django.conf import settings
from django.shortcuts import render

from weather.models import City

from .forms import CityForm

OPEN_WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'


def index(request):
    city = 'Teresina'
    if request.method == 'POST':
        form = CityForm(request.POST)
        city = form.data.get('name')

    form = CityForm()

    response = requests.get(OPEN_WEATHER_URL.format(city, settings.OPEN_WEATHER_API_KEY)).json()
    city_weather = {
        'city': city,
        'temperature': response.get('main', {}).get('temp', None),
        'description': response.get('weather', [{}])[0].get('description', None),
        'icon': response.get('weather', [{}])[0].get('icon', None),
    }

    context = {'city_weather': city_weather, 'form': form}
    return render(request, 'weather/index.html', context)
