from django.db import models

# Create your models here.
class Fabricante(models.Model):
    nombre = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    fabricante = models.ForeignKey(Fabricante,on_delete=models.SET_NULL, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre