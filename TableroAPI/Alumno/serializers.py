from re import A
from rest_framework import serializers
from Alumno.models import Alumnos

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = (
            'id',
            'nombre_programa',
            'clave_programa',
            'plan', 
            'expediente', 
            'nombre',
            'status',
            'cred_pasante',
            'cred_aprob',
            'prom_kdxs',
            'prom_periodo',
            'mat_aprob',
            'materias_acreditadas',
            'materias_inscritas',
            'materias_segunda_inscr',
            'materias_tercera_inscr',
            'materias_reprobadas',
            'materias_bajas_voluntarias',
            'cred_inscr',
            'nivel_y_ciclo_ingles',
            'correo',
            'cred_cult',
            'cred_dep',
            'practica_profesional_estatus_y_ciclo',
            'serviciosocialmateriaestatus_ciclo',
            'estatusproyectoserviciosocial_cicloregistro',
            'egel_testimonio',
            'inscrito'
            )