#!/usr/bin/env python3
"""
Script para configurar StudentsPoint en modo producción
Configura PostgreSQL y aplica migraciones
"""

import os
import sys
import subprocess
import psycopg2
from pathlib import Path

# Configuración de PostgreSQL
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': '214526867',
    'database': 'studentspoint_prod'
}

def verificar_postgresql():
    """Verificar conexión a PostgreSQL"""
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database='postgres'  # Conectar a base por defecto
        )
        conn.close()
        print("✅ Conexión a PostgreSQL exitosa")
        return True
    except Exception as e:
        print(f"❌ Error conectando a PostgreSQL: {e}")
        return False

def crear_base_datos():
    """Crear base de datos de producción"""
    try:
        conn = psycopg2.connect(
            host=DB_CONFIG['host'],
            port=DB_CONFIG['port'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database='postgres'
        )
        conn.autocommit = True
        cursor = conn.cursor()
        
        # Verificar si la base de datos existe
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_CONFIG['database'],))
        if cursor.fetchone():
            print(f"✅ Base de datos '{DB_CONFIG['database']}' ya existe")
        else:
            cursor.execute(f"CREATE DATABASE {DB_CONFIG['database']}")
            print(f"✅ Base de datos '{DB_CONFIG['database']}' creada")
        
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"❌ Error creando base de datos: {e}")
        return False

def configurar_variables_entorno():
    """Configurar variables de entorno para producción"""
    env_content = f"""# Configuración de Producción - StudentsPoint
SECRET_KEY=studentspoint-prod-secret-key-{os.urandom(32).hex()}
DEBUG=0
ALLOWED_HOSTS=studentspoint.app,www.studentspoint.app,localhost,127.0.0.1

# Base de Datos PostgreSQL
DB_ENGINE=django.db.backends.postgresql
DB_NAME={DB_CONFIG['database']}
DB_USER={DB_CONFIG['user']}
DB_PASSWORD={DB_CONFIG['password']}
DB_HOST={DB_CONFIG['host']}
DB_PORT={DB_CONFIG['port']}

# CORS
CORS_ALLOWED_ORIGINS=https://studentspoint.app,https://www.studentspoint.app,http://localhost:8000

# Google OAuth
GOOGLE_REDIRECT_URI=https://studentspoint.app/api/auth/google/callback/web/
FRONTEND_URL=https://studentspoint.app

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0
"""
    
    env_file = Path('.env')
    with open(env_file, 'w', encoding='utf-8') as f:
        f.write(env_content)
    
    print("✅ Archivo .env creado con configuración de producción")

def aplicar_migraciones():
    """Aplicar migraciones de Django"""
    try:
        # Configurar variables de entorno para producción
        os.environ['DJANGO_SETTINGS_MODULE'] = 'studentspoint.settings.prod'
        
        # Aplicar migraciones
        result = subprocess.run([
            sys.executable, 'manage.py', 'migrate', '--settings=studentspoint.settings.prod'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Migraciones aplicadas exitosamente")
            return True
        else:
            print(f"❌ Error aplicando migraciones: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error ejecutando migraciones: {e}")
        return False

def crear_superusuario():
    """Crear superusuario para producción"""
    try:
        result = subprocess.run([
            sys.executable, 'ensure_superuser.py'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Superusuario creado exitosamente")
            return True
        else:
            print(f"❌ Error creando superusuario: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error ejecutando script de superusuario: {e}")
        return False

def recolectar_archivos_estaticos():
    """Recolectar archivos estáticos"""
    try:
        result = subprocess.run([
            sys.executable, 'manage.py', 'collectstatic', '--noinput', '--settings=studentspoint.settings.prod'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Archivos estáticos recolectados")
            return True
        else:
            print(f"❌ Error recolectando archivos estáticos: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error ejecutando collectstatic: {e}")
        return False

def main():
    """Función principal"""
    print("🚀 Configurando StudentsPoint para Producción")
    print("=" * 50)
    
    # Verificar que estamos en el directorio correcto
    if not Path('manage.py').exists():
        print("❌ Error: Ejecutar este script desde el directorio backend")
        sys.exit(1)
    
    # Paso 1: Verificar PostgreSQL
    if not verificar_postgresql():
        print("❌ No se puede continuar sin PostgreSQL")
        sys.exit(1)
    
    # Paso 2: Crear base de datos
    if not crear_base_datos():
        print("❌ No se puede continuar sin la base de datos")
        sys.exit(1)
    
    # Paso 3: Configurar variables de entorno
    configurar_variables_entorno()
    
    # Paso 4: Aplicar migraciones
    if not aplicar_migraciones():
        print("❌ Error en migraciones")
        sys.exit(1)
    
    # Paso 5: Crear superusuario
    if not crear_superusuario():
        print("⚠️  Advertencia: No se pudo crear superusuario automáticamente")
        print("   Crear manualmente con: python manage.py createsuperuser --settings=studentspoint.settings.prod")
    
    # Paso 6: Recolectar archivos estáticos
    if not recolectar_archivos_estaticos():
        print("⚠️  Advertencia: Error recolectando archivos estáticos")
    
    print("\n" + "=" * 50)
    print("✅ Configuración de producción completada")
    print("\n📋 Próximos pasos:")
    print("1. Verificar configuración en archivo .env")
    print("2. Iniciar servidor: python manage.py runserver 0.0.0.0:8000 --settings=studentspoint.settings.prod")
    print("3. Configurar nginx/apache para servir archivos estáticos")
    print("4. Configurar SSL/HTTPS")
    print("\n🔗 URLs de acceso:")
    print("- Aplicación: http://localhost:8000")
    print("- Admin: http://localhost:8000/admin/")
    print("- API Docs: http://localhost:8000/api/docs/")

if __name__ == "__main__":
    main()
