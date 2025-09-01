from unittest.mock import patch

from django.test import TestCase
from rest_framework.test import APIClient

from duocpoint.apps.accounts.models import User
from .models import PushSub
from .tasks import send_class_push
from pywebpush import WebPushException


class PushTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="b@duocuc.cl", password="x")
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_subscribe(self):
        payload = {
            "endpoint": "https://example.com/ep",
            "p256dh": "k",
            "auth": "a",
        }
        resp = self.client.post("/api/push/subscribe", payload, format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(PushSub.objects.filter(usuario=self.user, endpoint=payload["endpoint"]).exists())

    def test_send_push_handles_invalid(self):
        sub = PushSub.objects.create(
            usuario=self.user,
            endpoint="https://bad/1",
            p256dh="k",
            auth="a",
        )
        with patch("duocpoint.apps.notifications.tasks.webpush", side_effect=WebPushException("bad")):
            send_class_push(self.user.id, None, None, None, test_only=True)
        sub.refresh_from_db()
        self.assertFalse(sub.activo)

    def test_send_push_success(self):
        PushSub.objects.create(
            usuario=self.user,
            endpoint="https://good/1",
            p256dh="k",
            auth="a",
        )
        with patch("duocpoint.apps.notifications.tasks.webpush") as mock_webpush:
            send_class_push(self.user.id, None, None, None, test_only=True)
            self.assertTrue(mock_webpush.called)
