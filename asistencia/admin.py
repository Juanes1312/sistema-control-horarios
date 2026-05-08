from django.contrib import admin
from .models import Empleado, Marcaje

# Configuración de la cabecera del panel para que se vea personalizado
admin.site.site_header = "Administración Virtual Llantas"
admin.site.site_title = "Portal SCH"
admin.site.index_title = "Bienvenido al Sistema de Control de Horarios"

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    # Columnas que se verán en la lista
    list_display = ('id', 'get_full_name', 'documento', 'activo')
    # Filtros laterales
    list_filter = ('activo',)
    # Buscador por nombre o documento
    search_fields = ('user__first_name', 'user__last_name', 'documento')

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_full_name.short_description = 'Nombre Completo'

@admin.register(Marcaje)
class MarcajeAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'get_tipo_display', 'fecha_hora', 'ip_origen')
    list_filter = ('tipo', 'fecha_hora')
    # Solo lectura para que no se puedan alterar los registros de tiempo manualmente
    readonly_fields = ('fecha_hora', 'ip_origen')