from django.db import models
import cloudinary.models


# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()


class Sertificat(models.Model):
    image = cloudinary.models.CloudinaryField('Сертификат')
