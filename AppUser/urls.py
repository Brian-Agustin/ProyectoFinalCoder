from django.contrib.auth.views import LogoutView
from django.urls import path
from AppUser.views import *


urlpatterns = [
    path('login/', login_request, name="AppUserLogin"),
    path('registro/', register, name="AppUserRegister"),
    path('logout/', LogoutView.as_view(template_name='index.html'), name='AppUserlogout'),
    path('editar/', editar_usuario, name="AppUserEditar"),
]