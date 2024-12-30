from django.db import models

# Create your models here.
class Automotriz(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class ModeloCarro(models.Model):
    nombre = models.CharField(max_length=255)
    automotriz = models.ForeignKey(Automotriz,on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre