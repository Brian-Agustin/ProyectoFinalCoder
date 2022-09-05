from django.shortcuts import render, redirect
from AppLente.models import Contacto
from django.http import HttpResponse
from AppLente.forms import Contactoformulario
from datetime import datetime


def inicio(request):
    return render(request, 'index.html')

def turnos(request):
    return render(request, 'AppLente/turnos.html')

def recetas(request):
    return render(request, 'AppLente/recetas.html')

def contacto(request):


    if request.method == 'POST':
        mi_formulario = Contactoformulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            contacto1 = Contacto(nombre=data.get('nombre'), numero=data.get('numero'), correo=data.get('correo'), mensaje=data.get('mensaje'))
            contacto1.save()

            return redirect('contacto')

    contactos = Contacto.objects.all()

    contexto = {
        'form': Contactoformulario(),
        'contactos': contactos
    }

    return render(request, 'AppLente/contacto.html', contexto)

def reportes(request):
    return render(request, 'AppLente/reportes.html')

