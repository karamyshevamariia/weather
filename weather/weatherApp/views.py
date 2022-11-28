import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

# Create your views here.
def index(request):
    apid = '2bff5d501fc9f136ba63e0fff9f15640'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+apid

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()


    form=CityForm()

    cities = City.objects.all()
    all_cities=[]
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city':city.name,
            'temp':res['main']['temp'],
            'icon': res['weather'][0]['icon'],
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form':form}

    return render(request, 'weatherApp/index.html', context)