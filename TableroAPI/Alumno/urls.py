from Alumno import views
from django.urls import include, re_path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    re_path(r'^alumno$', views.AlumnoApi),
    re_path(r'^alumno/([0-9]+)$',views.AlumnoApi),

    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
