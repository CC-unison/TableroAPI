from django.contrib import admin
from Alumno.models import Alumno, models
# Register your models here.
class AlumnoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Alumno, AlumnoAdmin)