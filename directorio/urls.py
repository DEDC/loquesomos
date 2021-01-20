# Django
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# App usuario
# --- views
from apps.usuario.views import vLogin, vLogout

urlpatterns = [
    path('login/', vLogin, name = 'login'),
    path('logout/', vLogout, name = 'logout'),
    path('admin/', include('apps.admin.urls', namespace = 'admin')),
    path('', include('apps.directorio.urls', namespace = 'directorio')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
