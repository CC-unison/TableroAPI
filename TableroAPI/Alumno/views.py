from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Alumno.models import Alumno
from Alumno.serializers import AlumnoSerializer

#Obtener lista de alumnos (CON SECRET KEY).

@csrf_exempt
def AlumnoApi(request,id=0):
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        alumnos_serializer = AlumnoSerializer(alumnos, many=True)
        return JsonResponse(alumnos_serializer.data, safe=False)
    elif request.method =='POST':
        alumnos_data = JSONParser().parse(request)
        alumnos_serializer = AlumnoSerializer(data=alumnos_data)
        if alumnos_serializer.is_valid():
            alumnos_serializer.save()
            return JsonResponse("Añadido correctamente", safe=False)
        # elif request.method=='PUT':
        #     alumno_data = JSONParser().parse(request)
        #     alumno = Alumno.objects.get(AlumnoId=alumno_data['AlumnoId'])
        #     alumnos_serializer = AlumnoSerializer(alumno, data = alumno_data)
        #     if alumnos_serializer.is_valid():
        #         alumnos_serializer.save()
        #         return JsonResponse("Actualizado correctamente", safe=False)
        #     return JsonResponse("Error al actualizar", safe=False)
        # elif request.method=='DELETE':
        #     alumno = Alumno.objects.get(AlumnoId=id)
        #     alumno.delete()
        #     return JsonResponse("Eliminado correctamente", safe=False)
            