from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

   path('cultura', views.cultura, name="Cultura"),
   path('historia', views.historia, name="Historia"),
   path('museo', views.museo, name="Museo"),
   path('museocont', views.museocont, name="MuseoCont"),
   path('manifestaciones', views.manifestaciones, name="Manifestacione"),
   path('areasverdes', views.areasverdes, name = "AreasVerdes"),
   path('iglesia', views.iglesia, name="Iglesia"),
   path('ballet', views.ballet, name="Ballet"),
   path('festival', views.festival, name="Festival"),
    
]