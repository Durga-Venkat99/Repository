from django.db import models

# Create your models here.

class WeatherPrediction(models.Model):
    city = models.CharField(max_length=255)
    temperature = models.FloatField()
    description = models.CharField(max_length=255)
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    pressure = models.FloatField()
    visibility = models.IntegerField()
