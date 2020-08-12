from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from recipes.models import Recipes
from django.views.generic import View
from django.conf.urls.static import static
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
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


class createPdf(View):
    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
            if not isinstance(result, (list, tuple)):
                result = [result]
            result = list(os.path.realpath(path) for path in result)
            path = result[0]
        else:
            sUrl = settings.STATIC_URL        # Typically /static/
            sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
            mUrl = settings.MEDIA_URL         # Typically /media/
            mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

            if uri.startswith(mUrl):
                path = os.path.join(mRoot, uri.replace(mUrl, ""))
            elif uri.startswith(sUrl):
                path = os.path.join(sRoot, uri.replace(sUrl, ""))
            else:
                return uri

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('recipes/list.html')
            context = {
                'recipes': Recipes.objects.filter(id=self.kwargs['Id']),
                'image': '{}{}'.format(settings.STATIC_URL, 'images/aprenderRecetas.png')
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
