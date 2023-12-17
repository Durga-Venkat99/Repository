from django.db import models

# Create your models here.
class bookmodel(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.IntegerField()
    