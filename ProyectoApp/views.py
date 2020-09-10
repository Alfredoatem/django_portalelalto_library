from django.shortcuts import render
from ProyectoApp.models import Proyecto
# Create your views here.
def proyecto(request):

    ProyectoApp = Proyecto.objects.all()
    return render(request, "ProyectoApp/proyecto.html", {"ProyectoApp": ProyectoApp})