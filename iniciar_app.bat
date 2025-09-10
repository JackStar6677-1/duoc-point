@echo off
chcp 65001 >nul
title DuocPoint - Iniciar Aplicación Completa
color 0A

echo.
echo ============================================================
echo    🚀 DuocPoint - Iniciar Aplicación Completa
echo    Versión 1.2.0
echo ============================================================
echo.
echo Este archivo iniciará DuocPoint completamente:
echo - Instalará dependencias si es necesario
echo - Configurará la base de datos
echo - Creará usuarios de prueba
echo - Iniciará el servidor
echo - Abrirá el navegador automáticamente
echo.

:: Verificar Python
echo [PASO 1] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python no está instalado
    echo.
    echo SOLUCIÓN:
    echo 1. Ve a: https://python.org
    echo 2. Descarga Python (versión 3.8 o superior)
    echo 3. IMPORTANTE: Marca "Add Python to PATH" durante la instalación
    echo 4. Reinicia tu computadora
    echo 5. Vuelve a ejecutar este archivo
    echo.
    set /p choice="¿Quieres que abra la página de Python? (si/no): "
    if /i "%choice%"=="si" start https://python.org
    pause
    exit /b 1
) else (
    echo ✅ Python está instalado
)

:: Verificar pip
echo [PASO 2] Verificando pip...
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: pip no está disponible
    echo Reinstala Python marcando "Add Python to PATH"
    pause
    exit /b 1
) else (
    echo ✅ pip está disponible
)

:: Verificar conexión a internet
echo [PASO 3] Verificando conexión a internet...
ping -n 1 google.com >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: No hay conexión a internet
    echo Necesitas internet para descargar dependencias
    pause
    exit /b 1
) else (
    echo ✅ Conexión a internet disponible
)

echo.
echo [PASO 4] Configurando archivos del sistema...

:: Crear archivo .env si no existe
if not exist ".env" (
    echo [INFO] Creando archivo de configuración...
    if exist "config_local.env" (
        copy "config_local.env" ".env" >nul 2>&1
    ) else (
        echo DEBUG=True > .env
        echo SECRET_KEY=dev-secret-key-change-in-production >> .env
        echo DATABASE_URL=sqlite:///db.sqlite3 >> .env
    )
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

echo.
echo [PASO 5] Instalando dependencias de Python...
echo [INFO] Esto puede tomar varios minutos la primera vez...
echo.

:: Actualizar pip
echo [INFO] Actualizando pip...
python -m pip install --upgrade pip --quiet

:: Instalar dependencias
echo [INFO] Instalando dependencias...
pip install -r src/backend/requirements.txt --no-cache-dir

if errorlevel 1 (
    echo.
    echo ❌ ERROR: No se pudieron instalar las dependencias
    echo.
    echo SOLUCIONES:
    echo 1. Verifica tu conexión a internet
    echo 2. Cierra temporalmente tu antivirus
    echo 3. Ejecuta este archivo como administrador
    echo 4. Reinicia tu computadora e intenta de nuevo
    echo.
    pause
    exit /b 1
)

echo ✅ Dependencias instaladas correctamente

echo.
echo [PASO 6] Configurando base de datos...
cd src\backend

:: Ejecutar migraciones
echo [INFO] Aplicando migraciones de base de datos...
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
echo [PASO 7] Iniciando servidor de desarrollo...
echo.
echo 🎉 ¡Todo está listo! Iniciando la aplicación...
echo.
echo 🌐 La aplicación estará disponible en:
echo    - Página principal: http://localhost:8000
echo    - Login mejorado: http://localhost:8000/login-duoc.html
echo    - Panel admin: http://localhost:8000/admin/
echo    - API REST: http://localhost:8000/api/
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
echo 🔧 Modo desarrollo activado:
echo    - DEBUG=True
echo    - Base de datos: SQLite
echo    - Recarga automática de archivos
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
