from django.db import models

# Create your models here.
class Sala(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    ubicacion = models.CharField(max_length=50)
    equipamiento = models.TextField()
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=50)
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()
    estado = models.CharField(choices=(('Confirmada','confirmada'), ('Pendiente','pendiente'), ('Cancelada','cancelada')), max_length=50)