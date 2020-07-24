from django.urls import path
from recipes import views

urlpatterns = [
    path(route='', view=views.index, name='index')
]