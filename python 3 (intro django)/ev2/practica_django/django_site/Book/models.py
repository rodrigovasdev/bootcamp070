from django.db import models

# Create your models here.
class BookModel(models.Model):
    # Campos del modelo
    titulo = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 200)
    valoracion = models.IntegerField(help_text='Valor entre 0 y 10000',default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "Libro Gatito"
        verbose_name_plural = "Libros Gatitos"
        ordering = ["-fecha_creacion"] 
    def __str__(self):
        return self.titulo