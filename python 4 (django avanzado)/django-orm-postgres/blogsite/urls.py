
from django.urls import path
from .views import index, agregar, agregarregistro
urlpatterns = [
    path('tablitafeliz', index),
    path('agregar/', agregar, name='agregar'),
    path('agregar/agregarregistro/', agregarregistro,name='agregarr'),


]
