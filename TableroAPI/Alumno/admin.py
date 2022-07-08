from django.contrib import admin
from Alumno.models import Alumnos, models
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AlumnoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
admin.site.register(Alumnos, AlumnoAdmin)