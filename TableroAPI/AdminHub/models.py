from django.db import models

# Create your models here.
class Admins(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=60, blank=False)
    correo = models.TextField(max_length=64, blank=False)
    passwd = models.TextField(max_length=20, blank=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre

class Sesiones_Admins(models.Model):
    id = models.AutoField(primary_key=True)
    id_admin = models.ForeignKey(Admins, on_delete=models.CASCADE)
    inicio_sesion = models.DateTimeField()
    cierre_sesion = models.DateTimeField()
    def __str__(self):
        return self.id_admin.nombre
