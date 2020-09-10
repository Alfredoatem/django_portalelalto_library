from django.shortcuts import render
from ServiciosApp.models import Distrito, Zona, UnidadEducativa,Hoteles, Restaurant,Empresa,Hospital,Transporte, Comunicado, Noticia
# Create your views here.

def distrito(request):
    ServiciosApp = Distrito.objects.all()
    return render(request, "ServiciosApp/distrito.html", {"ServiciosApp": ServiciosApp})

def zona(request):
    ServiciosApp = Zona.objects.all()
    return render(request, "ServiciosApp/zona.html", {"ServiciosApp": ServiciosApp})

def unidadeducativa(request):
    ServiciosApp = UnidadEducativa.objects.all()
    return render(request, "ServiciosApp/unidadeducativa.html", {"ServiciosApp": ServiciosApp})

def hoteles(request):
    ServiciosApp = Hoteles.objects.all()
    return render(request, "ServiciosApp/hoteles.html", {"ServiciosApp": ServiciosApp})

def restaurant(request):
    ServiciosApp = Restaurant.objects.all()
    return render(request, "ServiciosApp/restaurant.html", {"ServiciosApp": ServiciosApp})

def empresa(request):
    ServiciosApp = Empresa.objects.all()
    return render(request, "ServiciosApp/empresa.html", {"ServiciosApp": ServiciosApp})

def hospital(request):
    ServiciosApp = Hospital.objects.all()
    return render(request, "ServiciosApp/hospital.html", {"ServiciosApp": ServiciosApp})

def transporte(request):
    ServiciosApp = Transporte.objects.all()
    return render(request, "ServiciosApp/transporte.html", {"ServiciosApp": ServiciosApp})

def comunicado(request):
    ServiciosApp = Comunicado.objects.all()
    return render(request, "ServiciosApp/comunicado.html", {"ServiciosApp": ServiciosApp})

def noticia(request):
    ServiciosApp = Noticia.objects.all()
    return render(request, "ServiciosApp/noticia.html", {"ServiciosApp": ServiciosApp})