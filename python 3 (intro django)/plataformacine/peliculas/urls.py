from django.urls import path
from .views import nuevaPeliculaView, indexView, peliculaform_view

urlpatterns = [
    path('', indexView),
    path('nueva', nuevaPeliculaView),
    path('formulario',peliculaform_view)

]
