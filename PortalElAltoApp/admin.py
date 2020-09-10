from django.contrib import admin

#Para la cabecera del panel de admin
from django.contrib.auth.models import Group

from .models import Snippet, PageView
from ContenidoApp.models import Historia
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html
# Register your models here.
admin.site.site_header = 'Administración del Portal Web El Alto'

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'font_size_html_display')
    list_filter = ('created',)
    change_list_template = 'admin/snippets/snippets_change_list.html'

    readonly_fields = ('body_preview',)
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('fontsize/<int:size>/', self.change_font_size)
        ]

        return custom_urls + urls
    
    def change_font_size(self, request, size):
        self.model.objects.all().update(font_size=size)
        self.message_user(request, 'Font size cambiado satisfactoriamente!!!')
        return HttpResponseRedirect("../")

    def font_size_html_display(self, obj):
        display_size = obj.font_size if obj.font_size <= 30 else 30 
        return format_html(
            f'<span style="font-size: {display_size}px;">{obj.font_size}</span>'
        )
class PageViewAdmin(admin.ModelAdmin):
    list_display = ["hits"]
    readonly_fields = ["hits"]

admin.site.register(PageView, PageViewAdmin)
admin.site.register(Snippet, SnippetAdmin)
admin.site.unregister(Group)
