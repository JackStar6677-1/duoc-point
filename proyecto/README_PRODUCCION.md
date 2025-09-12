# DuocPoint - Guía de Producción

Esta guía te ayudará a desplegar DuocPoint en un entorno de producción usando PostgreSQL.

## Requisitos del Sistema

### Software Requerido
- **Python 3.8+** - Lenguaje de programación
- **PostgreSQL 12+** - Base de datos de producción
- **Node.js 16+** (opcional) - Para herramientas de frontend
- **Git** - Control de versiones

### Hardware Mínimo
- **RAM**: 4GB mínimo, 8GB recomendado
- **Almacenamiento**: 10GB libres
- **CPU**: 2 cores mínimo

## Instalación Rápida

### 1. Clonar el Repositorio
```bash
git clone https://github.com/JackStar6677-1/duoc-point.git
cd duoc-point
git checkout production
```

### 2. Instalar PostgreSQL
```bash
# Windows
instalar_postgresql.bat

# Linux/macOS
sudo apt-get install postgresql postgresql-contrib  # Ubuntu/Debian
brew install postgresql  # macOS
```

### 3. Configurar Variables de Entorno
```bash
# Copiar archivo de ejemplo
cp env.production.example .env

# Editar configuración
nano .env  # o tu editor preferido
```

### 4. Configuración Mínima en .env
```env
# Base de datos
DB_NAME=duocpoint_prod
DB_USER=postgres
DB_PASSWORD=tu_password_aqui
DB_HOST=localhost
DB_PORT=5432

# Django
DEBUG=False
SECRET_KEY=tu_secret_key_muy_segura_aqui
ALLOWED_HOSTS=localhost,127.0.0.1,tu-dominio.com
```

### 5. Iniciar Producción
```bash
# Windows
iniciar_produccion.bat

# Linux/macOS
python src/backend/manage.py migrate --settings=duocpoint.settings.production
python src/backend/manage.py collectstatic --settings=duocpoint.settings.production
python src/backend/manage.py runserver 0.0.0.0:8000 --settings=duocpoint.settings.production
```

## Configuración Avanzada

### Base de Datos PostgreSQL

#### Crear Base de Datos
```sql
-- Conectar como superusuario
psql -U postgres

-- Crear base de datos
CREATE DATABASE duocpoint_prod;

-- Crear usuario específico (opcional)
CREATE USER duocpoint_user WITH PASSWORD 'password_segura';
GRANT ALL PRIVILEGES ON DATABASE duocpoint_prod TO duocpoint_user;
```

#### Configuración de PostgreSQL
```bash
# Editar postgresql.conf
sudo nano /etc/postgresql/12/main/postgresql.conf

# Configuraciones recomendadas:
# shared_buffers = 256MB
# effective_cache_size = 1GB
# maintenance_work_mem = 64MB
# checkpoint_completion_target = 0.9
# wal_buffers = 16MB
# default_statistics_target = 100
```

### Servidor Web (Nginx + Gunicorn)

#### Instalar Gunicorn
```bash
pip install gunicorn
```

#### Configuración de Gunicorn
```bash
# Crear archivo gunicorn.conf.py
cat > gunicorn.conf.py << EOF
bind = "127.0.0.1:8000"
workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 100
preload_app = True
EOF
```

#### Configuración de Nginx
```nginx
# /etc/nginx/sites-available/duocpoint
server {
    listen 80;
    server_name tu-dominio.com;

    location /static/ {
        alias /ruta/a/duocpoint/src/backend/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /ruta/a/duocpoint/src/backend/media/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### SSL/HTTPS (Let's Encrypt)
```bash
# Instalar Certbot
sudo apt-get install certbot python3-certbot-nginx

# Obtener certificado
sudo certbot --nginx -d tu-dominio.com

# Renovación automática
sudo crontab -e
# Agregar: 0 12 * * * /usr/bin/certbot renew --quiet
```

## Monitoreo y Logs

### Configuración de Logs
```python
# En settings/production.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/duocpoint/django.log',
            'maxBytes': 15728640,  # 15MB
            'backupCount': 10,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### Monitoreo del Sistema
```bash
# Crear script de monitoreo
cat > monitor.sh << EOF
#!/bin/bash
# Verificar estado de PostgreSQL
systemctl is-active postgresql

# Verificar estado de Nginx
systemctl is-active nginx

# Verificar uso de memoria
free -h

# Verificar espacio en disco
df -h

# Verificar logs de errores
tail -n 50 /var/log/duocpoint/django.log
EOF

chmod +x monitor.sh
```

## Backup y Restauración

### Backup de Base de Datos
```bash
# Backup completo
pg_dump -U postgres -h localhost duocpoint_prod > backup_$(date +%Y%m%d_%H%M%S).sql

# Backup solo datos
pg_dump -U postgres -h localhost --data-only duocpoint_prod > data_backup.sql

# Backup solo estructura
pg_dump -U postgres -h localhost --schema-only duocpoint_prod > schema_backup.sql
```

### Restauración
```bash
# Restaurar backup completo
psql -U postgres -h localhost duocpoint_prod < backup_20240101_120000.sql

# Restaurar solo datos
psql -U postgres -h localhost duocpoint_prod < data_backup.sql
```

### Backup Automático
```bash
# Crear script de backup
cat > backup.sh << EOF
#!/bin/bash
BACKUP_DIR="/var/backups/duocpoint"
DATE=$(date +%Y%m%d_%H%M%S)
pg_dump -U postgres -h localhost duocpoint_prod > $BACKUP_DIR/backup_$DATE.sql
find $BACKUP_DIR -name "backup_*.sql" -mtime +7 -delete
EOF

# Programar en crontab
crontab -e
# Agregar: 0 2 * * * /ruta/a/backup.sh
```

## Actualizaciones

### Actualizar Código
```bash
# Hacer backup antes de actualizar
./backup.sh

# Actualizar código
git pull origin production

# Aplicar migraciones
python src/backend/manage.py migrate --settings=duocpoint.settings.production

# Recopilar archivos estáticos
python src/backend/manage.py collectstatic --settings=duocpoint.settings.production

# Reiniciar servicios
sudo systemctl restart nginx
sudo systemctl restart gunicorn
```

## Troubleshooting

### Problemas Comunes

#### Error de Conexión a PostgreSQL
```bash
# Verificar estado del servicio
sudo systemctl status postgresql

# Verificar configuración
sudo nano /etc/postgresql/12/main/postgresql.conf
sudo nano /etc/postgresql/12/main/pg_hba.conf

# Reiniciar servicio
sudo systemctl restart postgresql
```

#### Error de Permisos de Archivos
```bash
# Corregir permisos
sudo chown -R www-data:www-data /ruta/a/duocpoint/
sudo chmod -R 755 /ruta/a/duocpoint/
```

#### Error de Memoria
```bash
# Verificar uso de memoria
free -h
htop

# Ajustar configuración de PostgreSQL
sudo nano /etc/postgresql/12/main/postgresql.conf
# shared_buffers = 128MB  # Reducir si es necesario
```

## Seguridad

### Configuración de Firewall
```bash
# UFW (Ubuntu)
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 80/tcp    # HTTP
sudo ufw allow 443/tcp   # HTTPS
sudo ufw enable
```

### Configuración de Django
```python
# En settings/production.py
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
```

## Soporte

Para soporte técnico:
- **Documentación**: README.md
- **Issues**: GitHub Issues
- **Email**: soporte@duocpoint.com

## Licencia

Este proyecto está bajo la Licencia MIT. Ver LICENSE para más detalles.
