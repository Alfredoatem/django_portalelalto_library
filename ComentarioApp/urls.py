from django.urls import path
from ComentarioApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.add, name = 'Add'),
    path('', views.add, name = 'Add'),
]