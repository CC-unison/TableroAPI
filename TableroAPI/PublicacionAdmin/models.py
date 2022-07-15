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
    id_admin = models.ForeignKey(Admins, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField(null=True, blank=True)
    fecha_finalizacion = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.titulo
