from django.urls import path
from . import views
urlpatterns = [
    path('usuarios/', views.lista_usuario, name='lista_usuarios'),
    path('usuarios/nuevo', views.nuevo_usuario, name='nuevo_usuario'),
    path('usuarios/login', views.login_usuario, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/detalle/<int:id>', views.detalle_libro, name='detalle_libro'),
    path('libros/nuevo', views.nuevo_libro, name='nuevo_libro'),
    path('libros/editar/<int:id>', views.editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:id>', views.eliminar_libro, name='eliminar_libro'),
    path('prestamos/', views.lista_prestamos, name='lista_prestamos'),
    path('prestamos/nuevo', views.nuevo_prestamo, name='nuevo_prestamo'),
    path('prestamos/editar/<int:id>', views.editar_prestamo, name='editar_prestamo'),
    path('prestamos/eliminar/<int:id>', views.eliminar_prestamo, name='eliminar_prestamo'),
    path('prestamos/usuario/<int:id>', views.nuevo_usuario_prestamo, name='lista_prestamos_usuario'),

]