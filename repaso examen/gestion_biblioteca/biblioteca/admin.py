from django.contrib import admin
from .models import Libro, Prestamo
# Register your models here.

admin.site.register(Libro)
admin.site.register(Prestamo)

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

    # Campos que se mostrarán en el formulario de creación y edición
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "first_name", "last_name", "password1", "password2"),
        }),
    )

    # Mostrar el campo `email` en la lista de usuarios
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")

# Desregistrar el modelo original y registrarlo con la clase personalizada
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
