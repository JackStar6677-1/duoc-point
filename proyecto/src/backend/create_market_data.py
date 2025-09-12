#!/usr/bin/env python
"""
Script para crear datos de prueba del mercado
"""

import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duocpoint.settings.dev')
django.setup()

from duocpoint.apps.market.models import CategoriaProducto, Producto
from django.contrib.auth import get_user_model

User = get_user_model()

def create_market_data():
    """Crear datos de prueba para el mercado."""
    
    print("🛒 Creando datos del mercado...")
    
    # Crear categorías
    categorias_data = [
        {
            'nombre': 'Libros y Apuntes',
            'descripcion': 'Libros de texto, apuntes, guías de estudio y material académico.',
            'icono': 'fas fa-book',
            'activa': True
        },
        {
            'nombre': 'Tecnología',
            'descripcion': 'Laptops, tablets, accesorios, cables y dispositivos electrónicos.',
            'icono': 'fas fa-laptop',
            'activa': True
        },
        {
            'nombre': 'Ropa y Accesorios',
            'descripcion': 'Ropa casual, uniformes, mochilas y accesorios estudiantiles.',
            'icono': 'fas fa-tshirt',
            'activa': True
        },
        {
            'nombre': 'Hogar y Oficina',
            'descripcion': 'Muebles, decoración, artículos de oficina y productos para el hogar.',
            'icono': 'fas fa-home',
            'activa': True
        },
        {
            'nombre': 'Deportes y Fitness',
            'descripcion': 'Equipamiento deportivo, ropa deportiva y accesorios fitness.',
            'icono': 'fas fa-dumbbell',
            'activa': True
        },
        {
            'nombre': 'Otros',
            'descripcion': 'Productos diversos que no encajan en otras categorías.',
            'icono': 'fas fa-ellipsis-h',
            'activa': True
        }
    ]
    
    created_categories = 0
    
    for categoria_data in categorias_data:
        categoria, created = CategoriaProducto.objects.get_or_create(
            nombre=categoria_data['nombre'],
            defaults=categoria_data
        )
        
        if created:
            created_categories += 1
            print(f"✅ Categoría creada: {categoria.nombre}")
        else:
            print(f"⚠️ Categoría ya existe: {categoria.nombre}")
    
    print(f"\n🎉 Se crearon {created_categories} categorías")
    
    # Crear productos de ejemplo
    create_sample_products()

def create_sample_products():
    """Crear productos de ejemplo."""
    
    print("\n📦 Creando productos de ejemplo...")
    
    # Obtener usuario de ejemplo
    try:
        user = User.objects.get(email='student@duocuc.cl')
    except User.DoesNotExist:
        print("⚠️ Usuario student@duocuc.cl no encontrado")
        return
    
    # Obtener categorías
    categorias = CategoriaProducto.objects.filter(activa=True)
    
    if not categorias.exists():
        print("⚠️ No hay categorías disponibles")
        return
    
    # Productos de ejemplo
    productos_data = [
        {
            'titulo': 'Libro de Programación Web - React',
            'descripcion': 'Libro en excelente estado sobre React y desarrollo web moderno. Incluye ejemplos prácticos.',
            'precio': 15000,
            'categoria': categorias.filter(nombre='Libros y Apuntes').first(),
            'estado': 'publicado',
            'url_principal': 'https://example.com/libro-react'
        },
        {
            'titulo': 'Laptop HP Pavilion 15"',
            'descripcion': 'Laptop en buen estado, ideal para programación. Intel i5, 8GB RAM, 256GB SSD.',
            'precio': 450000,
            'categoria': categorias.filter(nombre='Tecnología').first(),
            'estado': 'publicado',
            'url_principal': 'https://example.com/laptop-hp'
        },
        {
            'titulo': 'Mochila North Face',
            'descripcion': 'Mochila resistente para laptop, perfecta para estudiantes. Color negro.',
            'precio': 35000,
            'categoria': categorias.filter(nombre='Ropa y Accesorios').first(),
            'estado': 'publicado',
            'url_principal': 'https://example.com/mochila-northface'
        },
        {
            'titulo': 'Escritorio de Estudio',
            'descripcion': 'Escritorio compacto ideal para estudiar en casa. Incluye cajones.',
            'precio': 80000,
            'categoria': categorias.filter(nombre='Hogar y Oficina').first(),
            'estado': 'publicado',
            'url_principal': 'https://example.com/escritorio-estudio'
        },
        {
            'titulo': 'Pesas Ajustables 20kg',
            'descripcion': 'Set de pesas ajustables para ejercicio en casa. Incluye barras y discos.',
            'precio': 120000,
            'categoria': categorias.filter(nombre='Deportes y Fitness').first(),
            'estado': 'publicado',
            'url_principal': 'https://example.com/pesas-ajustables'
        }
    ]
    
    created_products = 0
    
    for producto_data in productos_data:
        if producto_data['categoria']:
            producto, created = Producto.objects.get_or_create(
                titulo=producto_data['titulo'],
                vendedor=user,
                defaults={
                    'descripcion': producto_data['descripcion'],
                    'precio': producto_data['precio'],
                    'categoria': producto_data['categoria'],
                    'estado': producto_data['estado'],
                    'url_principal': producto_data['url_principal']
                }
            )
            
            if created:
                created_products += 1
                print(f"✅ Producto creado: {producto.titulo}")
    
    print(f"🎉 Se crearon {created_products} productos de ejemplo")

if __name__ == "__main__":
    create_market_data()
