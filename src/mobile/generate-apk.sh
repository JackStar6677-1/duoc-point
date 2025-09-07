#!/bin/bash

echo "Generando APK de DuocPoint..."

cd android
./gradlew assembleDebug

if [ $? -eq 0 ]; then
    echo ""
    echo "¡APK generada exitosamente!"
    echo "Ubicación: android/app/build/outputs/apk/debug/app-debug.apk"
    echo ""
else
    echo ""
    echo "Error al generar la APK. Verifica que tengas Java y Android SDK instalados."
    echo ""
fi

