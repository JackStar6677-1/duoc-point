"""
URL configuration for duocpoint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.views.static import serve
from pathlib import Path
from rest_framework_simplejwt.views import TokenRefreshView


def spa_serve(request, path=""):
    base = Path(settings.BASE_DIR).parent / "frontend"
    target = base / path
    if target.is_dir():
        path = f"{path.rstrip('/')}/index.html"
    return serve(request, path, document_root=base)

urlpatterns = [
    path('', RedirectView.as_view(url='/index.html', permanent=False)),
    path('admin/', admin.site.urls),
    path('api/', include('duocpoint.apps.accounts.urls')),
    path('api/', include('duocpoint.apps.campuses.urls')),
    path('api/', include('duocpoint.apps.forum.urls')),
    path('api/', include('duocpoint.apps.market.urls')),
    path('api/', include('duocpoint.apps.polls.urls')),
    path('api/', include('duocpoint.apps.schedules.urls')),
    path('api/', include('duocpoint.apps.notifications.urls')),
    path('api/', include('duocpoint.apps.reports.urls')),
    path('api/', include('duocpoint.apps.otec.urls')),
    path('api/', include('duocpoint.apps.wellbeing.urls')),
    path('api/', include('duocpoint.apps.portfolio.urls')),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('', include('duocpoint.apps.health.urls')),
    # Servir imágenes antes del catch-all
    re_path(r'^imagenes/(?P<path>.*)$', serve, {'document_root': Path(settings.BASE_DIR).parent / "imagenes"}),
    re_path(r'^(?P<path>.*)$', spa_serve),
]

# Servir archivos estáticos en desarrollo
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Servir imágenes desde la carpeta imagenes
    urlpatterns += static('/imagenes/', document_root=Path(settings.BASE_DIR).parent / "imagenes")
