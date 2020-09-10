from django.shortcuts import render, redirect
from ComentarioApp.models import Comentario
from ComentarioApp.forms import ComentarioForm
# Create your views here.


def add(request):
    #form = ComentarioForm()

    # if request.method == "POST":
    #   form = ComentarioForm(request.POST)
    #   if form.is_valid():
    #       instancia = form.save(commit=False)
    #       instancia.save()
    #       return redirect('/')

    # return render(request, "ComentarioApp/add.html", {'form': form})
    if request.method == "POST":
      miComentario=ComentarioForm(request.POST)
      if miComentario.is_valid():
        miComentario=ComentarioForm()
      
    return render(request, "ComentarioApp/formulariocomentario.html", {"form":miComentario})


        # return render(request, "ComentarioApp/gracias.html")
       # return render(request, "ComentarioApp/add.html")
