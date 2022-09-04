from django.shortcuts import render

from django.http import HttpResponse


def inicio(request):
    return render(request, 'index.html')

def turnos(request):
    return render(request, 'AppLente/turnos.html')

def recetas(request):
    return render(request, 'AppLente/recetas.html')

def contacto(request):
    return render(request, 'AppLente/contacto.html')

def reportes(request):
    return render(request, 'AppLente/reportes.html')