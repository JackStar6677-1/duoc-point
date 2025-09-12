@echo off
title StudentsPoint - Desarrollo

echo ============================================================
echo    StudentsPoint - Modo Desarrollo
echo ============================================================
echo.

echo Verificando Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no encontrado
    pause
    exit /b 1
)

echo Navegando al directorio backend...
cd proyecto\src\backend

echo Verificando Django...
python manage.py check
if errorlevel 1 (
    echo ERROR: Problema con Django
    pause
    exit /b 1
)

echo Aplicando migraciones...
python manage.py migrate --run-syncdb

echo Creando superusuario...
python ensure_superuser.py

echo.
echo ============================================================
echo    SERVIDOR LISTO
echo ============================================================
echo.
echo Aplicacion: http://127.0.0.1:8000
echo Admin: http://127.0.0.1:8000/admin/
echo.
echo Credenciales:
echo Email: admin@studentspoint.app
echo Password: admin123
echo.
echo Presiona Ctrl+C para detener
echo.

timeout /t 3 /nobreak >nul
start http://127.0.0.1:8000

echo Iniciando servidor...
python manage.py runserver 127.0.0.1:8000

echo.
echo Servidor detenido
pause