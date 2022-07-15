from django.db import models
from AdminHub.models import Admins

class Publicaciones_Admins(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField(max_length=100, blank=False, default= 'Publicacion')
    #----------------------------------------------------------------------
    class Tipos(models.TextChoices):
        NOT = '1', "NOTICIA"
        LAB = '2', "LABORAL"
        VID = '3', "VIDEO"
    tipo = models.CharField(
        max_length=3, choices=Tipos.choices, default=Tipos.NOT)
    #----------------------------------------------------------------------
    id_admin = models.ForeignKey(Admins, to_field='id', on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField(null=True, blank=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.titulo

class Publicaciones_Noticias(models.Model):
    id = models.AutoField(primary_key=True)
    id_publicacion = models.ForeignKey(Publicaciones_Admins, to_field='id', on_delete=models.CASCADE, null=True)
    titulo = models.TextField(max_length=100, blank=False, default= 'Publicacion')
    subtitulo = models.TextField(max_length=100, blank=False, default= 'Subtitulo')
    #----------------------------------------------------------------------
    class Tipos(models.TextChoices):
        ANU = '1', "ANUNCIO"
        AVI = '2', "AVISO"
    tipo = models.CharField(
        max_length=3, choices=Tipos.choices, default=Tipos.ANU)
    #----------------------------------------------------------------------
    descripcion = models.TextField(max_length=500, blank=True)
    tags = models.TextField(max_length=100, blank=True)
    ruta_img = models.TextField(max_length=100, blank=True)
    referencias = models.TextField(max_length=100, blank=True)
    hipervinculo = models.TextField(max_length=100, blank=True)
    def __str__(self):
        return self.titulo