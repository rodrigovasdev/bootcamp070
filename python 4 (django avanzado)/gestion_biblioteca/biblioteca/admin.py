from django.contrib import admin
from .models import Biblioteca, Autor, Libro
# Register your models here.

admin.site.register(Biblioteca)
admin.site.register(Autor)
admin.site.register(Libro)