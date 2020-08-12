from django.urls import path
from recipes import views
from django.conf.urls.static import static
from django.conf import settings

# from .views import generatePdf

"""Urls de recetas"""
urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='agregar/', view=views.ingresar, name='agregar'),
    path(route='recetario/', view=views.recetario, name='recetario'),
    path(route='recetario/individual/<int:numId>/',
         view=views.individual, name='individual'),
    path(route='recetario/pdf/<int:Id>/',
         view=views.createPdf.as_view(), name='pdf'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
