from django.db import models
from django.forms import FloatField

# Create your models here.

class Alumnos(models.Model):
   expediente = models.IntegerField(primary_key=True)
   nombre_programa = models.TextField(max_length=60, null=False, blank=False)
   clave_programa = models.IntegerField(null=False, blank=False)
   nombre = models.TextField(max_length=60, null=False, blank=False)
   status = models.TextField(max_length=20, null=False, blank=False)
   cred_pasante = models.IntegerField(null=False, blank=False)
   cred_aprob_ = models.IntegerField(null=False, blank=False)
   prom_kdxs = models.FloatField(null=False, blank=False)
   prom_periodo = models.FloatField(null=False, blank=False)
   mat_aprob_ = models.IntegerField(null=False, blank=False)
   materias_acreditadas = models.TextField(max_length=255, null=False, blank=True)
   materias_segunda_inscr = models.TextField(max_length=255, null=False, blank=True)
   materias_tercera_inscr = models.TextField(max_length=255, null=False, blank=True)
   materias_reprobadas = models.TextField(max_length=255, null=False, blank=True)
   materias_bajas_voluntarias = models.TextField(max_length=255, null=False, blank=True)
   cred_inscr = models.IntegerField(null=False, blank=False)
   nivel_y_ciclo_ingles = models.TextField(max_length=10, null=False, blank=False)
   correo = models.TextField(max_length=25, null=False, blank=False) 
   cred_cult = models.FloatField(null=False, blank=False)
   cred_dep = models.FloatField(null=False, blank=False)
   practica_profesional_estatus_y_ciclo = models.TextField(max_length=20, null=False, blank=True)
   serviciosocialmateriaestatus_ciclo = models.TextField(max_length=20, null=False, blank=True)
   estatusproyectoserviciosocial_cicloregistro = models.TextField(max_length=20, null=False, blank=True)
   egel_testimonio = models.TextField(max_length=60, null=False, blank=True)
   inscrito = models.BooleanField(null=False, blank=False)


   
   
   