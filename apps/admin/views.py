# Django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# App directorio
# --- forms
from apps.directorio.forms import fRegistroCategorias, fRegistroRepartidores, fRegistroDirectorio
# --- models
from apps.directorio.models import Categorias, Repartidores, Directorio

@login_required
def vPrincipalAdmin(request):
    return render(request, 'admin/principal.html')

@login_required
def vPrincipalCategorias(request):
    if request.method == 'POST':
        fcategoria = fRegistroCategorias(request.POST, request.FILES)
        if fcategoria.is_valid():
            fcategoria.save()
            messages.success(request, 'Registro guardado con éxito')
        else:
            print(fcategoria.errors)
            messages.error(request, 'El formulario es inválido. Intente de nuevo')
        return redirect('admin:pCategorias')
    else:
        fcategoria = fRegistroCategorias(label_suffix = '')
    categorias = Categorias.objects.filter(categoria__isnull = True)
    context = {'fcategoria': fcategoria, 'categorias': categorias, 'total_cat': Categorias.objects.count()}
    return render(request, 'admin/categorias/principal.html', context)

@login_required
def vPrincipalRepartidores(request):
    if request.method == 'POST':
        frepartidor = fRegistroRepartidores(request.POST, request.FILES)
        if frepartidor.is_valid():
            frepartidor.save()
            messages.success(request, 'Registro guardado con éxito')
        else:
            print(frepartidor.errors)
            messages.error(request, 'El formulario es inválido. Intente de nuevo')
        return redirect('admin:pRepartidores')
    else:
        frepartidor = fRegistroRepartidores(label_suffix = '')
    repartidores = Repartidores.objects.all()
    context = {'frepartidor': frepartidor, 'repartidores': repartidores}
    return render(request, 'admin/repartidores/principal.html', context)

@login_required
def vPrincipalDirectorio(request):
    if request.method == 'POST':
        fdirectorio = fRegistroDirectorio(request.POST, request.FILES)
        if fdirectorio.is_valid():
            fdirectorio.save()
            messages.success(request, 'Registro guardado con éxito')
        else:
            print(fdirectorio.errors)
            messages.error(request, 'El formulario es inválido. Intente de nuevo')
        return redirect('admin:pDirectorio')
    else:
        fdirectorio = fRegistroDirectorio(label_suffix = '')
    if request.GET.get('q', None):
        busqueda = request.GET.get('q', None)
        or_lookup = (Q(nombre__icontains = busqueda) | Q(telefono__icontains = busqueda))
        directorio = Directorio.objects.filter(or_lookup)
    else:
        busqueda = ''
        directorio = []
    context = {'fdirectorio': fdirectorio, 'directorio': directorio, 'q': busqueda, 'total_dir': Directorio.objects.count()}
    return render(request, 'admin/directorio/principal.html', context)

@login_required
def vEditarRepartidores(request, id):
    try:
        repartidor = Repartidores.objects.get(id = id)
        if request.method == 'POST':
            frepartidor = fRegistroRepartidores(request.POST, request.FILES, instance = repartidor)
            if frepartidor.has_changed():
                if frepartidor.is_valid():
                    frepartidor.save()
                    messages.success(request, 'Registro guardado con éxito')
                    return redirect('admin:eRepartidores', repartidor.id, permanent = True)
                else:
                    print(frepartidor.errors)
                    messages.error(request, 'El formulario es inválido. Intente de nuevo')
            else:
                messages.warning(request, 'No se detectó ningún cambio')
        else:
            frepartidor = fRegistroRepartidores(instance = repartidor)
        context = {'frepartidor': frepartidor}
        return render(request, 'admin/repartidores/editar.html', context)
    except Repartidores.DoesNotExist:
        return redirect('admin:pRepartidores')

@login_required
def vEditarDirectorio(request, id):
    try:
        directorio = Directorio.objects.get(id = id)
        if request.method == 'POST':
            fdirectorio = fRegistroDirectorio(request.POST, request.FILES, instance = directorio)
            if fdirectorio.has_changed():
                if fdirectorio.is_valid():
                    fdirectorio.save()
                    messages.success(request, 'Registro guardado con éxito')
                    return redirect('admin:eDirectorio', directorio.id)
                else:
                    print(fdirectorio.errors)
                    messages.error(request, 'El formulario es inválido. Intente de nuevo')
            else:
                messages.warning(request, 'No se detectó ningún cambio')
        else:
            fdirectorio = fRegistroDirectorio(instance = directorio)
        context = {'fdirectorio': fdirectorio}
        return render(request, 'admin/directorio/editar.html', context)
    except Directorio.DoesNotExist:
        return redirect('admin:pDirectorio')

@login_required
def vEliminarRepartidores(request, id):
    if request.method == 'POST':
        try:
            repartidor = Repartidores.objects.get(id = id)
            repartidor.delete()
            messages.success(request, 'Repartidor eliminado con éxito')
        except Repartidores.DoesNotExist:
            pass
        return redirect('admin:pRepartidores')
    return render(request, 'admin/repartidores/eliminar_confirm.html')