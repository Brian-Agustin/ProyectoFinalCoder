from unicodedata import name
from django.urls import path

from .views import inicio,turnos,recetas,contacto,cotizar,resultadoBusqueda,SacarTurnos,buscarTurnos
from AppLente.views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('SacarTurnos/', SacarTurnos, name="SacarTurnos"),
    path('recetas/', recetas, name="recetas"),
    path('contacto/', contacto, name="contacto"),
    path('cotizar/', cotizar, name="cotizar"),
    path('resultadoBusqueda', resultadoBusqueda, name="resultadobusqueda"),
    path('turnos/',turnos, name="turnos"),
    path('buscarTurnos',buscarTurnos, name="buscarTurnos"),
]