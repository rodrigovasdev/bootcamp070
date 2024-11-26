from django.urls import path
from .views import PalindromoView
urlpatterns = [
    path('<palabra>', PalindromoView, name='palindromo'),
]