from unicodedata import name
from django.urls import path

from .views import inicio,turnos,recetas,contacto,cotizar,resultadoBusquedaReceta,SacarTurnos,buscarTurnos,resultadoBusquedaTurno
from AppLente.views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('SacarTurnos/', SacarTurnos, name="SacarTurnos"),
    path('recetas/', recetas, name="recetas"),
    path('contacto/', contacto, name="contacto"),
    path('cotizar/', cotizar, name="cotizar"),
    path('resultadoBusqueda', resultadoBusquedaReceta, name="resultadobusqueda"),
    path('turnos/',turnos, name="turnos"),
    path('buscarTurnos',buscarTurnos, name="buscarTurnos"),
    path('resultadoBusquedaTurno/',resultadoBusquedaTurno, name="resultadoBusquedaTurno")
]