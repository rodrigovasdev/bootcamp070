from django.urls import path
from . import views
from .views import IndexView, PepitoView, obtenerFecha

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pepito', PepitoView.as_view(), name='pepito'),
    path('fecha/<name>', obtenerFecha, name='fecha'),
]