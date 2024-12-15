from django.contrib import admin


admin.site.site_header = 'Curso Django'
admin.site.index_title = 'Panel de control Proyecto Django'
admin.site.site_title = 'Administrador Django'

# Register your models here.
class BoardsAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('clasificacion','titulo', 'valoracion')
    search_fields = ('titulo', 'descripcion')
    ordering = ('valoracion',)
    list_filter = ('creado','valoracion')
    def clasificacion(self, obj):
        return "Alto" if obj.valoracion >= 5 else "Bajo"

from .models import BoardsModel
admin.site.register(BoardsModel,BoardsAdmin)