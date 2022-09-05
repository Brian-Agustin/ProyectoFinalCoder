from django.urls import path

from . import views
from AppLente.views import *


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('turnos/', views.turno, name="turnos"),
    path('recetas/', views.recetas, name="recetas"),
    path('contacto/', views.contacto, name="contacto"),
    path('reportes/', views.reportes, name="reportes"),
]