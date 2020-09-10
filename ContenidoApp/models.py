from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.
class Festival(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='festival')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.titulo

class FestivalCont(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=700)
    director1 = models.CharField(max_length=50)
    director2 = models.CharField(max_length=50)
    imagen1 = models.ImageField(upload_to='festival')
    imagen2 = models.ImageField(upload_to='festival')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.titulo

class Gastronomia(models.Model):
    restaurant = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    contenido = models.CharField(max_length=700)
    precio = models.CharField(max_length=10)
    lugar = models.CharField(max_length=50)
    telefono = models.IntegerField()
    imagen = models.ImageField(upload_to='gastronomia')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class AreaVerde(models.Model):
    nombre = models.CharField(max_length=50)
    lugar = models.CharField(max_length=700)
    imagen = models.ImageField(upload_to='areasverdes')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class Cultura(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=350)
    imagen = models.ImageField(upload_to='cultura')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class Museo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=350)
    imagen = models.ImageField(upload_to='museo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class MuseoCont(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=350)
    tipo = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='museo')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class Ballet(models.Model):
    nombre = models.CharField(max_length=30)
    imagen = models.FileField(upload_to='ballet')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()
class ArtesPlast(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.CharField(max_length=750)
    imagen = models.ImageField(upload_to='artes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='artes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.CharField(max_length=750)
    imagen = models.ImageField(upload_to='tecnologia')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class TecnologiaCont(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=350)
    imagen = models.ImageField(upload_to='tecnologia')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class Arquitectura(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.CharField(max_length=750)
    imagen = models.ImageField(upload_to='arquitectura')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class ArquitecturaCont(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=350)
    imagen = models.ImageField(upload_to='arquitectura')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class WhipalaCont(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=350)
    imagen = models.ImageField(upload_to='arquitectura')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class Iglesia(models.Model):
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=350)
    imagen = models.ImageField(upload_to='iglesia')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class Historia(models.Model):
    titulo = models.CharField(max_length=50)
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=70)
    contenido = models.CharField(max_length=5000)
    imagen1 = models.ImageField(upload_to='historia')
    imagen2 = models.ImageField(upload_to='historia')
    imagen3 = models.ImageField(upload_to='historia')
    imagen4 = models.ImageField(upload_to='historia')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

class Manifestacione(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=700)
    imagen1 = models.ImageField(upload_to='manifestaciones')
    imagen2 = models.ImageField(upload_to='manifestaciones')
    audio1 = models.FileField(upload_to='manifestaciones')
    traducido = models.CharField(max_length=700)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()