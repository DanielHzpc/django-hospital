from django.db import models

# Create your models here.

class Planta(models.Model):
    nombre = models.CharField(max_length=100)
    numeroCamas = models.IntegerField()