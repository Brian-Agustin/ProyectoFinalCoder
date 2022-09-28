from django.urls import path

from .views import inicio,turno,recetas,contacto,cotizar,resultadoBusqueda
from AppLente.views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    path('turnos/', turno, name="turnos"),
    path('recetas/', recetas, name="recetas"),
    path('contacto/', contacto, name="contacto"),
    path('cotizar/', cotizar, name="cotizar"),
    path('resultadoBusqueda', resultadoBusqueda, name="resultadobusqueda"),
]