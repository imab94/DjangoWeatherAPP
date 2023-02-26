from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import City
from .forms import CityForm
# from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.csrf import requires_csrf_token



# Create your views here.
def home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=Metric&appid=066a97ba6fafcdfa7b0942467078fac9'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weatherApp/weather.html', context)
