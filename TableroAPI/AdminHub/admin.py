from django.contrib import admin
from AdminHub.models import Admins, Sesiones_Admins

# Register your models here.
class AdminHubAdmin(admin.ModelAdmin):
    pass
admin.site.register(Admins, AdminHubAdmin)

class SesionesAdminHubAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sesiones_Admins, SesionesAdminHubAdmin)