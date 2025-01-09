from django.db import models

# Create your models here.
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    estado = models.CharField(choices=(('DISPONIBLE', 'Disponible'), ('PRESTADO', 'Prestado')))
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo