=====
Weather
=====

Django app moved to package to check the weather using OpenWeatherMap API.


Quick start
-----------

0. Create a django project and after that use ``pip`` to install this app::

    pip install git+https://github.com/albertosdneto/weather-django-package.git#egg=django-weather


1. Add "weather" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'weather',
    ]


2. Add necessary environment variables to ``settings.py`` at project source::

    OPEN_WEATHER_API_KEY = "YourKeyHere"

3. Include the weather URLconf in your project urls.py like this::

    path('weather/', include('weather.urls')),

4. Run ``python manage.py migrate`` to create the polls models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to check if everything is alright (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/weather/ to check the weather for a given city.
