from django.urls import path

from .views import PushSubscribeView, PushTestView

urlpatterns = [
    path("push/subscribe", PushSubscribeView.as_view()),
    path("push/test", PushTestView.as_view()),
]
