from django.db import models

# Create your models here.

class Becas(models.Model):
    nombre = models.CharField(max_length=250)
    porcentaje = models.IntegerField()
    pais = models.CharField(max_length=100)
    universidad = models.CharField(max_length=100)
    requerimiento = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre