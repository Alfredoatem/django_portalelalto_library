from django import forms
#from django.forms import ModelForm
from .models import Comentario


class ComentarioForm(forms.Form):
    nombre = forms.CharField()
    contenido = forms.CharField()
    #class Meta:
     #   model = Comentario
      #  fields = ['nombre', 'contenido']