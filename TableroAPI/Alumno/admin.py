from django.contrib import admin
from Alumno.models import Alumnos, models
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

class AlumnoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass
admin.site.register(Alumnos, AlumnoAdmin)

class AlumnoResource(resources.ModelResource):
    class Meta:
        model = Alumnos
    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        dataset.export('csv')
        template_headers = [h for h in dataset.headers]
        for col in template_headers:
            dataset.headers[col] = col.str.replace(' ','_')
            dataset.headers[col] = col.str.replace('.','_')
            dataset.headers[col] = col.str.replace('-','_')
            dataset.headers[col] = col.str.lower()
            print(dataset.headers[col])
        dataset.headers["NIVEL_Y_CICLO_INGLÉS"] = "NIVEL_Y_CICLO_INGLES"
        dataset.headers["CRED_APROB_"] = "CRED_APROB"
        dataset.headers["MAT_APROB_"] = "MAT_APROB"
        dataset.headers.insert(0,"ID")
        return super().before_import(dataset, using_transactions, dry_run, **kwargs)