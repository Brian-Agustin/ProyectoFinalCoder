from django.urls import path
from AppUser.views import *


urlpatterns = [
    path('login/', login_request, name="AppUserLogin"),
]