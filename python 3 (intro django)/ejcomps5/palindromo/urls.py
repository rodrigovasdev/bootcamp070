from django.urls import path
from .views import PalindromoView, PalindromoIndexView
urlpatterns = [
    path('<palabra>', PalindromoView, name='palindromo'),
    path('', PalindromoIndexView, name='index'),
]