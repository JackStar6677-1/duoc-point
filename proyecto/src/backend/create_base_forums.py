#!/usr/bin/env python
"""
Script para crear foros de base
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duocpoint.settings.dev')
django.setup()

from duocpoint.apps.forum.models import Foro, Post, Comentario
from duocpoint.apps.campuses.models import Sede
from django.contrib.auth import get_user_model

User = get_user_model()

def create_base_forums():
    """Crear foros de base para el sistema."""
    
    print("🏗️ Creando foros de base...")
    
    # Obtener sede por defecto
    sede, created = Sede.objects.get_or_create(
        nombre="Sede Maipú",
        defaults={
            'slug': 'sede-maipu',
            'direccion': 'Av. Américo Vespucio 1501, Maipú',
            'lat': -33.5111,
            'lng': -70.7585
        }
    )
    
    # Foros de base
    forums_data = [
        {
            'titulo': 'Programación Web',
            'carrera': 'Ingeniería en Informática',
            'slug': 'programacion-web',
            'sede': sede
        },
        {
            'titulo': 'Base de Datos',
            'carrera': 'Ingeniería en Informática',
            'slug': 'base-de-datos',
            'sede': sede
        },
        {
            'titulo': 'Ingeniería de Software',
            'carrera': 'Ingeniería en Informática',
            'slug': 'ingenieria-software',
            'sede': sede
        },
        {
            'titulo': 'Redes y Seguridad',
            'carrera': 'Ingeniería en Informática',
            'slug': 'redes-seguridad',
            'sede': sede
        },
        {
            'titulo': 'Inteligencia Artificial',
            'carrera': 'Ingeniería en Informática',
            'slug': 'inteligencia-artificial',
            'sede': sede
        },
        {
            'titulo': 'Proyectos y Tesis',
            'carrera': 'Ingeniería en Informática',
            'slug': 'proyectos-tesis',
            'sede': sede
        },
        {
            'titulo': 'Vida Universitaria',
            'carrera': 'General',
            'slug': 'vida-universitaria',
            'sede': sede
        },
        {
            'titulo': 'Empleos y Prácticas',
            'carrera': 'General',
            'slug': 'empleos-practicas',
            'sede': sede
        }
    ]
    
    created_count = 0
    
    for forum_data in forums_data:
        forum, created = Foro.objects.get_or_create(
            slug=forum_data['slug'],
            defaults=forum_data
        )
        
        if created:
            created_count += 1
            print(f"✅ Foro creado: {forum.titulo}")
        else:
            print(f"⚠️ Foro ya existe: {forum.titulo}")
    
    print(f"\n🎉 Se crearon {created_count} foros de base")
    
    # Crear algunos posts de ejemplo
    create_sample_posts()
    
def create_sample_posts():
    """Crear posts de ejemplo en los foros."""
    
    print("\n📝 Creando posts de ejemplo...")
    
    # Obtener usuario de ejemplo
    try:
        user = User.objects.get(email='student@duocuc.cl')
    except User.DoesNotExist:
        print("⚠️ Usuario student@duocuc.cl no encontrado")
        return
    
    # Obtener foros
    foros = Foro.objects.all()[:3]  # Solo los primeros 3
    
    sample_posts = [
        {
            'titulo': '¿Cómo empezar con React?',
            'cuerpo': 'Hola compañeros, estoy empezando a aprender React y me gustaría saber cuáles son los mejores recursos para principiantes. ¿Alguien tiene recomendaciones?',
            'foro': foros[0] if len(foros) > 0 else None
        },
        {
            'titulo': 'Consulta sobre consultas SQL complejas',
            'cuerpo': 'Necesito ayuda con una consulta que involucra múltiples JOINs. ¿Alguien puede ayudarme a optimizarla?',
            'foro': foros[1] if len(foros) > 1 else None
        },
        {
            'titulo': 'Evento de networking - Próximo viernes',
            'cuerpo': '¡Hola! Les informo que el próximo viernes habrá un evento de networking con empresas tecnológicas en el auditorio principal. ¡No se lo pierdan!',
            'foro': foros[2] if len(foros) > 2 else None
        }
    ]
    
    created_posts = 0
    
    for post_data in sample_posts:
        if post_data['foro']:
            post, created = Post.objects.get_or_create(
                titulo=post_data['titulo'],
                usuario=user,
                foro=post_data['foro'],
                defaults={
                    'cuerpo': post_data['cuerpo'],
                    'estado': 'publicado'
                }
            )
            
            if created:
                created_posts += 1
                print(f"✅ Post creado: {post.titulo}")
    
    print(f"🎉 Se crearon {created_posts} posts de ejemplo")

if __name__ == "__main__":
    create_base_forums()
