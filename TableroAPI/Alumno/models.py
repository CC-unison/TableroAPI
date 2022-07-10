from django.db import models
from django.forms import FloatField

# Create your models here.

class Alumnos(models.Model):
   id = models.IntegerField(primary_key=True, auto_created=True)
   nombre_programa = models.TextField(max_length=60, null=False, blank=False)
   clave_programa = models.IntegerField(null=True, blank=False)
   plan = models.IntegerField(null=True, blank=False)
   expediente = models.IntegerField(null=True, blank=False)
   nombre = models.TextField(max_length=60, null=False, blank=False)
   status = models.TextField(max_length=20, null=False, blank=False)
   cred_pasante = models.IntegerField(null=True, blank=False)
   cred_aprob = models.IntegerField(null=True, blank=False)
   prom_kdxs = models.FloatField(null=True, blank=False)
   prom_periodo = models.FloatField(null=True, blank=False)
   mat_aprob = models.IntegerField(null=True, blank=False)
   materias_acreditadas = models.TextField(max_length=255, null=False, blank=True)
   materias_inscritas = models.TextField(max_length=255, null=False, blank=True)
   materias_segunda_inscr = models.TextField(max_length=255, null=True, blank=True)
   materias_tercera_inscr = models.TextField(max_length=255, null=True, blank=True)
   materias_reprobadas = models.TextField(max_length=255, null=True, blank=True)
   materias_bajas_voluntarias = models.TextField(max_length=255, null=True, blank=True)
   cred_inscr = models.IntegerField(null=True, blank=False)
   nivel_y_ciclo_ingles = models.TextField(max_length=10, null=False, blank=False)
   correo = models.TextField(max_length=25, null=False, blank=False) 
   cred_cult = models.FloatField(null=True, blank=False)
   cred_dep = models.FloatField(null=True, blank=False)
   practica_profesional_estatus_y_ciclo = models.TextField(max_length=20, null=True, blank=True)
   serviciosocialmateriaestatus_ciclo = models.TextField(max_length=20, null=True, blank=True)
   estatusproyectoserviciosocial_cicloregistro = models.TextField(max_length=20, null=True, blank=True)
   egel_testimonio = models.TextField(max_length=60, null=True, blank=True)
   inscrito = models.TextField(max_length=5, null=True, blank=False)


   
   
   