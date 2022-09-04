from django.urls import path

from . import views
from AppLente.views import *


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('turnos/', views.turnos, name="turnos"),
    path('recetas/', views.recetas, name="recetas"),
    path('contacto/', views.contacto, name="contacto"),
    path('reportes/', contacto, name="reportes"),
]