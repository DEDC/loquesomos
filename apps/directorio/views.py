# Django
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# App directorio
# --- models
from apps.directorio.models import Categorias, Directorio
# --- forms
from apps.directorio.forms import fMunicipios

def vHome(request):
    categorias = Categorias.objects.filter(categoria__isnull = True)
    fmunicipios = fMunicipios()
    context = {'categorias': categorias, 'fmunicipios': fmunicipios}
    return render(request, 'directorio/home.html', context)

def vSearch(request):
    if request.is_ajax():
        category = request.GET.get('cat', None)
        page = request.GET.get('page', None)
        name = request.GET.get('name', None)
        fmunicipios = fMunicipios(request.GET)
        if fmunicipios.is_valid():
            if name is not None:
                results = Directorio.objects.filter(nombre__icontains = name, municipio = fmunicipios.cleaned_data['municipios'])
            elif category is not None:
                results = Directorio.objects.filter(categoria__codename = category, municipio = fmunicipios.cleaned_data['municipios'])
            data = []
            for row in results:
                data.append({
                    'name': row.nombre,
                    'phonenumber': row.telefono,
                    'facebook_url': row.facebook_url,
                    'instagram_url': row.instagram_url,
                    'web_url': row.web_page,
                    'logo': row.logo.url,
                    'municipality': row.get_town(),
                    'own_service': row.serv_dom,
                    'dealers': [{'name': dealer.nombre, 'logo': dealer.logo.url, 'app_url': dealer.app_url, 'phonenumber': dealer.telefono} for dealer in row.repartidores.all()]
                })
            return JsonResponse(data, safe = False)
    return HttpResponse('No fue posible completar la búsqueda')