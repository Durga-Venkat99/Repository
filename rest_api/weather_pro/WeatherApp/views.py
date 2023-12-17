# views.py
from django.shortcuts import render
import requests
import datetime

def index(request):
    api_key = '6782593558af93a1bf94abf167ce179c'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    if request.method == 'POST':
        city = request.POST['city1']

        weather_data, daily_forecasts = fetch_weather_and_forecast(city, api_key, current_weather_url)

        context = {
            'weather_data': weather_data,
            'daily_forecasts': daily_forecasts,
        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

def fetch_weather_and_forecast(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

    # For simplicity, you can omit daily forecasts for now
    daily_forecasts = []

    return weather_data, daily_forecasts

