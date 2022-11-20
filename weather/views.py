from django.shortcuts import render
from .data_source import get_weather
from .forms import CityForm


def index(request):
    human = False
    city_weather = {}
    form = CityForm()
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.data.get('name')
            city_weather = get_weather(city)

    context = {'city_weather': city_weather, 'form': form, 'human': human}
    return render(request, 'weather/index.html', context)
