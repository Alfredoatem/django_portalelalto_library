from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from ContenidoApp.models import Festival, FestivalCont, Gastronomia, AreaVerde, Cultura,Museo, MuseoCont,Ballet,ArtesPlast,Artista,Tecnologia,TecnologiaCont,Arquitectura,ArquitecturaCont,WhipalaCont,Iglesia,Historia, Manifestacione, Iglesia

# Register your models here.
class FestivalAdmin(admin.ModelAdmin):
    list_display = ("titulo", "created")
    search_fields = ("titulo", "contenido", "created")
    list_filter = ("titulo", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class FestivalContAdmin(admin.ModelAdmin):
    list_display = ("titulo", "created", "director1")
    search_fields = ("titulo", "contenido", "created", "director1")
    list_filter = ("titulo", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class GastronomiaAdmin(admin.ModelAdmin):
    list_display = ("restaurant", "nombre", "precio", "telefono", "created")
    search_fields = ("restaurant","nombre","precio","telefono", "contenido", "created")
    list_filter = ("restaurant", "nombre","precio","lugar", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class AreaVerdeAdmin(admin.ModelAdmin):
    list_display = ("nombre", "lugar", "created")
    search_fields = ("nombre", "lugar", "created")
    list_filter = ("nombre", "lugar", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")
    
class CulturaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "created")
    search_fields = ("titulo", "contenido", "created")
    list_filter = ("titulo", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class MuseoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "created")
    search_fields = ("titulo", "contenido", "created")
    list_filter = ("titulo", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class MuseoContAdmin(admin.ModelAdmin):
    list_display = ("titulo", "tipo","created")
    search_fields = ("titulo","tipo", "contenido", "created")
    list_filter = ("titulo", "tipo","created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class BalletAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created")
    search_fields = ("nombre", "created")
    list_filter = ("nombre", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class ArtesPlastAdmin(admin.ModelAdmin):
    list_display = ("nombre", "contenido", "created")
    search_fields = ("nombre", "contenido", "created")
    list_filter = ("nombre", "contenido", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class ArtistaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created")
    search_fields = ("nombre", "created")
    list_filter = ("nombre", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "contenido", "created")
    search_fields = ("nombre", "contenido", "created")
    list_filter = ("nombre", "contenido", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class TecnologiaContAdmin(admin.ModelAdmin):
    list_display = ("titulo", "contenido", "created")
    search_fields = ("titulo", "contenido", "created")
    list_filter = ("titulo", "contenido", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class ArquitecturaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "contenido", "created")
    search_fields = ("nombre", "contenido", "created")
    list_filter = ("nombre", "contenido", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class ArquitecturaContAdmin(admin.ModelAdmin):
    list_display = ("titulo", "contenido", "created")
    search_fields = ("titulo", "contenido", "created")
    list_filter = ("titulo", "contenido", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")
class WhipalaContAdmin(admin.ModelAdmin):
    list_display = ("titulo", "contenido", "created")
    search_fields = ("titulo", "contenido", "created")
    list_filter = ("titulo", "contenido", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class IglesiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "contenido", "created")
    search_fields = ("titulo", "contenido", "created")
    list_filter = ("titulo", "contenido", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class HistoriaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "nombre1","nombre2","contenido", "created")
    search_fields = ("titulo","nombre1","nombre2", "contenido", "created")
    list_filter = ("titulo","nombre1","nombre2",  "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

class ManifestacioneAdmin(admin.ModelAdmin):
    list_display = ("titulo","contenido", "created")
    search_fields = ("titulo", "contenido", "created")
    list_filter = ("titulo", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

admin.site.register(Festival, FestivalAdmin)
admin.site.register(FestivalCont, FestivalContAdmin)
admin.site.register(Gastronomia, GastronomiaAdmin)
admin.site.register(AreaVerde, AreaVerdeAdmin)
admin.site.register(Cultura, CulturaAdmin)
admin.site.register(Museo, MuseoAdmin)
admin.site.register(MuseoCont, MuseoContAdmin)
admin.site.register(Ballet, BalletAdmin)
admin.site.register(ArtesPlast, ArtesPlastAdmin)
admin.site.register(Artista,ArtistaAdmin)
admin.site.register(Tecnologia, TecnologiaAdmin)
admin.site.register(TecnologiaCont, TecnologiaContAdmin)
admin.site.register(Arquitectura, ArquitecturaAdmin)
admin.site.register(ArquitecturaCont, ArquitecturaContAdmin)
admin.site.register(WhipalaCont, WhipalaContAdmin)
admin.site.register(Iglesia,IglesiaAdmin)
admin.site.register(Historia,HistoriaAdmin)
admin.site.register(Manifestacione,ManifestacioneAdmin)


