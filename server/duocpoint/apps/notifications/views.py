"""Views for Web Push subscription management and testing."""

from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import PushSub
from .serializers import PushSubSerializer, SimpleStatusSerializer
from .tasks import send_class_push


class PushSubscribeView(generics.CreateAPIView):
    serializer_class = PushSubSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PushTestView(generics.GenericAPIView):
    """Send a dummy notification to check the service worker."""

    serializer_class = SimpleStatusSerializer

    @extend_schema(responses=SimpleStatusSerializer)
    def post(self, request, *args, **kwargs):
        send_class_push.delay(request.user.id, None, None, None, test_only=True)
        return Response({"status": "sent"})
