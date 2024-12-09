from django.db import models

# Create your models here.
class PeliculaModel(models.Model):
    # Campos del modelo
    titulo = models.CharField(max_length = 200)
    trama = models.CharField(max_length = 200)
    fecha_estreno = models.DateTimeField()
    def __str__(self):
        return self.titulo