from django.shortcuts import render, redirect
import urllib.request
import json


# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=7c4c223f52ed2e4f196cbd629001f62a')
        
        str_response = source.read().decode('utf-8')
        list_of_data = json.loads(str_response)
        ##list_of_data = json.loads(source)

        data= {
            "cityname" : city.title(),
            "main" : str(list_of_data['weather'][0]['main']),
            "description" : str(list_of_data['weather'][0]['description']),
            "icon" : list_of_data['weather'][0]['icon'],
            "temp" : str(list_of_data['main']['temp']),
            "temp_min" : str(list_of_data['main']['temp_min']),
            "temp_max" : str(list_of_data['main']['temp_max']),
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']),
            "feels_like" : str(list_of_data['main']['feels_like'])
        }
    else:
        data = {}
    return render(request,'base.html', data)
