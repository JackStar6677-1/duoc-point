"""Generación de portafolio en PDF."""

from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework import permissions, views
from weasyprint import HTML


class PortfolioPDFView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        html = render_to_string("portfolio/basic.html", {"user": request.user})
        pdf = HTML(string=html).write_pdf()
        resp = HttpResponse(pdf, content_type="application/pdf")
        resp["Content-Disposition"] = "attachment; filename=portafolio.pdf"
        return resp
