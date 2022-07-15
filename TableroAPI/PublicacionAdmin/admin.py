from django.contrib import admin
from PublicacionAdmin.models import Publicaciones_Admins

# Register your models here.

class PublicacionAdminAdmin(admin.ModelAdmin):
    pass
admin.site.register(Publicaciones_Admins, PublicacionAdminAdmin)