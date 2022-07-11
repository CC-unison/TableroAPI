from django.contrib import admin
from Alumno.models import Alumnos, models
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from import_export.formats.base_formats import TablibFormat
from importlib import import_module
from Alumno.resources import AlumnoResource

import tablib
# Register your models here.

class AlumnoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Se indica que resource class utilizara el ImportExport Admin
    resource_class = AlumnoResource
    pass
admin.site.register(Alumnos, AlumnoAdmin)