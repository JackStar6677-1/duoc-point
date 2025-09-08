@echo off
chcp 65001 >nul
title DuocPoint - Modo Producción

echo.
echo ============================================================
echo    DuocPoint - Modo Producción
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

echo [INFO] Configurando entorno de producción...

:: Verificar archivo .env de producción
if not exist ".env" (
    echo ERROR: No se encontró archivo .env
    echo Crea un archivo .env con la configuración de producción
    echo Puedes usar env.example como base
    pause
    exit /b 1
)

:: Crear directorio config si no existe
if not exist "config" (
    echo [INFO] Creando directorio de configuración...
    mkdir config >nul 2>&1
)

:: Verificar archivo push.yaml
if not exist "config\push.yaml" (
    echo ERROR: No se encontró config\push.yaml
    echo Configura las claves VAPID para notificaciones push
    pause
    exit /b 1
)

echo [INFO] Instalando dependencias de producción...
pip install -r src/backend/requirements.txt --quiet

if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

echo [INFO] Verificando configuración de producción...

:: Verificar variables de entorno críticas
if "%SECRET_KEY%"=="" (
    echo ADVERTENCIA: SECRET_KEY no está configurado
    echo Usando clave por defecto (NO RECOMENDADO PARA PRODUCCIÓN)
)

if "%DEBUG%"=="1" (
    echo ADVERTENCIA: DEBUG está habilitado en producción
    echo Considera deshabilitar DEBUG para mejor seguridad
)

echo [INFO] Iniciando servidor de producción...
echo.
echo 🌐 La aplicación estará disponible en:
echo    - Aplicación: http://localhost:8000
echo    - Admin: http://localhost:8000/admin/
echo    - API: http://localhost:8000/api/
echo.
echo 🔒 Modo producción activado:
echo    - DEBUG=False (si está configurado)
echo    - Base de datos: PostgreSQL (recomendado)
echo    - Configuración de seguridad habilitada
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

:: Ejecutar con configuración de producción
set DJANGO_SETTINGS_MODULE=duocpoint.settings.prod
python start.py

echo.
echo [INFO] Servidor de producción detenido
pause
