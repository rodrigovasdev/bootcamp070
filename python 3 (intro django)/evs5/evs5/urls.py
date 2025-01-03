"""
URL configuration for evs5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import navbarView, indexView, mostrarView, librosView, datosform_view, widget_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('navbar/', navbarView, name='navbar'),
    path('', indexView, name='index'),
    path('persona', mostrarView, name='persona'),
    path('libros', librosView, name='libros'),
    path('formulario', datosform_view, name='formulario'),
    path('formwidget', widget_view, name='widget'),
    path('formularios/', include('formulario.urls')),
]
