"""URLs para el sistema de compra/venta."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CategoriaProductoViewSet, ProductoViewSet, 
    ProductoReporteViewSet, ProductoAnalyticsViewSet
)

router = DefaultRouter()
router.register(r'categorias', CategoriaProductoViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'reportes', ProductoReporteViewSet)
router.register(r'analytics', ProductoAnalyticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]