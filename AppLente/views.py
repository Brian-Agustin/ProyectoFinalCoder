from django.shortcuts import render, redirect
from AppLente.models import Contacto, Turno, Cotiza
from django.http import HttpResponse
from AppLente.forms import Contactof, Turnof, Cotizaf,BuscaTurnoPorDNI
from datetime import datetime
def inicio(request):
    return render(request, 'index.html')

def contacto(request):

    if request.method == 'POST':
        mi_formulario = Contactof(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            contacto1 = Contacto(nombre=data.get('nombre'), numero=data.get('numero'), correo=data.get('correo'), mensaje=data.get('mensaje'))
            contacto1.save()

            return redirect('contacto')

    contactos = Contacto.objects.all()

    contexto = {
        'form': Contactof(),
        'contactos': contactos
    }
    
    return render(request, 'AppLente/contacto.html', contexto)


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

def recetas(request):
    con = {
        'form' : BuscaTurnoPorDNI()
    }

    return render(request, 'AppLente/recetas.html',con)

def resultadoBusquedaReceta(request):
    resultado = request.GET.get('dni')
    try:
        dniEncontrado = Turno.objects.filter(dni__exact = resultado).values('dni')
        con = {
            'resultado': dniEncontrado.get()['dni'],
        }
        return render(request,"AppLente/resultadoBusqueda.html",con)
    except:
        con = {
            'resultado': "Tu dni nunca ingreso en la base de datos"
        }
        return render(request,"AppLente/resultadoBusqueda.html",con)

def SacarTurnos(request):
    if request.method == 'POST':
        mi_formulario = Turnof(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            turno1 = Turno(nombre=data.get('nombre'), numero=data.get('numero'), correo=data.get('correo'), dni=data.get('dni'), fecha=data.get('fecha'))
            turno1.save()
            return redirect('turnos')
    turnos = Turno.objects.all()
    contexto = {
        'form': Turnof(),
        'turnos': turnos
    }
    return render(request, 'AppLente/SacarTurnos.html', contexto)


def turnos(request):
    return render(request,'AppLente/Turnos.html')

def buscarTurnos(request):
    con ={ 'form' : BuscaTurnoPorDNI() }

    return render(request,'AppLente/buscarTurno.html',con)

def resultadoBusquedaTurno(request):
    resultado = request.GET.get('dni')
    try:
        dniEncontrado = Turno.objects.filter(dni__exact = resultado).values('fecha')
        con = {
            'resultado': dniEncontrado.get()['fecha'],
        }
        return render(request,"AppLente/resultadoBusquedaTurno.html",con)
    except:
        con = {
            'resultado': "Tu dni nunca ingreso en la base de datos"
        }
        return render(request,"AppLente/resultadoBusquedaTurno.html",con)