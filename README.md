# 🎓 DuocPoint

**Plataforma integral para la comunidad estudiantil de Duoc UC**

DuocPoint es una aplicación web progresiva (PWA) que conecta a estudiantes, profesores y personal de Duoc UC a través de foros, mercado de compra/venta, portafolio profesional y recorridos virtuales del campus.

## ✨ Características

- **🔐 Autenticación JWT** - Login seguro con emails @duocuc.cl y @gmail.com
- **💬 Sistema de Foros** - Discusiones con moderación automática y manual
- **🛒 Mercado** - Compra y venta de productos entre estudiantes
- **📁 Portafolio** - Perfil profesional con generación de PDF
- **🏫 Recorridos Virtuales** - Street View personalizado del campus
- **📱 PWA** - Instalable como app nativa en móviles
- **🔧 API REST** - Documentación automática con Swagger

## 🚀 Inicio Rápido

### Prerrequisitos
- Python 3.10+
- Node.js (opcional, para frontend)

### Instalación y Ejecución

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/duoc-point.git
cd duoc-point

# 2. Instalar dependencias
cd server
pip install -r requirements.txt

# 3. Configurar base de datos
python manage.py migrate
python manage.py collectstatic --noinput

# 4. Crear superusuario
python manage.py createsuperuser

# 5. Poblar datos de ejemplo
python manage.py shell -c "
from duocpoint.apps.campuses.models import Sede
from duocpoint.apps.accounts.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

# Crear sede
if not Sede.objects.exists():
    Sede.objects.create(
        nombre='Sede Maipú',
        direccion='Av. Américo Vespucio 1501, Maipú',
        lat=-33.5115,
        lng=-70.7525
    )

# Crear usuarios demo
if not User.objects.filter(email='student@duocuc.cl').exists():
    User.objects.create_user(
        email='student@duocuc.cl',
        password='student123',
        name='Estudiante Demo',
        role='student',
        campus_id=1,
        career='Ingeniería en Informática'
    )

if not User.objects.filter(email='moderator@duocuc.cl').exists():
    User.objects.create_user(
        email='moderator@duocuc.cl',
        password='moderator123',
        name='Moderador Demo',
        role='moderator',
        campus_id=1,
        career='Ingeniería en Informática'
    )
"

# 6. Ejecutar servidor
python manage.py runserver 0.0.0.0:8000
```

### 🌐 Acceso

- **Local**: http://localhost:8000
- **Red local**: http://TU_IP:8000 (para probar PWA en móvil)

### 👥 Usuarios de Prueba

- **Admin**: Tu superusuario creado
- **Estudiante**: `student@duocuc.cl` / `student123`
- **Moderador**: `moderator@duocuc.cl` / `moderator123`

## 🏗️ Despliegue en Producción

### Opción 1: Servidor VPS (DigitalOcean, AWS, etc.)

```bash
# 1. En el servidor
sudo apt update && sudo apt install python3-pip nginx postgresql
git clone https://github.com/tu-usuario/duoc-point.git
cd duoc-point/server

# 2. Configurar entorno virtual
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Configurar variables de entorno
cp env.example .env
nano .env  # Editar con tus configuraciones

# 4. Configurar base de datos PostgreSQL
sudo -u postgres createdb duocpoint
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser

# 5. Configurar Gunicorn
pip install gunicorn
gunicorn --bind 0.0.0.0:8000 duocpoint.wsgi:application

# 6. Configurar Nginx
sudo nano /etc/nginx/sites-available/duocpoint
```

**Configuración Nginx:**
```nginx
server {
    listen 80;
    server_name tu-dominio.com;

    location /static/ {
        alias /ruta/a/duoc-point/server/staticfiles/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Opción 2: Docker (Recomendado)

```bash
# 1. Configurar variables de entorno
cp env.example .env
nano .env

# 2. Desplegar con Docker Compose
docker-compose -f docker-compose.prod.yml up -d

# 3. Verificar estado
docker-compose -f docker-compose.prod.yml ps
```

### Opción 3: Servicio en la Nube

**Railway, Render, Heroku:**
1. Conectar repositorio GitHub
2. Configurar variables de entorno
3. Desplegar automáticamente

## 🔧 Configuración

### Variables de Entorno (.env)

```env
# Base de datos
DB_ENGINE=django.db.backends.postgresql
DB_NAME=duocpoint
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=5432

# Django
SECRET_KEY=tu-secret-key-super-segura
DEBUG=0
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com

# Email (opcional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=tu-email@gmail.com
EMAIL_HOST_PASSWORD=tu-app-password
```

## 📱 PWA - Instalación en Móvil

1. **Abrir en Chrome móvil**: http://tu-servidor.com
2. **Tocar "Instalar App"** en la barra superior
3. **Confirmar instalación** - La app aparecerá en el escritorio
4. **Usar como app nativa** - Funciona offline parcialmente

## 🛠️ Comandos Útiles

```bash
# Desarrollo
python manage.py runserver                    # Servidor desarrollo
python manage.py migrate                      # Aplicar migraciones
python manage.py collectstatic                # Recopilar archivos estáticos
python manage.py createsuperuser              # Crear admin
python manage.py shell                        # Consola Django

# Producción
gunicorn duocpoint.wsgi:application          # Servidor producción
docker-compose -f docker-compose.prod.yml up # Docker producción

# Testing
python manage.py test                         # Ejecutar tests
python run_tests.py                          # Tests completos
```

## 📊 Monitoreo

- **Health Check**: http://tu-servidor.com/health/
- **API Docs**: http://tu-servidor.com/api/docs/
- **Admin Panel**: http://tu-servidor.com/admin/

## 🆘 Solución de Problemas

### Error CSRF
```bash
# Verificar configuración CORS
python manage.py check
```

### PWA no funciona
- Verificar HTTPS en producción
- Comprobar manifest.json
- Revisar Service Worker en DevTools

### Base de datos
```bash
# Resetear base de datos
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 📞 Soporte

- **Issues**: [GitHub Issues](https://github.com/tu-usuario/duoc-point/issues)
- **Documentación**: [Wiki del proyecto](https://github.com/tu-usuario/duoc-point/wiki)

---

**Desarrollado con ❤️ para la comunidad Duoc UC**