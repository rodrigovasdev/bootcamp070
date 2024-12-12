from django.contrib import admin

# Register your models here.
class BoardsAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('titulo', 'valoracion')
    search_fields = ('titulo', 'descripcion')
    ordering = ('valoracion',)

from .models import BoardsModel
admin.site.register(BoardsModel,BoardsAdmin)