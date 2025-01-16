from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    patente = models.CharField(max_length=10, unique=True)
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.patente}'

class Asignacion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField(auto_now_add=True)
    fecha_desasignacion = models.DateField(null=True, blank=True)
    estado = models.CharField(choices=(
        ('A', 'Activo'),
        ('Co', 'Completado'),
        ('Ca', 'Cancelado')
    ), max_length=2)

    def __str__(self):
        return f'{self.vehiculo} - {self.usuario}'