from re import A
from rest_framework import serializers
from AdminHub.models import Admins, Sesiones_Admins

class AdminHubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = (
            'id',
            'nombre',
            'correo',
            'passwd', 
            'fecha_creacion'
        )

class SesionesAdminHubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sesiones_Admins
        fields = (
            'id',
            'id_admin',
            'inicio_sesion',
            'cierre_sesion', 
            'fecha_creacion'
        )