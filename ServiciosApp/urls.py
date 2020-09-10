from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('distrito', views.distrito, name="Distrito"),
    path('zona', views.zona, name="Zona"),
    path('unidadeducativa', views.unidadeducativa, name="UnidadEducativa"),
    path('hoteles', views.hoteles, name="Hoteles"),
    path('restaurant', views.restaurant, name="Restaurant"),
    path('empresa', views.empresa, name="Empresa"),
    path('hospital', views.hospital, name="Hospital"),
    path('transporte', views.transporte, name="Transporte"),
    path('comunicado', views.comunicado, name="Comunicado"),
    path('noticia', views.noticia, name="Noticia"),
    
    
]