from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    contenido = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.nombre
