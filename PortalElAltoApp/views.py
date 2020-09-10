from django.shortcuts import render, HttpResponse, get_object_or_404

from django.http import HttpResponse
from django.urls import reverse
from .models import Snippet, PageView
from ContenidoApp.models import Historia
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.
def home(request):
    if(PageView.objects.count()<=0):
        x=PageView.objects.create()
        x.save()
    else:
        x=PageView.objects.all()[0]
        x.hits=x.hits+1
        x.save()
    context={'page':x.hits}
    return render(request, "PortalElAltoApp/home.html",context=context)

def turismop(request):
    return render(request, "PortalElAltoApp/turismop.html")

def servicios(request):
    return render(request, "PortalElAltoApp/servicios.html")

class SnippetListView(ListView):
    model = Snippet
    template_name = 'snippets/snippet_list.html'


class SnippetDetailView(DetailView):
    model = Snippet
    template_name = 'snippets/snippet_detail.html'


