from django.db import models

# Create your models here.
class BoardsModel(models.Model):
    # Campos del modelo
    titulo = models.CharField(max_length = 5)
    descripcion = models.CharField(max_length = 200)
    valoracion = models.IntegerField(help_text='Valor entre 0 y 10000')
    def __str__(self):
        return self.titulo
