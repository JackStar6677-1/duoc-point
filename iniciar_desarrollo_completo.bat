@echo off
echo ========================================
echo    DuocPoint - Inicio de Desarrollo
echo ========================================
echo.

echo [1/4] Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python no encontrado. Por favor instala Python 3.8+
    pause
    exit /b 1
)
echo ✅ Python encontrado
echo.

echo [2/4] Navegando al directorio del backend...
cd /d "%~dp0src\backend"
if %errorlevel% neq 0 (
    echo ❌ No se pudo acceder al directorio del backend
    pause
    exit /b 1
)
echo ✅ Directorio del backend accedido
echo.

echo [3/4] Aplicando migraciones...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ❌ Error al aplicar migraciones
    pause
    exit /b 1
)
echo ✅ Migraciones aplicadas
echo.

echo [4/4] Creando usuarios de prueba...
python create_test_users.py
if %errorlevel% neq 0 (
    echo ❌ Error al crear usuarios de prueba
    pause
    exit /b 1
)
echo ✅ Usuarios de prueba creados
echo.

echo ========================================
echo    🚀 Iniciando servidor de desarrollo
echo ========================================
echo.
echo 📍 URL: http://localhost:8000
echo 📍 Login: http://localhost:8000/login.html
echo.
echo 👤 Usuarios de prueba:
echo    - estudiante@gmail.com / estudiante123
echo    - moderador@duocuc.cl / moderador123
echo    - admin@duocuc.cl / admin123
echo    - profesor@duocuc.cl / profesor123
echo.
echo 🎨 Página de pruebas: http://localhost:8000/test-animations.html
echo.
echo Presiona Ctrl+C para detener el servidor
echo ========================================
echo.

python manage.py runserver 0.0.0.0:8000
