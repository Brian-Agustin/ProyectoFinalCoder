from django.shortcuts import render, redirect
from AppLente.models import Contacto
from django.http import HttpResponse
from AppLente.forms import Contactoformulario


def inicio(request):
    return render(request, 'index.html')

def turnos(request):
    return render(request, 'AppLente/turnos.html')

def recetas(request):
    return render(request, 'AppLente/recetas.html')

def contacto(request):

    contexto = {
        'form': Contactoformulario()
    }

    return render(request, 'AppLente/contacto.html', contexto)

def reportes(request):
    return render(request, 'AppLente/reportes.html')

