from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Comentario

# Register your models here.
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "created")
    search_fields = ("nombre", "contenido", "created")
    list_filter = ("nombre", "created")
    date_hierarchy = "created"
    readonly_fields = ("created", "updated")

admin.site.register(Comentario, ComentarioAdmin)