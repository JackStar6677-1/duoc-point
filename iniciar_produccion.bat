@echo off
chcp 65001 >nul
title DuocPoint - Modo Producción

echo ============================================================
echo    DuocPoint - Sistema de Gestión Estudiantil
echo    Modo Producción con PostgreSQL
echo    Versión 1.2.0
echo ============================================================
echo.

echo [INFO] Configurando entorno de producción...
echo [INFO] Verificando dependencias...

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no está instalado o no está en el PATH
    echo [INFO] Por favor instala Python 3.8+ desde https://python.org
    pause
    exit /b 1
)

REM Verificar si PostgreSQL está instalado
psql --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] PostgreSQL no está instalado o no está en el PATH
    echo [INFO] Por favor instala PostgreSQL desde https://postgresql.org
    pause
    exit /b 1
)

echo [INFO] Python detectado
echo [INFO] PostgreSQL detectado

REM Cambiar al directorio del backend
cd /d "%~dp0src\backend"

echo.
echo [INFO] Instalando dependencias de producción...
pip install -r requirements.txt

echo.
echo [INFO] Configurando base de datos PostgreSQL...

REM Crear base de datos si no existe
echo [INFO] Creando base de datos 'duocpoint_prod'...
psql -U postgres -c "CREATE DATABASE duocpoint_prod;" 2>nul || echo [INFO] Base de datos ya existe o error de conexión

echo.
echo [INFO] Ejecutando migraciones...
python manage.py migrate --settings=duocpoint.settings.prod

echo.
echo [INFO] Creando superusuario...
echo [INFO] Si ya existe, se omitirá la creación
python manage.py createsuperuser --settings=duocpoint.settings.prod --noinput --email admin@duocuc.cl --username admin 2>nul || echo [INFO] Superusuario ya existe

echo.
echo [INFO] Cargando datos iniciales...
python manage.py loaddata initial_data --settings=duocpoint.settings.prod 2>nul || echo [INFO] No hay datos iniciales para cargar

echo.
echo [INFO] Recopilando archivos estáticos...
python manage.py collectstatic --settings=duocpoint.settings.prod --noinput

echo.
echo ============================================================
echo [INFO] Sistema listo para producción
echo.
echo 🌐 La aplicación estará disponible en:
echo    - Aplicación: http://localhost:8000
echo    - Admin: http://localhost:8000/admin/
echo    - API: http://localhost:8000/api/
echo.
echo 👤 Credenciales por defecto:
echo    - Email: admin@duocuc.cl
echo    - Contraseña: admin123
echo.
echo 🔧 Modo producción activado:
echo    - DEBUG=False
echo    - Base de datos: PostgreSQL
echo    - Archivos estáticos servidos por Django
echo.
echo ⚠️  IMPORTANTE:
echo    - Configura las variables de entorno en .env
echo    - Asegúrate de que PostgreSQL esté ejecutándose
echo    - Para producción real, usa un servidor WSGI como Gunicorn
echo.
echo Presiona Ctrl+C para detener el servidor
echo ============================================================

echo.
echo [INFO] Iniciando servidor de producción...
python manage.py runserver 0.0.0.0:8000 --settings=duocpoint.settings.prod

echo.
echo [INFO] Servidor detenido
pause
