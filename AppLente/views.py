from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from AppLente.models import Contacto, Turno, Cotiza, Avatar
from django.http import HttpResponse
from AppLente.forms import Contactof, Turnof, Cotizaf,BuscaTurnoPorDNI
from datetime import datetime

def inicio(request):
    user = request.user
    print(f'este es el user {user}')
    print(f'DATO DEL USER:   {(dir(user))}')
    return render(request, 'index.html')

@login_required
def turno(request):

    return render(request, 'AppLente/turnos.html')

def sacarturno(request):
    if request.method == 'POST':
        mi_formulario = Turnof(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            turno1 = Turno(nombre=data.get('nombre'), numero=data.get('numero'), correo=data.get('correo'), dni=data.get('dni'), fecha=data.get('fecha'))
            turno1.save()
            return render(request,'AppLente/sacarTurnoSucceful.html')
    turnos = Turno.objects.all()
    contexto = {
        'form': Turnof(),
        'turnos': turnos
    }
    return render(request, 'AppLente/SacarTurno.html', contexto)

def sacarTurnoSucceful(request):
    render(request,'AppLente/sacarTurnoSucceful.html')

@login_required
def contacto(request):

    if request.method == 'POST':
        mi_formulario = Contactof(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            contacto1 = Contacto(nombre=data.get('nombre'), numero=data.get('numero'), correo=data.get('correo'), mensaje=data.get('mensaje'))
            contacto1.save()

            return render(request, 'AppLente/contactoSuccessful.html')

    contactos = Contacto.objects.all()

    contexto = {
        'form': Contactof(),
        'contactos': contactos
    }

    return render(request, 'AppLente/contacto.html', contexto)

def SuccefulContactoPost(request):
    return render(request, 'AppLente/ContactoSuccessful.html')


@login_required
def cotizar(request):

    if request.method == 'POST':
        mi_formulario = Cotizaf(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            cotiza1 = Cotiza(servicio=data.get('servicio'), mensaje=data.get('mensaje'))
            cotiza1.save()
            return redirect('cotizar')
    cotizar = Cotiza.objects.all()
    contexto = {
        'form': Cotizaf(),
        'cotizar': cotizar
    }
    return render(request, 'AppLente/cotiza.html', contexto)


@login_required
def buscarturno(request):
    con = {
        'form' : BuscaTurnoPorDNI()
    }

    return render(request, 'AppLente/BuscarTurno.html', con)


def resultadoBusqueda(request):
    resultado = request.GET.get('dni')
    try:
        dniEncontrado = Turno.objects.filter(dni__exact = resultado).values("fecha")
        con = {
            'resultado': dniEncontrado.get()['fecha'],
        }
        return render(request,"AppLente/resultadoBusqueda.html",con)
    except:
        con = {
            'resultado': "No tiene ningun turno registrado"
        }
        return render(request,"AppLente/resultadoBusqueda2.html",con)

