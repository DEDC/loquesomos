# Django
from django.urls import path
# App admin
# --- views
from .views import (vPrincipalAdmin, vPrincipalCategorias, vPrincipalRepartidores, vPrincipalDirectorio,
    vEditarRepartidores, vEditarDirectorio, vEliminarRepartidores
)
app_name = 'admin'

urlpatterns = [
    path('', vPrincipalAdmin, name = 'pAdmin'),
    path('categorias', vPrincipalCategorias, name = 'pCategorias'),
    path('repartidores', vPrincipalRepartidores, name = 'pRepartidores'),
    path('directorio', vPrincipalDirectorio, name = 'pDirectorio'),
    path('repartidor/<int:id>/editar', vEditarRepartidores, name = 'eRepartidores'),
    path('directorio/<int:id>/editar', vEditarDirectorio, name = 'eDirectorio'),
    path('repartidor/<int:id>/eliminar', vEliminarRepartidores, name = 'elRepartidores')
]