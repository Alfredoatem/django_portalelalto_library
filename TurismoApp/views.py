from django.shortcuts import render
from TurismoApp.models import Turismo
from ContenidoApp.models import Cultura
from django.shortcuts import get_object_or_404
# Create your views here.
def turismo(request):

    TurismoApp = Turismo.objects.all()
    return render(request, "TurismoApp/turismo.html", {"TurismoApp": TurismoApp})