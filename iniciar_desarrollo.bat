@echo off
chcp 65001 >nul
title DuocPoint - Desarrollo Local

echo.
echo ============================================================
echo    DuocPoint - Modo Desarrollo Local
echo    Versión 1.2.0
echo ============================================================
echo.

:: Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado
    echo Descarga Python desde: https://python.org
    pause
    exit /b 1
)

echo [INFO] Configurando entorno de desarrollo...

:: Crear archivo .env si no existe
if not exist ".env" (
    echo [INFO] Creando archivo de configuración local...
    copy "config_local.env" ".env" >nul 2>&1
)

:: Crear directorio config si no existe
if not exist "config" (
    echo [INFO] Creando directorio de configuración...
    mkdir config >nul 2>&1
)

:: Crear archivo push.yaml si no existe
if not exist "config\push.yaml" (
    echo [INFO] Creando configuración de notificaciones push...
    echo # Configuración de Web Push Notifications > "config\push.yaml"
    echo vapid_public: "BEl62iUYgUivxIkv69yViEuiBIa40HI8l8V6V1V8H3BZ7pRJvnSW4UPHW3v3T1td1K3_fSqiNI2j_lLQ6Ypy1XM" >> "config\push.yaml"
    echo vapid_private: "3K1XdXz0L8Fz0aJSOdwuSeiJfZ5JWY7BdI3R2kS2aJ8" >> "config\push.yaml"
    echo subject: "mailto:admin@duocuc.cl" >> "config\push.yaml"
)

:: Crear archivo security.yaml si no existe
if not exist "config\security.yaml" (
    echo [INFO] Creando configuración de seguridad...
    echo # Configuración de seguridad > "config\security.yaml"
    echo file_validation: >> "config\security.yaml"
    echo   max_file_size: 10485760 >> "config\security.yaml"
    echo   allowed_extensions: [".pdf", ".jpg", ".jpeg", ".png", ".gif"] >> "config\security.yaml"
    echo rate_limiting: >> "config\security.yaml"
    echo   requests_per_minute: 60 >> "config\security.yaml"
    echo   requests_per_hour: 1000 >> "config\security.yaml"
    echo authentication: >> "config\security.yaml"
    echo   max_login_attempts: 5 >> "config\security.yaml"
    echo   lockout_duration: 900 >> "config\security.yaml"
)

echo [INFO] Instalando dependencias de Python...
echo [INFO] Esto puede tomar varios minutos la primera vez...
echo [INFO] Por favor, espera y no cierres esta ventana...
echo.

:: Actualizar pip primero
python -m pip install --upgrade pip --quiet

:: Instalar dependencias con más información
pip install -r src/backend/requirements.txt --no-cache-dir

if errorlevel 1 (
    echo.
    echo ERROR: No se pudieron instalar las dependencias
    echo.
    echo Posibles soluciones:
    echo 1. Verifica tu conexión a internet
    echo 2. Cierra temporalmente tu antivirus
    echo 3. Ejecuta este archivo como administrador
    echo 4. Reinicia tu computadora e intenta de nuevo
    echo.
    pause
    exit /b 1
)

echo [INFO] Dependencias instaladas correctamente

echo [INFO] Iniciando servidor de desarrollo...
echo.
echo 🌐 La aplicación estará disponible en:
echo    - Aplicación: http://127.0.0.1:8000
echo    - Admin: http://127.0.0.1:8000/admin/
echo    - API: http://127.0.0.1:8000/api/
echo    - Docs: http://127.0.0.1:8000/api/docs/
echo.
echo 📱 También accesible desde otros dispositivos en tu red:
echo    - http://127.0.0.1:8000 (localhost)
echo    - http://[tu-ip-local]:8000 (red local)
echo.
echo 👤 Credenciales por defecto:
echo    - Email: admin@duocuc.cl
echo    - Contraseña: admin123
echo.
echo 🔧 Modo desarrollo activado:
echo    - DEBUG=True
echo    - Base de datos: SQLite
echo    - Recarga automática de archivos
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

:: Configurar base de datos y crear usuarios de prueba
echo [INFO] Configurando base de datos...
cd src\backend

:: Ejecutar migraciones
echo [INFO] Aplicando migraciones de base de datos...
python manage.py migrate --run-syncdb

:: Crear superusuario si no existe
echo [INFO] Verificando superusuario...
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@duocuc.cl').exists():
    User.objects.create_superuser('admin', 'admin@duocuc.cl', 'admin123')
    print('Superusuario creado: admin@duocuc.cl / admin123')
else:
    print('Superusuario ya existe')
"

:: Crear usuarios de prueba
echo [INFO] Creando usuarios de prueba...
python create_test_users.py

cd ..\..

:: Abrir navegador automáticamente después de 3 segundos
echo [INFO] Abriendo navegador en 3 segundos...
timeout /t 3 /nobreak >nul
start http://localhost:8000

:: Ejecutar con configuración de desarrollo
set DJANGO_SETTINGS_MODULE=duocpoint.settings.dev
python start.py

echo.
echo [INFO] Servidor de desarrollo detenido
pause
