from django.conf import settings
from django.conf.urls.static import static

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
    path('ContactoSucces/', SuccefulContactoPost, name="contactoSucceful"),
    path('sacarTurnoSucceful/', sacarTurnoSucceful, name="sacarTurnoSucceful"),
    path('recetas/', showimage, name="recetas"),
    path('about/', about, name='about'),
    path('d_turno/<int:dni>', d_turnos, name='d_turno'),
    path('ed_tu/<int:dni>', ed_tu, name='ed_tu')
]


