from django.shortcuts import render

# Create your views here.
# weather_api/views.py
from rest_framework import generics
from .models import WeatherPrediction
from .serializers import WeatherPredictionSerializer

class WeatherPredictionListCreateView(generics.ListCreateAPIView):
    queryset = WeatherPrediction.objects.all()
    serializer_class = WeatherPredictionSerializer
