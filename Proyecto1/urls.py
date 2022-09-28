from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppLente.urls')),
    path('', include('AppUser.urls')),
]