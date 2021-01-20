# Django
from django.urls import path
# App directorio
# --- views
app_name = 'directorio'
from apps.directorio.views import vHome, vSearch

urlpatterns = [
    path('', vHome, name = 'home'),
    path('search', vSearch)
]