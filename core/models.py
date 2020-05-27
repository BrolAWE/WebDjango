from django.db import models
import cloudinary.models


# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()


class Dostopr(models.Model):
    name = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    rate = models.FloatField()
    photo = models.CharField(max_length=100)
    url = models.CharField(max_length=200, default="null")


class Sertificat(models.Model):
    image = cloudinary.models.CloudinaryField('Сертификат')
