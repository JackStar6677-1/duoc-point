"""Views para el sistema de portafolio."""

import io
import os
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.conf import settings
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

from .models import (
    Logro, Proyecto, ExperienciaLaboral, Habilidad,
    PortafolioConfig, PortafolioSugerencia, PortafolioAnalytics
)
from .serializers import (
    LogroSerializer, ProyectoSerializer, ExperienciaLaboralSerializer,
    HabilidadSerializer, PortafolioConfigSerializer, PortafolioSugerenciaSerializer,
    PortafolioAnalyticsSerializer, PortafolioCompletoSerializer
)


class LogroViewSet(viewsets.ModelViewSet):
    """ViewSet para logros."""
    
    serializer_class = LogroSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Logro.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ProyectoViewSet(viewsets.ModelViewSet):
    """ViewSet para proyectos."""
    
    serializer_class = ProyectoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ExperienciaLaboralViewSet(viewsets.ModelViewSet):
    """ViewSet para experiencias laborales."""
    
    serializer_class = ExperienciaLaboralSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return ExperienciaLaboral.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class HabilidadViewSet(viewsets.ModelViewSet):
    """ViewSet para habilidades."""
    
    serializer_class = HabilidadSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Habilidad.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class PortafolioConfigViewSet(viewsets.ModelViewSet):
    """ViewSet para configuración de portafolio."""
    
    serializer_class = PortafolioConfigSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return PortafolioConfig.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    
    def get_object(self):
        """Obtiene o crea la configuración del usuario."""
        obj, created = PortafolioConfig.objects.get_or_create(
            usuario=self.request.user
        )
        return obj


class PortafolioSugerenciaViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet para sugerencias de portafolio."""
    
    serializer_class = PortafolioSugerenciaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return PortafolioSugerencia.objects.filter(
            usuario=self.request.user,
            completada=False
        )
    
    @extend_schema(
        summary="Marcar sugerencia como completada",
        responses={200: {"description": "Sugerencia marcada como completada"}}
    )
    @action(detail=True, methods=['post'])
    def completar(self, request, pk=None):
        """Marca una sugerencia como completada."""
        sugerencia = self.get_object()
        sugerencia.completada = True
        sugerencia.save()
        
        # Actualizar analytics
        try:
            analytics = request.user.portafolio_analytics
            analytics.actualizar_estadisticas()
        except PortafolioAnalytics.DoesNotExist:
            PortafolioAnalytics.objects.create(usuario=request.user)
        
        return Response({'message': 'Sugerencia completada'})


class PortafolioAnalyticsViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet para analytics de portafolio."""
    
    serializer_class = PortafolioAnalyticsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return PortafolioAnalytics.objects.filter(usuario=self.request.user)
    
    def get_object(self):
        """Obtiene o crea los analytics del usuario."""
        obj, created = PortafolioAnalytics.objects.get_or_create(
            usuario=self.request.user
        )
        if created:
            obj.actualizar_estadisticas()
        return obj


class PortafolioCompletoViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet para obtener toda la información del portafolio."""
    
    serializer_class = PortafolioCompletoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return [self.request.user]
    
    def get_object(self):
        return self.request.user
    
    @extend_schema(
        summary="Generar PDF del portafolio",
        responses={200: {"description": "PDF generado exitosamente"}}
    )
    @action(detail=False, methods=['get'])
    def generar_pdf(self, request):
        """Genera un PDF del portafolio del usuario."""
        try:
            # Obtener datos del usuario
            usuario = request.user
            
            # Asegurar que existe configuración
            config, created = PortafolioConfig.objects.get_or_create(usuario=usuario)
            
            # Obtener datos del portafolio
            logros = Logro.objects.filter(usuario=usuario, visible=True)
            proyectos = Proyecto.objects.filter(usuario=usuario, visible=True)
            experiencias = ExperienciaLaboral.objects.filter(usuario=usuario, visible=True)
            habilidades = Habilidad.objects.filter(usuario=usuario, visible=True)
            
            # Contexto para el template
            context = {
                'usuario': usuario,
                'config': config,
                'logros': logros,
                'proyectos': proyectos,
                'experiencias': experiencias,
                'habilidades': habilidades,
            }
            
            # Renderizar HTML
            html_string = render_to_string('portfolio/portafolio_pdf.html', context)
            
            # Generar PDF
            font_config = FontConfiguration()
            html_doc = HTML(string=html_string)
            
            # CSS personalizado
            css_string = """
            @page {
                size: A4;
                margin: 2cm;
            }
            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
            }
            .header {
                text-align: center;
                border-bottom: 2px solid #2e004f;
                padding-bottom: 20px;
                margin-bottom: 30px;
            }
            .section {
                margin-bottom: 30px;
            }
            .section h2 {
                color: #2e004f;
                border-bottom: 1px solid #ddd;
                padding-bottom: 5px;
            }
            .item {
                margin-bottom: 15px;
                padding: 10px;
                border-left: 3px solid #2e004f;
                background-color: #f9f9f9;
            }
            """
            
            css_doc = CSS(string=css_string, font_config=font_config)
            
            # Generar PDF
            pdf_buffer = io.BytesIO()
            html_doc.write_pdf(pdf_buffer, stylesheets=[css_doc], font_config=font_config)
            pdf_buffer.seek(0)
            
            # Actualizar analytics
            try:
                analytics = usuario.portafolio_analytics
                analytics.descargas_pdf += 1
                analytics.save()
            except PortafolioAnalytics.DoesNotExist:
                PortafolioAnalytics.objects.create(usuario=usuario)
            
            # Marcar generación en configuración
            config.generar_pdf()
            
            # Respuesta
            response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="portafolio_{usuario.name.replace(" ", "_")}.pdf"'
            return response
            
        except Exception as e:
            return Response(
                {'error': f'Error generando PDF: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    @extend_schema(
        summary="Generar sugerencias automáticas",
        responses={200: {"description": "Sugerencias generadas"}}
    )
    @action(detail=False, methods=['post'])
    def generar_sugerencias(self, request):
        """Genera sugerencias automáticas para mejorar el portafolio."""
        usuario = request.user
        
        # Limpiar sugerencias anteriores no completadas
        PortafolioSugerencia.objects.filter(
            usuario=usuario, 
            completada=False
        ).delete()
        
        sugerencias = []
        
        # Verificar completitud del perfil
        if not usuario.name or len(usuario.name.strip()) < 3:
            sugerencias.append({
                'tipo': 'completar_perfil',
                'titulo': 'Completar nombre completo',
                'descripcion': 'Agrega tu nombre completo para que tu portafolio se vea más profesional.',
                'prioridad': 'alta'
            })
        
        # Verificar configuración de portafolio
        try:
            config = usuario.portafolio_config
            if not config.titulo_profesional:
                sugerencias.append({
                    'tipo': 'completar_perfil',
                    'titulo': 'Agregar título profesional',
                    'descripcion': 'Define tu título profesional o área de especialización.',
                    'prioridad': 'alta'
                })
            
            if not config.resumen_profesional:
                sugerencias.append({
                    'tipo': 'mejorar_descripcion',
                    'titulo': 'Escribir resumen profesional',
                    'descripcion': 'Crea un resumen profesional que destaque tus fortalezas y objetivos.',
                    'prioridad': 'alta'
                })
        except PortafolioConfig.DoesNotExist:
            sugerencias.append({
                'tipo': 'completar_perfil',
                'titulo': 'Configurar portafolio',
                'descripcion': 'Completa la configuración básica de tu portafolio.',
                'prioridad': 'alta'
            })
        
        # Verificar logros
        logros_count = Logro.objects.filter(usuario=usuario, visible=True).count()
        if logros_count == 0:
            sugerencias.append({
                'tipo': 'agregar_logros',
                'titulo': 'Agregar logros y certificaciones',
                'descripcion': 'Incluye certificaciones, premios o logros académicos y profesionales.',
                'prioridad': 'media'
            })
        
        # Verificar proyectos
        proyectos_count = Proyecto.objects.filter(usuario=usuario, visible=True).count()
        if proyectos_count == 0:
            sugerencias.append({
                'tipo': 'agregar_proyectos',
                'titulo': 'Agregar proyectos',
                'descripcion': 'Muestra tus proyectos más importantes con descripción y tecnologías utilizadas.',
                'prioridad': 'alta'
            })
        elif proyectos_count < 3:
            sugerencias.append({
                'tipo': 'agregar_proyectos',
                'titulo': 'Agregar más proyectos',
                'descripcion': 'Incluye al menos 3 proyectos para mostrar tu experiencia.',
                'prioridad': 'media'
            })
        
        # Verificar experiencias
        experiencias_count = ExperienciaLaboral.objects.filter(usuario=usuario, visible=True).count()
        if experiencias_count == 0:
            sugerencias.append({
                'tipo': 'agregar_experiencia',
                'titulo': 'Agregar experiencia laboral',
                'descripcion': 'Incluye prácticas profesionales, trabajos o voluntariados.',
                'prioridad': 'media'
            })
        
        # Verificar habilidades
        habilidades_count = Habilidad.objects.filter(usuario=usuario, visible=True).count()
        if habilidades_count == 0:
            sugerencias.append({
                'tipo': 'mejorar_habilidades',
                'titulo': 'Agregar habilidades',
                'descripcion': 'Lista tus habilidades técnicas y blandas con niveles de competencia.',
                'prioridad': 'alta'
            })
        elif habilidades_count < 5:
            sugerencias.append({
                'tipo': 'mejorar_habilidades',
                'titulo': 'Completar habilidades',
                'descripcion': 'Agrega más habilidades para mostrar tu versatilidad.',
                'prioridad': 'media'
            })
        
        # Crear sugerencias
        for sugerencia_data in sugerencias:
            PortafolioSugerencia.objects.create(
                usuario=usuario,
                **sugerencia_data
            )
        
        return Response({
            'message': f'Se generaron {len(sugerencias)} sugerencias',
            'sugerencias_count': len(sugerencias)
        })
