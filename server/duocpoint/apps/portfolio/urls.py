from django.urls import path

from .views import PortfolioPDFView

urlpatterns = [path("portfolio", PortfolioPDFView.as_view(), name="portfolio")]
