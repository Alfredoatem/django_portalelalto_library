from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Distrito, Zona, UnidadEducativa, Hoteles, Restaurant, Empresa, Hospital, Transporte, Comunicado, Noticia
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class DistritoResource(resources.ModelResource):
    class Meta:
        model = Distrito

class DistritoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("distrito", "created")
    search_fields = ("distrito", "created")
    list_filter = ("distrito","created")
    date_hierarchy = "created"
    readonly_fields=('created', 'updated')
    resource_class = DistritoResource

class ZonaResource(resources.ModelResource):
    class Meta:
        model = Zona

class ZonaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("zona", "created")
    search_fields = ("zona", "created")
    list_filter = ("zona","created")
    date_hierarchy = "created"
    readonly_fields=('created', 'updated')
    resource_class = ZonaResource

class UnidadEducativaResource(resources.ModelResource):
    class Meta:
        model = UnidadEducativa

class UnidadEducativaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre","estado","distrito","zona","direccion","telefono","web","email")
    search_fields = ("nombre","distrito","contenido","descripcion","direccion","telefono","web","email","created")
    list_filter = ("nombre","distrito","zona","created")
    date_hierarchy = "created"
    readonly_fields=('created', 'updated')
    resource_class = UnidadEducativaResource

class HotelesResource(resources.ModelResource):
    class Meta:
        model = Hoteles

class HotelesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre","estado","tipo","distrito","zona","direccion","telefono","web","email")
    search_fields = ("nombre","tipo","distrito","zona","contenido","descripcion","direccion","telefono","web","email","created")
    list_filter = ("nombre","tipo","distrito","zona","created")
    date_hierarchy = "created"
    readonly_fields=('created', 'updated')
    resource_class = HotelesResource

class RestaurantResource(resources.ModelResource):
    class Meta:
        model = Restaurant

class RestaurantAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre","estado","distrito","zona","direccion","telefono","web","email")
    search_fields = ("nombre","distrito","zona","contenido","direccion","telefono","web","email","created")
    list_filter = ("nombre","horario","distrito","zona","created")
    date_hierarchy = "created"
    readonly_fields=('created', 'updated')
    resource_class = RestaurantResource

class EmpresaResource(resources.ModelResource):
    class Meta:
        model = Empresa

class EmpresaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre","estado","distrito","zona","direccion","telefono","web","email")
    search_fields = ("nombre","distrito","zona","contenido","direccion","telefono","web","email","created")
    list_filter = ("nombre","distrito","zona","created")
    date_hierarchy = "created"
    readonly_fields=('created', 'updated')
    resource_class = EmpresaResource

class HospitalResource(resources.ModelResource):
    class Meta:
        model = Hospital

class HospitalAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre","tipo","estado","distrito","zona","direccion","telefono","web","email")
    search_fields = ("nombre","distrito","zona","tipo","contenido","direccion","telefono","web","email","created")
    list_filter = ("nombre","tipo","distrito","zona","created")
    date_hierarchy = "created"
    readonly_fields=('created', 'updated')
    resource_class = HospitalResource

class TransporteResource(resources.ModelResource):
    class Meta:
        model = Transporte

class TransporteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre","tipo","estado","distrito","zona","direccion","telefono","web","email")
    search_fields = ("nombre","distrito","zona","tipo","sindicato","contenido","linea","direccion","telefono","web","email","created")
    list_filter = ("nombre","tipo","distrito","sindicato","linea","zona","created")
    date_hierarchy = "created"
    readonly_fields=('created', 'updated')
    resource_class = TransporteResource

class ComunicadoResource(resources.ModelResource):
    class Meta:
        model = Transporte

class ComunicadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre","estado")
    search_fields = ("nombre","created")
    list_filter = ("nombre","created")
    date_hierarchy = "created"
    readonly_fields=('created', 'updated')
    resource_class = ComunicadoResource

class NoticiaResource(resources.ModelResource):
    class Meta:
        model = Transporte

class NoticiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("nombre","estado")
    search_fields = ("nombre","created")
    list_filter = ("nombre","created")
    date_hierarchy = "created"
    readonly_fields=('created', 'updated')
    resource_class = NoticiaResource

admin.site.register(Distrito, DistritoAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(UnidadEducativa, UnidadEducativaAdmin)
admin.site.register(Hoteles, HotelesAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Transporte, TransporteAdmin)
admin.site.register(Comunicado, ComunicadoAdmin)
admin.site.register(Noticia, NoticiaAdmin)
