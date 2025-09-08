@echo off
chcp 65001 >nul
title DuocPoint - Configuración de Aplicación Móvil

echo.
echo ============================================================
echo    DuocPoint - Configuración de Aplicación Móvil
echo    Versión 1.2.0
echo ============================================================
echo.

:: Verificar Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js no está instalado
    echo Descarga Node.js desde: https://nodejs.org
    pause
    exit /b 1
)

echo [INFO] Node.js detectado correctamente
echo.

:: Navegar al directorio frontend
cd src\frontend

:: Instalar Capacitor CLI globalmente
echo [INFO] Instalando Capacitor CLI...
npm install -g @capacitor/cli

:: Inicializar Capacitor
echo [INFO] Inicializando Capacitor...
npx cap init DuocPoint com.duocuc.duocpoint --web-dir=../

:: Instalar plugins necesarios
echo [INFO] Instalando plugins de Capacitor...
npm install @capacitor/core @capacitor/cli @capacitor/android
npm install @capacitor/status-bar @capacitor/splash-screen @capacitor/network @capacitor/push-notifications

:: Agregar plataforma Android
echo [INFO] Agregando plataforma Android...
npx cap add android

:: Crear archivo de configuración
echo [INFO] Creando configuración de Capacitor...
(
echo import { CapacitorConfig } from '@capacitor/cli';
echo.
echo const config: CapacitorConfig = {
echo   appId: 'com.duocuc.duocpoint',
echo   appName: 'DuocPoint',
echo   webDir: '../',
echo   server: {
echo     androidScheme: 'https'
echo   },
echo   plugins: {
echo     SplashScreen: {
echo       launchShowDuration: 2000,
echo       backgroundColor: "#4A148C",
echo       showSpinner: true,
echo       spinnerColor: "#D4AF37"
echo     },
echo     StatusBar: {
echo       style: 'dark',
echo       backgroundColor: "#4A148C"
echo     }
echo   }
echo };
echo.
echo export default config;
) > capacitor.config.ts

:: Sincronizar archivos
echo [INFO] Sincronizando archivos...
npx cap sync

:: Crear script de build
echo [INFO] Creando script de build...
(
echo @echo off
echo echo Construyendo DuocPoint Mobile...
echo cd src\frontend
echo npx cap sync
echo npx cap build android
echo echo Build completado!
echo pause
) > ..\..\build-mobile.bat

:: Crear script de ejecución
echo [INFO] Creando script de ejecución...
(
echo @echo off
echo echo Ejecutando DuocPoint Mobile...
echo cd src\frontend
echo npx cap run android
echo pause
) > ..\..\run-mobile.bat

echo.
echo ============================================================
echo    Configuración Completada
echo ============================================================
echo.
echo ✅ Capacitor instalado y configurado
echo ✅ Plataforma Android agregada
echo ✅ Plugins instalados
echo ✅ Archivos sincronizados
echo.
echo 📱 Para ejecutar la aplicación móvil:
echo    1. Ejecuta: run-mobile.bat
echo    2. O abre Android Studio: npx cap open android
echo.
echo 🔧 Para construir APK:
echo    Ejecuta: build-mobile.bat
echo.
echo 📋 Próximos pasos:
echo    1. Instala Android Studio
echo    2. Configura un emulador Android
echo    3. Ejecuta la aplicación
echo.
echo Presiona cualquier tecla para continuar...
pause >nul
