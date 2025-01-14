from django.urls import path
from . import views
urlpatterns = [

    path('salas', views.lista_salas),
    path('salas/<int:id>', views.detalle_sala),
    path('salas/nueva/', views.registrar_sala),
    path('salas/<int:id>/editar', views.editar_sala),
    path('salas/<int:id>/eliminar', views.eliminar_sala),
]
