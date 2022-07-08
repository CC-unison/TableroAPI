from Tablero import views 
from django.urls import include, re_path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    re_path(r'^anuncio$', views.AnunciosApi),

    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
