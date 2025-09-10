@echo off
chcp 65001 >nul
title DuocPoint - Inicio Fácil para Principiantes
color 0A

echo.
echo ============================================================
echo    🚀 DuocPoint - Inicio Fácil para Principiantes
echo    Versión 1.2.0
echo ============================================================
echo.
echo ¡Hola! Este archivo te ayudará a iniciar DuocPoint paso a paso.
echo Si es tu primera vez, sigue las instrucciones que aparecerán.
echo.

:: Verificar Python con mensajes más claros
echo [PASO 1] Verificando si tienes Python instalado...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ❌ PROBLEMA: Python no está instalado en tu computadora
    echo.
    echo 📋 SOLUCIÓN:
    echo 1. Ve a: https://python.org
    echo 2. Haz clic en el botón amarillo "Download Python"
    echo 3. Ejecuta el archivo descargado
    echo 4. IMPORTANTE: Marca la casilla "Add Python to PATH"
    echo 5. Haz clic en "Install Now"
    echo 6. Reinicia tu computadora
    echo 7. Vuelve a ejecutar este archivo
    echo.
    echo ¿Quieres que abra la página de Python automáticamente?
    set /p choice="Escribe 'si' y presiona Enter: "
    if /i "%choice%"=="si" start https://python.org
    pause
    exit /b 1
) else (
    echo ✅ Python está instalado correctamente
)

:: Verificar pip
echo [PASO 2] Verificando pip (instalador de paquetes)...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ PROBLEMA: pip no está disponible
    echo Esto es raro, pero puede solucionarse reinstalando Python
    pause
    exit /b 1
) else (
    echo ✅ pip está disponible
)

:: Verificar conexión a internet
echo [PASO 3] Verificando conexión a internet...
ping -n 1 google.com >nul 2>&1
if errorlevel 1 (
    echo ❌ PROBLEMA: No hay conexión a internet
    echo Necesitas internet para descargar las dependencias
    echo Verifica tu conexión y vuelve a intentar
    pause
    exit /b 1
) else (
    echo ✅ Conexión a internet disponible
)

echo.
echo [PASO 4] Configurando archivos necesarios...

:: Crear archivo .env si no existe
if not exist ".env" (
    echo [INFO] Creando archivo de configuración...
    copy "config_local.env" ".env" >nul 2>&1
)

:: Crear directorio config si no existe
if not exist "config" (
    echo [INFO] Creando directorio de configuración...
    mkdir config >nul 2>&1
)

:: Crear archivo push.yaml si no existe
if not exist "config\push.yaml" (
    echo [INFO] Creando configuración de notificaciones...
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

echo.
echo [PASO 5] Instalando dependencias de Python...
echo.
echo ⚠️  IMPORTANTE: Esto puede tomar varios minutos la primera vez
echo ⚠️  Por favor, NO cierres esta ventana mientras se instala
echo ⚠️  Si tienes antivirus, puede que te pregunte si permitir la instalación
echo.
echo Presiona cualquier tecla para continuar...
pause >nul

:: Actualizar pip primero
echo [INFO] Actualizando pip...
python -m pip install --upgrade pip --quiet

:: Instalar dependencias con información detallada
echo [INFO] Instalando dependencias (esto puede tomar tiempo)...
pip install -r src/backend/requirements.txt --no-cache-dir

if errorlevel 1 (
    echo.
    echo ❌ ERROR: No se pudieron instalar las dependencias
    echo.
    echo 🔧 POSIBLES SOLUCIONES:
    echo 1. Verifica tu conexión a internet
    echo 2. Cierra temporalmente tu antivirus
    echo 3. Ejecuta este archivo como administrador (clic derecho → "Ejecutar como administrador")
    echo 4. Reinicia tu computadora e intenta de nuevo
    echo.
    echo Si el problema persiste, contacta al desarrollador
    pause
    exit /b 1
)

echo.
echo ✅ Dependencias instaladas correctamente

echo.
echo [PASO 6] Configurando base de datos...
cd src\backend

:: Ejecutar migraciones
echo [INFO] Configurando base de datos...
python manage.py migrate --run-syncdb

:: Crear superusuario si no existe
echo [INFO] Verificando usuario administrador...
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@duocuc.cl').exists():
    User.objects.create_superuser('admin', 'admin@duocuc.cl', 'admin123')
    print('✅ Usuario administrador creado: admin@duocuc.cl / admin123')
else:
    print('✅ Usuario administrador ya existe')
"

:: Crear usuarios de prueba
echo [INFO] Creando usuarios de prueba...
python create_test_users.py

cd ..\..

echo.
echo [PASO 7] Iniciando la aplicación...
echo.
echo 🎉 ¡Todo está listo! La aplicación se iniciará ahora
echo.
echo 🌐 La aplicación estará disponible en:
echo    - Página principal: http://localhost:8000
echo    - Login mejorado: http://localhost:8000/login-duoc.html
echo    - Panel admin: http://localhost:8000/admin/
echo.
echo 👤 Credenciales para iniciar sesión:
echo    - Email: admin@duocuc.cl
echo    - Contraseña: admin123
echo.
echo 📱 El navegador se abrirá automáticamente en 5 segundos...
echo.
echo ⚠️  Para detener la aplicación:
echo    1. Ve a esta ventana negra
echo    2. Presiona Ctrl+C
echo    3. Presiona Enter
echo.

:: Abrir navegador automáticamente
timeout /t 5 /nobreak >nul
start http://localhost:8000

:: Ejecutar con configuración de desarrollo
set DJANGO_SETTINGS_MODULE=duocpoint.settings.dev
python start.py

echo.
echo [INFO] Aplicación detenida
echo ¡Gracias por usar DuocPoint!
pause
