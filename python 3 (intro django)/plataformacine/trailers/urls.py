from django.urls import path
from .views import indexView, nuevoTrailerView

urlpatterns = [
    path('', indexView),
    path('nuevo',nuevoTrailerView)
]
