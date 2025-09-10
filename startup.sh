#!/bin/bash
# DuocPoint - Script de inicio para AMP (CubeCoders)
# Este script configura y inicia DuocPoint en un servidor AMP

echo "============================================================"
echo "    DuocPoint - Iniciando en AMP (CubeCoders)"
echo "    Versión 1.2.0"
echo "============================================================"
echo

# Verificar Python
python3 --version || python --version
if [ $? -ne 0 ]; then
    echo "ERROR: Python no está instalado"
    exit 1
fi

echo "[INFO] Instalando dependencias..."
pip install -r src/backend/requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: No se pudieron instalar las dependencias"
    exit 1
fi

echo "[INFO] Aplicando migraciones de base de datos..."
python src/backend/manage.py migrate --settings=duocpoint.settings.production

echo "[INFO] Recopilando archivos estáticos..."
python src/backend/manage.py collectstatic --settings=duocpoint.settings.production --noinput

echo "[INFO] Verificando superusuario..."
python src/backend/manage.py shell --settings=duocpoint.settings.production -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@duocuc.cl').exists():
    User.objects.create_superuser('admin', 'admin@duocuc.cl', 'admin123')
    print('Superusuario creado: admin@duocuc.cl / admin123')
else:
    print('Superusuario ya existe')
"

echo
echo "============================================================"
echo "[INFO] DuocPoint iniciando en modo producción..."
echo
echo "🌐 La aplicación estará disponible en:"
echo "   - Aplicación: http://localhost:8000"
echo "   - Admin: http://localhost:8000/admin/"
echo "   - API: http://localhost:8000/api/"
echo
echo "👤 Credenciales por defecto:"
echo "   - Email: admin@duocuc.cl"
echo "   - Contraseña: admin123"
echo
echo "🔧 Modo producción activado:"
echo "   - DEBUG=False"
echo "   - Base de datos: PostgreSQL"
echo "   - Servidor: Gunicorn"
echo "============================================================"

# Cambiar al directorio del backend
cd src/backend

# Iniciar con Gunicorn
exec gunicorn --bind 0.0.0.0:8000 --workers 4 --timeout 30 --keep-alive 2 --max-requests 1000 --max-requests-jitter 100 --preload-app duocpoint.wsgi:application
