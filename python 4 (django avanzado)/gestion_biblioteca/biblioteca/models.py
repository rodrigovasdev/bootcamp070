from django.db import models

# Create your models here.
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50)

class Autor(models.Model):
    nombre = models.CharField(max_length=50)

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    estado = models.CharField(choices=(('DISPONIBLE', 'Disponible'), ('PRESTADO', 'Prestado')))