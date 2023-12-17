# weather_api/urls.py
from django.urls import path
from .views import WeatherPredictionListCreateView

urlpatterns = [
    path('', WeatherPredictionListCreateView.as_view(), name='WeatherPredictions'),
]