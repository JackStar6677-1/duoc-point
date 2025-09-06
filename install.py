#!/usr/bin/env python
"""
🔧 DuocPoint - Instalador de Dependencias
========================================

Instala todas las dependencias necesarias para DuocPoint:
- Python packages
- ngrok (opcional)
- Base de datos
- Usuarios de prueba

Uso:
    python install.py
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Ejecutar comando con descripción"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✅ {description} completado")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error en {description}: {e}")
        print(f"   Output: {e.stdout}")
        print(f"   Error: {e.stderr}")
        return False

def install_python_packages():
    """Instalar paquetes de Python"""
    print("📦 Instalando paquetes de Python...")
    
    packages = [
        "django>=5.0",
        "djangorestframework>=3.14",
        "django-cors-headers>=4.3",
        "django-celery-results>=2.6",
        "djangorestframework-simplejwt>=5.3",
        "drf-spectacular>=0.26",
        "pillow>=10.0",
        "requests>=2.31",
        "gunicorn>=21.0"
    ]
    
    for package in packages:
        if not run_command(f"pip install {package}", f"Instalando {package}"):
            return False
    
    return True

def install_ngrok():
    """Instalar ngrok (opcional)"""
    print("🌐 Verificando ngrok...")
    
    try:
        result = subprocess.run(['ngrok', 'version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("✅ ngrok ya está instalado")
            return True
    except:
        pass
    
    print("⚠️ ngrok no encontrado")
    print("💡 Para PWA completo en móvil, instala ngrok:")
    print("   1. Ve a https://ngrok.com/download")
    print("   2. Descarga e instala ngrok")
    print("   3. O usa: python start.py local")
    
    return True

def setup_database():
    """Configurar base de datos"""
    print("🗄️ Configurando base de datos...")
    
    server_dir = Path(__file__).parent / "server"
    os.chdir(server_dir)
    
    commands = [
        ("python manage.py migrate", "Aplicando migraciones"),
        ("python manage.py collectstatic --noinput", "Recolectando archivos estáticos")
    ]
    
    for command, description in commands:
        if not run_command(command, description):
            return False
    
    return True

def create_test_users():
    """Crear usuarios de prueba"""
    print("👥 Creando usuarios de prueba...")
    
    server_dir = Path(__file__).parent / "server"
    os.chdir(server_dir)
    
    # Script para crear usuarios
    create_users_script = '''
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duocpoint.settings.dev')
django.setup()

from django.contrib.auth import get_user_model
from duocpoint.apps.campuses.models import Campus

User = get_user_model()

# Crear campus si no existe
campus, created = Campus.objects.get_or_create(
    nombre="Sede Maipú",
    defaults={
        'direccion': 'Av. Américo Vespucio 1501, Maipú',
        'telefono': '+56 2 2000 0000',
        'email': 'maipu@duocuc.cl'
    }
)

# Crear usuarios de prueba
users_data = [
    {
        'email': 'student@duocuc.cl',
        'password': 'student123',
        'name': 'Estudiante',
        'role': 'student',
        'campus': campus,
        'career': 'Ingeniería en Informática'
    },
    {
        'email': 'moderator@duocuc.cl',
        'password': 'moderator123',
        'name': 'Moderador',
        'role': 'moderator',
        'campus': campus,
        'career': 'Administración'
    },
    {
        'email': 'admin@duocuc.cl',
        'password': 'admin123',
        'name': 'Administrador',
        'role': 'admin',
        'campus': campus,
        'career': 'Sistemas'
    }
]

for user_data in users_data:
    user, created = User.objects.get_or_create(
        email=user_data['email'],
        defaults=user_data
    )
    if created:
        user.set_password(user_data['password'])
        user.save()
        print(f"✅ Usuario creado: {user.email}")
    else:
        print(f"⚠️ Usuario ya existe: {user.email}")

print("🎉 Usuarios de prueba creados!")
'''
    
    # Escribir script temporal
    with open('create_users_temp.py', 'w') as f:
        f.write(create_users_script)
    
    # Ejecutar script
    success = run_command('python create_users_temp.py', 'Creando usuarios de prueba')
    
    # Limpiar archivo temporal
    try:
        os.remove('create_users_temp.py')
    except:
        pass
    
    return success

def create_notifications():
    """Crear notificaciones de prueba"""
    print("🔔 Creando notificaciones de prueba...")
    
    server_dir = Path(__file__).parent / "server"
    os.chdir(server_dir)
    
    # Script para crear notificaciones
    create_notifications_script = '''
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duocpoint.settings.dev')
django.setup()

from django.contrib.auth import get_user_model
from duocpoint.apps.notifications.models import Notificacion

User = get_user_model()

# Obtener usuarios
users = User.objects.all()

if not users.exists():
    print("⚠️ No hay usuarios en la base de datos")
    exit()

# Notificaciones de ejemplo
notifications_data = [
    {
        'titulo': '¡Bienvenido a DuocPoint!',
        'mensaje': 'Tu cuenta ha sido creada exitosamente. Explora todas las funcionalidades disponibles.',
        'tipo': 'success'
    },
    {
        'titulo': 'Nuevo post en el foro',
        'mensaje': 'Se ha publicado un nuevo tema en "Programación Web". ¡Participa en la discusión!',
        'tipo': 'forum'
    },
    {
        'titulo': 'Producto disponible en el mercado',
        'mensaje': 'El libro "Python para Principiantes" está disponible por $15.000.',
        'tipo': 'market'
    },
    {
        'titulo': 'Recorrido virtual disponible',
        'mensaje': 'Explora el nuevo recorrido virtual del Campus San Carlos de Apoquindo.',
        'tipo': 'campus'
    },
    {
        'titulo': 'Actualización del portafolio',
        'mensaje': 'Tu portafolio ha sido actualizado exitosamente. ¡Comparte tus proyectos!',
        'tipo': 'portfolio'
    }
]

created_count = 0

for user in users:
    for notification_data in notifications_data:
        notification = Notificacion.objects.create(
            usuario=user,
            titulo=notification_data['titulo'],
            mensaje=notification_data['mensaje'],
            tipo=notification_data['tipo']
        )
        created_count += 1

print(f"🎉 Se crearon {created_count} notificaciones de prueba")
print(f"👥 Para {users.count()} usuarios")
'''
    
    # Escribir script temporal
    with open('create_notifications_temp.py', 'w') as f:
        f.write(create_notifications_script)
    
    # Ejecutar script
    success = run_command('python create_notifications_temp.py', 'Creando notificaciones de prueba')
    
    # Limpiar archivo temporal
    try:
        os.remove('create_notifications_temp.py')
    except:
        pass
    
    return success

def main():
    """Función principal"""
    print("=" * 60)
    print("🔧 DuocPoint - Instalador de Dependencias")
    print("=" * 60)
    
    steps = [
        ("Instalando paquetes de Python", install_python_packages),
        ("Verificando ngrok", install_ngrok),
        ("Configurando base de datos", setup_database),
        ("Creando usuarios de prueba", create_test_users),
        ("Creando notificaciones de prueba", create_notifications)
    ]
    
    for description, function in steps:
        print(f"\n📋 {description}...")
        if not function():
            print(f"❌ Error en: {description}")
            return False
    
    print("\n" + "=" * 60)
    print("🎉 ¡INSTALACIÓN COMPLETADA!")
    print("=" * 60)
    print("🚀 Para iniciar DuocPoint:")
    print("   python start.py")
    print()
    print("📱 Para PWA en móvil:")
    print("   python start.py ngrok")
    print()
    print("🧪 Para solo tests:")
    print("   python start.py test")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)
