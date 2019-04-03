from django.db import models

# Create your models here.

class Dostopr(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    rate = models.FloatField()
    photo = models.CharField(max_length=100, default='null')
