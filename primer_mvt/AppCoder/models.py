from django.db import models

# Create your models here.

class familiares(models.Model):
    nombre_apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    cumpleaños=models.DateField()
