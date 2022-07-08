from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Tablero.models import *
from Tablero.serializers import *

# Create your views here.


@csrf_exempt
def AnunciosApi(request):
    if request.method == 'GET':
        anuncios = Anuncio.objects.all()
        anuncios_serializer = AnuncioSerializer(anuncios, many=True)
        return JsonResponse(anuncios_serializer.data, safe=False)
    elif request.method == 'POST':
        anuncios_data = JSONParser().parse(request)
        anuncios_serializer = AnuncioSerializer(data=anuncios_data)
        if anuncios_serializer.is_valid():
            anuncios_serializer.save()
            return JsonResponse("Añadido correctamente", safe=False)


@csrf_exempt
def MateriaApi(request):
    if request.method == 'GET':
        materias = Materia.objects.all()
        materias_serializer = MateriaSerializer(materias, many=True)
        return JsonResponse(materias_serializer.data, safe=False)
    elif request.method == 'POST':
        materias_data = JSONParser().parse(request)
        materias_serializer = MateriaSerializer(data=materias_data)
        if materias_serializer.is_valid():
            materias_serializer.save()
            return JsonResponse("Añadido correctamente", safe=False)


@csrf_exempt
def PlanEstudioApi(request):
    if request.method == 'GET':
        plan_estudios = PlanEstudio.objects.all()
        plan_estudios_serializer = PlanEstudioSerializer(plan_estudios, many=True)
        return JsonResponse(plan_estudios_serializer.data, safe=False)
    elif request.method == 'POST':
        plan_estudios_data = JSONParser().parse(request)
        plan_estudios_serializer = PlanEstudioSerializer(data=plan_estudios_data)
        if plan_estudios_serializer.is_valid():
            plan_estudios_serializer.save()
            return JsonResponse("Añadido correctamente", safe=False)


@csrf_exempt
def ServicioSocialApi(request):
    if request.method == 'GET':
        serviciosocial = ServicioSocial.objects.all()
        serviciosocial_serializer = ServicioSocialSerializer(serviciosocial, many=True)
        return JsonResponse(serviciosocial_serializer.data, safe=False)
    elif request.method == 'POST':
        serviciosocial_data = JSONParser().parse(request)
        serviciosocial_serializer = ServicioSocialSerializer(data=serviciosocial_data)
        if serviciosocial_serializer.is_valid():
            serviciosocial_serializer.save()
            return JsonResponse("Añadido correctamente", safe=False)


@csrf_exempt
def ServicioSocialApi(request):
    if request.method == 'GET':
        practicas_profesionales = PracticasProfesionales.objects.all()
        practicas_profesionales_serializer = PracticasProfesionalesSerializer(practicas_profesionales, many=True)
        return JsonResponse(practicas_profesionales_serializer.data, safe=False)
    elif request.method == 'POST':
        practicas_profesionales_data = JSONParser().parse(request)
        practicas_profesionales_serializer = PracticasProfesionalesSerializer(data=practicas_profesionales_data)
        if practicas_profesionales_serializer.is_valid():
            practicas_profesionales_serializer.save()
            return JsonResponse("Añadido correctamente", safe=False)
