from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Proyecto
# Register your models here.

class ProyectoResource(resources.ModelResource):
    class Meta:
        model = Proyecto

class ProyectoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ("titulo", "created")
    #search_fields permite buscar
    search_fields = ("titulo", "contenido", "created")
    #para filrar
    list_filter = ("titulo","created")
    #para filtrar fecha
    date_hierarchy = "created"
    #muestra las fechas de creacion y modificación
    readonly_fields=('created', 'updated')
    #para importar y exportar
    resource_class = ProyectoResource
#admin.site.register(nombre de la clase de models, Aplicacion)
admin.site.register(Proyecto, ProyectoAdmin)


