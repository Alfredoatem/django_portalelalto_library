from django.db import models
from simple_history.models import HistoricalRecords
from ckeditor.fields import RichTextField
# Create your models here.

class Distrito(models.Model):
    id = models.AutoField(primary_key=True)
    distrito = models.CharField('Distrito', max_length=100, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Distrito'
        verbose_name_plural = 'Distritos'

    def __str__(self):
        return self.distrito

class Zona(models.Model):
    id = models.AutoField(primary_key=True)
    zona = models.CharField('Zona', max_length=100, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'

    def __str__(self):
        return self.zona

class UnidadEducativa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Título', max_length=90,blank=False, null=False)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='unidad')
    contenido = RichTextField('Contenido',null=True, blank=True)
    descripcion = models.CharField('Descripción', max_length=110, blank=False, null=False)
    direccion = models.CharField('Dirección', max_length=110, blank=False, null=False)
    telefono = models.IntegerField(null=True, blank=True)
    web = models.URLField('Página Web', null=True, blank=True)
    ubicacion = models.URLField('Página Web', null=True, blank=True)
    email = models.EmailField('Correo Electrónico', blank=False, null=False)
    estado = models.BooleanField('Publicado/No publicado', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'UnidadEducativa'
        verbose_name_plural = 'UnidadesEducativas'

    def __str__(self):
        return self.nombre

class Hoteles(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Título', max_length=90,blank=False, null=False)
    tipo = models.CharField('Tipo', max_length=110, blank=False, null=False)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='hoteles')
    contenido = RichTextField('Contenido',null=True, blank=True)
    direccion = models.CharField('Dirección', max_length=110, blank=False, null=False)
    telefono = models.IntegerField(null=True, blank=True)
    web = models.URLField('Página Web', null=True, blank=True)
    ubicacion = models.URLField('Ubicación', null=True, blank=True)
    email = models.EmailField('Correo Electrónico', blank=False, null=False)
    estado = models.BooleanField('Publicado/No publicado', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hoteles'

    def __str__(self):
        return self.nombre

class Restaurant(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Título', max_length=90,blank=False, null=False)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='restaurantes')
    contenido = RichTextField('Contenido',null=True, blank=True)
    horario = models.CharField('Horario', max_length=110, blank=False, null=False)
    direccion = models.CharField('Dirección', max_length=110, blank=False, null=False)
    telefono = models.IntegerField(null=True, blank=True)
    web = models.URLField('Página Web', null=True, blank=True)
    ubicacion = models.URLField('Ubicación', null=True, blank=True)
    email = models.EmailField('Correo Electrónico', blank=False, null=False)
    estado = models.BooleanField('Publicado/No publicado', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurantes'

    def __str__(self):
        return self.nombre

class Empresa(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Título', max_length=90,blank=False, null=False)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='empresas')
    contenido = RichTextField('Contenido',null=True, blank=True)
    direccion = models.CharField('Dirección', max_length=110, blank=False, null=False)
    telefono = models.IntegerField(null=True, blank=True)
    web = models.URLField('Página Web', null=True, blank=True)
    ubicacion = models.URLField('Ubicación', null=True, blank=True)
    email = models.EmailField('Correo Electrónico', blank=False, null=False)
    estado = models.BooleanField('Publicado/No publicado', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre

class Hospital(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Título', max_length=90,blank=False, null=False)
    tipo = models.CharField('Tipo', max_length=110, blank=False, null=False)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='empresas')
    contenido = RichTextField('Contenido',null=True, blank=True)
    direccion = models.CharField('Dirección', max_length=110, blank=False, null=False)
    telefono = models.IntegerField(null=True, blank=True)
    web = models.URLField('Página Web', null=True, blank=True)
    ubicacion = models.URLField('Ubicación', null=True, blank=True)
    email = models.EmailField('Correo Electrónico', blank=False, null=False)
    estado = models.BooleanField('Publicado/No publicado', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitales'

    def __str__(self):
        return self.nombre
    
class Transporte(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Título', max_length=90,blank=False, null=False)
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
    tipo = models.CharField('Tipo', max_length=110, blank=False, null=False)
    imagen = models.ImageField(upload_to='empresas')
    sindicato = models.CharField('Título', max_length=90,blank=False, null=False)
    contenido = RichTextField('Contenido')
    linea = models.CharField('Tipo', max_length=110, blank=False, null=False)
    direccion = models.CharField('Dirección', max_length=110, blank=False, null=False)
    telefono = models.IntegerField(null=True, blank=True)
    web = models.URLField('Página Web', null=True, blank=True)
    email = models.EmailField('Correo Electrónico', blank=False, null=False)
    estado = models.BooleanField('Publicado/No publicado', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Transporte'
        verbose_name_plural = 'Transportes'

    def __str__(self):
        return self.nombre

class Comunicado(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Título', max_length=90,blank=False, null=False)
    imagen = models.ImageField(upload_to='empresas')
    estado = models.BooleanField('Publicado/No publicado', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Comunicado'
        verbose_name_plural = 'Comunicado'

    def __str__(self):
        return self.nombre

class Noticia(models.Model): 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Título', max_length=90,blank=False, null=False)
    imagen = models.ImageField(upload_to='empresas')
    web = models.URLField('Página Web', null=True, blank=True)
    estado = models.BooleanField('Publicado/No publicado', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()
    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticia'

    def __str__(self):
        return self.nombre