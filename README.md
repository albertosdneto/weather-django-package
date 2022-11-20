# Weather

Django app moved to package to check the weather using OpenWeatherMap API.


Access It
-----------
[Link to running example]


Quick start
-----------

1. Create a django project and after that use ``pip`` to install this app::
   ```
   pip install git+https://github.com/albertosdneto/weather-django-package.git#egg=django-weather
   ```

2. Add ``weather`` and ``captcha`` to your INSTALLED_APPS setting like this::
   ```
   INSTALLED_APPS = [
       ...
       'weather',
       'captcha',
   ]
   ```

3. Add necessary environment variables to ``settings.py`` at project source::
   ```
   OPEN_WEATHER_API_KEY = "YourKeyHere"
   ```

4. Include ``weather`` and ``captcha`` URLconf in your project urls.py like this::
   ```
   path('weather/', include('weather.urls')),
   path('captcha/', include('captcha.urls')),
   ```

5. Run ``python manage.py migrate`` to create the polls models.

6. Start the development server and visit http://127.0.0.1:8000/admin/
   to check if everything is alright (you'll need the Admin app enabled).

7. Visit http://127.0.0.1:8000/weather/ to check the weather for a given city.


Resources
-----------

- [Background Video]
- [Bootstrap Template]

[Background Video]: https://www.pexels.com/video/drone-view-of-big-waves-rushing-to-the-shore-3571264/

[Bootstrap Template]: https://startbootstrap.com/previews/coming-soon

[Link to running example]: https://albertosdneto.pythonanywhere.com/weather/