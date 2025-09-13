@echo off
echo ========================================
echo    StudentsPoint - Modo Produccion
echo ========================================
echo.

echo Configurando entorno de produccion...
echo.

echo [1/6] Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python no encontrado. Instala Python 3.11+
    pause
    exit /b 1
)

echo [2/6] Instalando dependencias...
pip install -r proyecto/src/backend/requirements.txt

echo [3/6] Configurando variables de entorno...
if not exist "proyecto/src/backend/.env" (
    echo Copiando configuracion de produccion...
    copy "proyecto/src/backend/env.production.example" "proyecto/src/backend/.env"
    echo.
    echo IMPORTANTE: Edita el archivo .env con tus configuraciones reales
    echo - Cambia SECRET_KEY por una clave segura
    echo - Configura tu dominio en ALLOWED_HOSTS
    echo - Verifica la configuracion de PostgreSQL
    echo.
    pause
)

echo [4/6] Verificando conexion a PostgreSQL...
echo Intentando conectar a PostgreSQL...
python -c "import psycopg2; conn = psycopg2.connect(host='localhost', port=5432, user='postgres', password='214526867', database='postgres'); print('Conexion exitosa a PostgreSQL'); conn.close()"
if %errorlevel% neq 0 (
    echo ERROR: No se puede conectar a PostgreSQL
    echo Verifica que PostgreSQL este ejecutandose en puerto 5432
    echo Usuario: postgres, Password: 214526867
    pause
    exit /b 1
)

echo [5/6] Aplicando migraciones...
cd proyecto/src/backend
python manage.py migrate --settings=studentspoint.settings.prod

echo [6/6] Recolectando archivos estaticos...
python manage.py collectstatic --noinput --settings=studentspoint.settings.prod

echo.
echo ========================================
echo    StudentsPoint - Produccion Lista
echo ========================================
echo.
echo URLs de acceso:
echo - Aplicacion: https://studentspoint.app
echo - Admin: https://studentspoint.app/admin/
echo - API Docs: https://studentspoint.app/api/docs/
echo.
echo Credenciales por defecto:
echo - Email: admin@studentspoint.app
echo - Password: admin123
echo.
echo Base de datos: PostgreSQL (puerto 5432)
echo Archivos estaticos: /var/www/studentspoint/staticfiles/
echo.
echo Para iniciar el servidor:
echo python manage.py runserver 0.0.0.0:8000 --settings=studentspoint.settings.prod
echo.
pause