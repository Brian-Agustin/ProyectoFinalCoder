from django.urls import path

from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('turnos/', views.turnos, name="turnos"),
    path('recetas/', views.recetas, name="recetas"),
    path('contacto/', views.contacto, name="contacto")
]