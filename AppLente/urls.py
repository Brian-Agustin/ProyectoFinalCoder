from unicodedata import name
from django.urls import path

from AppLente.views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('turnos/', turno, name="turnos"),
    path('contacto/', contacto, name="contacto"),
    path('cotizar/', cotizar, name="cotizar"),
    path('sacarturno/', sacarturno, name="SacarTurno"),
    path('buscarturno/', buscarturno, name="buscarturno"),
    path('resultadoBusqueda', resultadoBusqueda, name="resultadobusqueda"),
]