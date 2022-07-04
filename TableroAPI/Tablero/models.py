from django.db import models

# Create your models here.


class Anuncio(models.Model):
    AnuncioId = models.AutoField(primary_key=True)

class Materia(models.Model):
    MateriaId = models.AutoField(primary_key=True)

class PlanEstudio(models.Model):
    PlanEstudioId = models.AutoField(primary_key=True)

class ServicioSocial(models.Model):
    ServicioSocialId = models.AutoField(primary_key=True)

class PracticasProfesionales(models.Model):
    PracticasProfesionalesId = models.AutoField(primary_key=True)
