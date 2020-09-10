from django.contrib import admin

from .models import Turismo
# Register your models here.
class TurismoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Turismo, TurismoAdmin)