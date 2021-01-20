# Django
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# --- App Usuario
# --- forms
from .forms import fLogin

def vLogin(request):
    if request.user.is_authenticated:
	    return redirect('logout')
    if request.method == 'POST': 
        flogin = fLogin(request.POST)
        if flogin.is_valid():
            username = flogin.cleaned_data['username']
            password = flogin.cleaned_data['password']
            autenticar = authenticate(username = username, password = password)
            if autenticar is not None:
                login(request, autenticar)
                if request.user.is_superuser or request.user.is_staff:
                    return redirect('admin:pAdmin')
            else:
                messages.error(request, 'Usuario y/o contraseña no válidos')
            return redirect('login')
            print(flogin.errors)
    else:
        flogin = fLogin()
    context = {'flogin': flogin}
    return render(request, 'base/login.html', context)

def vLogout(request):
    logout(request)
    return redirect('login')