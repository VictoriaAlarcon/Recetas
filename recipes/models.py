from django.db import models

# Create your models here.

"""Añade modelo de perfil"""


class Recipes(models.Model):
    title = models.CharField('titulo', max_length=50)
    description = models.CharField('descripcion', max_length=100)
    ingredients = models.TextField('ingrefientes',  max_length=200)
    process = models.TextField('procedimiento', max_length=400)
    images = models.ImageField(upload_to='recipes/images')
    puntuation = models.CharField('puntaje', max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)