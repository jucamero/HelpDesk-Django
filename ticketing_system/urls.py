from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('tickets.urls')),  # Esto elimina el prefijo 'tickets/' y las URLs serán directas
    path('admin/', admin.site.urls),
]