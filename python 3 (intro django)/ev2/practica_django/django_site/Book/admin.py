from django.contrib import admin
from .models import BookModel
# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('titulo', 'descripcion','valoracion')
    list_filter = ('fecha_modificacion','valoracion','fecha_creacion')
admin.site.register(BookModel,BooksAdmin)