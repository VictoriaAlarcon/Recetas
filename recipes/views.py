from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from recipes.models import Recipes
from django.views.generic import View
from django.http import HttpResponse
import xhtml2pdf.pisa as pisa

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template

from .utils import render_to_pdf

# decorador

"""Te redirige si estas logueado"""


@login_required
def index(request):
    return render(request, 'recipes/home.html')


"""Añade nueva recetas"""


def ingresar(request):
    """Verica si es post"""
    if request.method == 'POST':
        title = request.POST['input_title']
        description = request.POST['input_description']
        ingredients = request.POST['input_ingredients']
        process = request.POST['input_proces']
        images = request.FILES['file_images']
        puntuation = request.POST['input_puntuation']

        recipe = Recipes.objects.create(
            title=title, description=description)
        recipe.ingredients = ingredients
        recipe.process = process
        recipe.images = images
        recipe.puntuation = puntuation
        recipe.save()
        return redirect('recipes:index')

    """renderiza la vista aunque no sea post"""
    return render(request, 'recipes/recetas.html')


def recetario(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipes/recetario.html', {'recipes': recipes})


def individual(request, numId):
    recipes = Recipes.objects.filter(id=numId)
    return render(request, 'recipes/individual.html', {'recipes': recipes})

def generatePdf(View):
    model = Recipes
    template_name= "recipes/individual.html"
    context_object_name = 'recipes'

def List_recipes(View):

    def get(self, request, *args, **kwargs):
        recipes = recipes.objects.all()
        data = {
            'title':title
        }
        pdf=render_to_pdf('recipes/list.html', data)
        return HttpResponse(pdf, content_type='aplication/pdf')
