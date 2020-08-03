from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from recipes.models import Recipes
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

    return render(request, 'recipes/recetario.html')
