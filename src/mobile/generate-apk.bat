@echo off
echo Generando APK de DuocPoint...

cd android
call gradlew assembleDebug

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ¡APK generada exitosamente!
    echo Ubicación: android\app\build\outputs\apk\debug\app-debug.apk
    echo.
    pause
) else (
    echo.
    echo Error al generar la APK. Verifica que tengas Java y Android SDK instalados.
    echo.
    pause
)

