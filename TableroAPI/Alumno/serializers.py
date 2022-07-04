from re import A
from rest_framework import serializers
from Alumno.models import Alumno

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('AlumnoId', 'AlumnoNombre')