from django.shortcuts import render
import requests
import datetime

def index(request):
    api_key = '6782593558af93a1bf94abf167ce179c'
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'

    if request.method == 'POST':
        city = request.POST['city1']

        weather_data, daily_forecasts = fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url)

        context = {
            'weather_data': weather_data,
            'daily_forecasts': daily_forecasts,
        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

def fetch_weather_and_forecast(city, api_key, current_weather_url, forecast_url):
    # Get current weather data
    current_response = requests.get(current_weather_url.format(city, api_key)).json()

    # Check if 'main' key is present in the response
    if 'main' not in current_response:
        return None, None

    lat, lon = current_response['coord']['lat'], current_response['coord']['lon']

    # Get forecast data
    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()

    weather_data = {
        'city': city,
        'temperature': round(current_response['main']['temp'] - 273.15, 2),
        'description': current_response['weather'][0]['description'],
        'icon': current_response['weather'][0]['icon'],
    }

    daily_forecasts = []
    for daily_data in forecast_response['daily'][:5]:
        daily_forecasts.append({
            'day': datetime.datetime.fromtimestamp(daily_data['dt']).strftime('%A'),
            'min_temp': round(daily_data['temp']['min'] - 273.15, 2),
            'max_temp': round(daily_data['temp']['max'] - 273.15, 2),
            'description': daily_data['weather'][0]['description'],
            'icon': daily_data['weather'][0]['icon'],
        })

    return weather_data, daily_forecasts
