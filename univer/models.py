from django.db import models


# Create your models here.

class Dostopr(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    rate = models.FloatField()


class Topic(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
