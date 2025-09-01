"""Pruebas de API para la funcionalidad de encuestas."""

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from duocpoint.apps.campuses.models import Sede
from duocpoint.apps.forum.models import Foro, Post
from .models import Poll


class PollAPITests(APITestCase):
    """Verifica creación de encuestas, votación y resultados."""

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email="mod@duocuc.cl", password="pass123", role=User.Roles.MODERATOR
        )
        login = self.client.post(
            "/api/auth/login", {"email": self.user.email, "password": "pass123"}
        )
        token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

        sede = Sede.objects.create(
            slug="central", nombre="Sede Central", direccion="Av 1", lat=0, lng=0
        )
        foro = Foro.objects.create(sede=sede, carrera="Ing", titulo="General", slug="gen")
        self.post = Post.objects.create(foro=foro, usuario=self.user, titulo="t", cuerpo="c")

    def _crear_poll(self):
        resp = self.client.post(
            "/api/polls",
            {"post": self.post.id, "multi": False, "opciones": ["a", "b"]},
        )
        self.assertEqual(resp.status_code, 201)
        return resp.data

    def test_crear_poll(self):
        data = self._crear_poll()
        self.assertEqual(Poll.objects.count(), 1)
        self.assertEqual(len(data["opciones"]), 2)

    def test_votar_poll(self):
        poll = self._crear_poll()
        opcion_id = poll["opciones"][0]["id"]
        resp = self.client.post(f"/api/polls/{poll['id']}/votar", {"opciones": [opcion_id]})
        self.assertEqual(resp.status_code, 200)

    def test_resultados_poll(self):
        poll = self._crear_poll()
        opcion_id = poll["opciones"][0]["id"]
        self.client.post(f"/api/polls/{poll['id']}/votar", {"opciones": [opcion_id]})
        detail = self.client.get(f"/api/polls/{poll['id']}")
        self.assertEqual(detail.status_code, 200)
        self.assertEqual(detail.data["opciones"][0]["votos"], 1)
