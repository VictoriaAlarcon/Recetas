from django.urls import path
from recipes import views
from django.conf.urls.static import static
from django.conf import settings

"""Urls de recetas"""
urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='agregar/', view=views.ingresar, name='agregar'),
    path(route='galeria/', view=views.galeria, name='galeria'),
    path(route='recetario/', view=views.recetario, name='recetario')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
