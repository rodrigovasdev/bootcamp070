from django.urls import path
from .views import ver_libros, agregar_libro, editar_libro, actualizar_libro, eliminar_libro
urlpatterns = [
    path('', ver_libros, name='ver_libros'),
    path('agregar/', agregar_libro, name='agregar_libro'),
    path('editar/<int:pk>/', editar_libro, name='editar_libro'),
    path('actualizar/<int:id>/', actualizar_libro, name='actualizar_libro'),
    path('eliminar/<int:pk>/', eliminar_libro, name='eliminar_emp'),
]