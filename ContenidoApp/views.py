from django.shortcuts import render
from ContenidoApp.models import Cultura, Historia, Manifestacione, Museo, MuseoCont, AreaVerde, Iglesia, Ballet, Festival
# Create your views here.


def cultura(request):

    ContenidoApp = Cultura.objects.all()
    return render(request, "ContenidoApp/cultura.html", {"ContenidoApp": ContenidoApp})


def historia(request):

    ContenidoApp = Historia.objects.all()
    return render(request, "ContenidoApp/historia.html", {"ContenidoApp": ContenidoApp})

def manifestaciones(request):

    ContenidoApp = Manifestacione.objects.all()
    return render(request, "ContenidoApp/manifestaciones.html", {"ContenidoApp": ContenidoApp})

def museo(request):

    ContenidoApp = Museo.objects.all()
    return render(request, "ContenidoApp/museo.html", {"ContenidoApp": ContenidoApp})

def museocont(request):

    ContenidoApp = MuseoCont.objects.all()
    return render(request, "ContenidoApp/museocont.html", {"ContenidoApp": ContenidoApp})

def areasverdes(request):

    ContenidoApp = AreaVerde.objects.all()
    return render(request, "ContenidoApp/areasverdes.html", {"ContenidoApp": ContenidoApp})

def iglesia(request):

    ContenidoApp = Iglesia.objects.all()
    return render(request, "ContenidoApp/iglesia.html", {"ContenidoApp": ContenidoApp})

def ballet(request):

    ContenidoApp = Ballet.objects.all()
    return render(request, "ContenidoApp/ballet.html", {"ContenidoApp": ContenidoApp})

def festival(request):

    ContenidoApp = Festival.objects.all()
    return render(request, "ContenidoApp/festival.html", {"ContenidoApp": ContenidoApp})