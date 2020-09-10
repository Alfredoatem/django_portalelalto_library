from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.
class Turismo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=700)
    imagen1 = models.ImageField(upload_to='turismo')
    imagen2 = models.ImageField(upload_to='turismo')
    audio1 = models.FileField(upload_to='turismo')
    traducido = models.CharField(max_length=700)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'turismo'
        verbose_name_plural = 'turismos'

    def __str__(self):
        return self.titulo



