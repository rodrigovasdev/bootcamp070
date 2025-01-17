from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Libro (models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
class Prestamo (models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    estado = models.CharField(choices=(('Activo', 'Activo'), ('Completado', 'Completado'),('Cancelado','Cancelado')), max_length=13)

    def __str__(self):
        return self.libro.titulo + ' - ' + self.usuario.username
