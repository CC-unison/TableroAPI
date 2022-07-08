from re import A
from rest_framework import serializers
from Tablero.models import *

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = ('AnuncioId')

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = ('MateriaId')

class PlanEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanEstudio
        fields = ('PlanEstudioId')

class ServicioSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioSocial
        fields = ('ServicioSocialId')

class PracticasProfesionalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticasProfesionales
        fields = ('PracticasProfesionalesId')