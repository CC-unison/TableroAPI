from django.db import models

# Create your models here.

class Alumno(models.Model):
   AlumnoId = models.AutoField(primary_key=True)
   AlumnoNombre = models.TextField(blank=False)
   
   
   