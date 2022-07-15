from django.contrib import admin
from PublicacionAdmin.models import Publicaciones_Admins, Publicaciones_Noticias

# Register your models here.

class PublicacionAdminAdmin(admin.ModelAdmin):
    pass
admin.site.register(Publicaciones_Admins, PublicacionAdminAdmin)

class PublicacionNoticiaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Publicaciones_Noticias, PublicacionNoticiaAdmin)