@echo off
echo ========================================
echo    DuocPoint - Prueba de Login
echo ========================================
echo.

echo [1/3] Verificando servidor...
netstat -an | findstr :8000 >nul
if %errorlevel% neq 0 (
    echo ❌ El servidor no está ejecutándose
    echo 💡 Ejecuta 'iniciar_desarrollo_completo.bat' primero
    pause
    exit /b 1
)
echo ✅ Servidor ejecutándose en puerto 8000
echo.

echo [2/3] Verificando usuarios de prueba...
cd /d "%~dp0src\backend"
python test_login.py
if %errorlevel% neq 0 (
    echo ❌ Error al verificar usuarios
    pause
    exit /b 1
)
echo.

echo [3/3] Abriendo página de login...
echo 🌐 Abriendo http://localhost:8000/login.html en el navegador...
start http://localhost:8000/login.html
echo.

echo ========================================
echo    ✅ Prueba de Login Lista
echo ========================================
echo.
echo 📋 Instrucciones:
echo    1. La página de login se abrió automáticamente
echo    2. Haz clic en cualquier botón de usuario de prueba
echo    3. Haz clic en "Iniciar Sesión"
echo    4. Deberías ser redirigido a la página principal
echo.
echo 🎵 Nota: Los sonidos y animaciones están activos
echo.
pause
