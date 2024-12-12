from django.db import models

# Create your models here.
class BoardsModel(models.Model):
    # Campos del modelo
    titulo = models.CharField(max_length = 5)
    descripcion = models.CharField(max_length = 200)
    valoracion = models.IntegerField(help_text='Valor entre 0 y 10000',default=0)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = "tablero"
        verbose_name_plural = "tableros"
        permissions = (
        ("es_miembro_uno", "Es miembro con prioridad uno"),
        ("development", "Permiso como desarrollador"),
        ("scrum_master", "Permiso como scrum master"),
        ("product_owner", "Permiso como Product Owner"),)

    def __str__(self):
        return self.titulo