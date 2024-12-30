from django.urls import path
from .views import index, add, addproducto

urlpatterns = [
    path('lista', index),
    path('add/', add),
    path('add/addproduct/',addproducto),

]