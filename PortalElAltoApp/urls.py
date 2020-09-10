from django.urls import path
from PortalElAltoApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('turismop/', views.turismop, name="TurismoP"),
    path('servicios/', views.servicios, name="Servicios"),
    path('<int:pk>/', views.SnippetDetailView.as_view(), name='detail'),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)