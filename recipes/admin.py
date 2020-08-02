from django.contrib import admin
from recipes.models import Recipes
# Register your models here.
# admin.site.register(Recipes)

"""Añade vista al admin"""


@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'images', 'puntuation')
    list_display_links = ('pk', 'images')
    list_editable = ('title', 'puntuation')
    list_filter = ('created', 'modified')
