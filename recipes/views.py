from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from recipes.models import Recipes
from django.http import HttpResponse
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

def galeria(request):
    content=[]
    for recipe in recipes:
        content.append("""
            <p><strong>{title}</strong></p>
            <p><small>{description}</small></p>
        """.format(**post)
        )
        # return render(request, 'recipes/individual.html')
    return HttpResponse('<br>'.join(content))

def recetario(request):
    recipes = Recipes.objects.all()
    return render(request, 'recipes/recetario.html', {'recipes':recipes})

def individual(request):
    recipes = Recipes.objects.filter(id=6)
    return render(request, 'recipes/individual.html', {'recipes':recipes})

# def main(request):
#        i = get_object_or_404(images, pk=1)
#        return render_to_response('recipes/recetario.html', {'image': i}, context_instance=RequestContext(request))

# def list_posts(request):
#     """List existing posts."""
#     posts = Post.objects.all().order_by('-created')
#     return render(request, 'posts/feed.html', {'posts': posts}

# def recetario(request):

#     return render(request, 'recipes/recetario.html')
