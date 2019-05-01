from django.db import models


# Create your models here.

class Workshop(models.Model):
    name = models.CharField(max_length=255)
