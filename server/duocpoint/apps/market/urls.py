from django.http import JsonResponse
from django.urls import path


def market_root(_request):
    """Simple placeholder endpoint for the market app."""
    return JsonResponse({"message": "Market API"})


urlpatterns = [path("market", market_root, name="market-root")]
