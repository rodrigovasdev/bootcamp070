from django.urls import path
from .views import new_libro_view, BookListView
urlpatterns = [
    path('formulario', new_libro_view),
    path('libros', BookListView.as_view())
]
