
from django.db import models

# Create your models here.
class LibroModel(models.Model):
    # Campos del modelo
    titulo = models.CharField(max_length = 50)
    autor = models.CharField(max_length = 50)
    valoracion = models.IntegerField(help_text='Valor entre 0 y 10000',default=0)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.titulo