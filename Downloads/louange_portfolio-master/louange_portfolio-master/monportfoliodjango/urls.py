from django.contrib import admin
from django.urls import path, include

# Importations nécessaires pour les fichiers MEDIA et STATIC en mode développement
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')), # Assurez-vous que cette ligne est présente pour inclure les URLs de votre application portfolio
]

# UNIQUEMENT pour le développement : servir les fichiers MEDIA et STATIC
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Cette ligne est essentielle pour que le serveur de développement de Django serve
    # les fichiers collectés dans STATIC_ROOT (comme votre CV).
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)