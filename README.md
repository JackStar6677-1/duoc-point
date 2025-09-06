# Duoc-Point — Plataforma Completa para la Comunidad Duoc UC

## Qué es

Plataforma web **cerrada** para la comunidad de **Duoc UC**, hecha como **PWA** (se puede "instalar" en el celular) y web tradicional. El acceso es **exclusivo con correos `@duocuc.cl` y `@gmail.com`** (para estudiantes sin correo institucional). La idea es centralizar lo que el estudiante necesita día a día: orientación en la sede, comunicación por carrera, recordatorios, bienestar, reportes, compra/venta segura y portafolio automático.

## Enfoque

* 🎯 **MVP útil en la vida real** del estudiante.
* 🔒 **Comunidad privada** (solo Duoc).
* 📱 **Una sola base web + PWA**: usable en PC y móvil.
* 🤝 **Por sedes y por carreras**: cada sede tiene su espacio; cada carrera su “Point”.
* 🤖 **Moderación automática** para mantener el espacio sano.
* ⚙️ **Escalable**: backend Django + API REST compartida.

---

## Funcionalidades (MVP)

### 1) Mapa y recorrido virtual

* Mapa por sede con **Leaflet**.
* **Recorridos fotográficos en slides**: desde la entrada hasta salas y servicios clave.

### 2) Foro por carrera (tipo Reddit, texto)

* Subforos: *Informática Point, Arquitectura Point*, etc.
* Posts de texto, comentarios en hilo, **votos ↑↓**.
* **Moderación automática** (filtros de spam/toxicidad) y descargo de responsabilidad.
* Encuestas integradas (ver #8).

### 3) Notificaciones de clases

* Carga de **horarios** por el estudiante.
* **Recordatorio 20 min antes** vía **Web Push** (PWA) y preparado para FCM.
* Programación con **Celery** (backend).

### 4) Cursos abiertos (sin certificado)

* Catálogo donde estudiantes/profesores/directores **publican cursos** (SQL, BD, leyes básicas, etc.).
* Disponibles **por tiempo limitado**, solo para aprendizaje.

### 5) Bienestar por carrera

* **Kinesiología**: estiramientos/masajes según riesgos de cada carrera (p. ej., informáticos → muñecas/túnel carpiano).
* **Psicológico**: hábitos de sueño, manejo de estrés, pautas simples.
* Material en texto + imágenes/videos cortos.

### 6) Reportes de infraestructura

* Reportar **fallas** (mobiliario, grietas, talleres).
* Categoría + descripción + **ubicación en mapa** + fotos.
* Flujo de estados: **Abierto → En revisión → Resuelto** para transparencia.

### 7) Compra/Venta segura ✅ **COMPLETO**

* Publicación de **links** (FB Marketplace, Yapo, MercadoLibre).
* **Previsualización OpenGraph** automática.
* Sistema de favoritos y reportes.
* Analytics de productos y clicks.
* Categorización y filtros avanzados.

### 8) Votaciones y encuestas ✅ **COMPLETO**

* Creación por **moderadores/directores** o roles con permiso.
* Útiles para priorizar mejoras e **insights por sede/carrera**.
* Opción de ver resultados al cierre o en vivo.
* Sistema completo con gráficos y exportación CSV.

### 9) Portafolio automático ✅ **COMPLETO**

* Genera **CV/portafolio PDF** profesional con WeasyPrint.
* Gestión completa de logros, proyectos, experiencia y habilidades.
* Sugerencias automáticas para mejorar el portafolio.
* Analytics de completitud y visualizaciones.

---

## Integraciones clave

* **Google OAuth** restringido a `@duocuc.cl` y `@gmail.com`.
* **PWA**: manifest, service worker y soporte offline básico.
* **Notificaciones**: Web Push (VAPID) + FCM.
* **OpenGraph** para previsualizar enlaces en compra/venta.
* **Google Street View** para imágenes de recorridos.
* **WeasyPrint** para generación de PDFs de portafolio.

---

## Arquitectura y stack

* **Backend**: Django + DRF, Celery, Redis.
* **DB**: PostgreSQL (prod) / SQLite (dev).
* **Frontend**: HTML/CSS/JS + Bootstrap 5, Leaflet, PWA.
* **Almacenamiento**: local en dev; S3/MinIO en prod.
* **Tiempo real (futuro)**: Django Channels.

---

## Seguridad y moderación

* Acceso solo `@duocuc.cl` y `@gmail.com` (estudiantes).
* Moderación automática con filtros de contenido.
* Descargo legal visible.
* Roles: estudiante, moderador, director de carrera, staff sede, admin.
* Autenticación JWT con Google OAuth.

---

## Organización por sedes y carreras

* Subespacios por **sede** (ej. Duoc-Point Maipú).
* Dentro de cada sede, subforos por **carrera**.
* Métricas/votos/reportes **segmentados** por sede.

---

## Roadmap corto (curso, ~3 meses)

1. **Base**: auth dominio, PWA mínima, sedes+mapa, foros texto.
2. **Productividad**: horarios + push 20 min; reportes con fotos/estados.
3. **Contenido**: cursos abiertos, bienestar, encuestas.
4. **Salida**: portafolio PDF + pulido y demo.

---

## Qué NO incluye en el MVP

* Carga masiva de media de usuarios en foros.
* Buscador semántico/ML avanzado.
* Modo anónimo “duro”.

---

## Valor para la comunidad

* 📌 Orientación más rápida y menos ansiedad para estudiantes nuevos.
* 💬 Comunidad por carrera en un entorno moderado.
* ⏰ Recordatorios útiles para la puntualidad y organización.
* 🛠️ Reportes visibles que empujan mejoras reales en la sede.
* 🧠 Bienestar y hábitos saludables ligados al contexto de cada carrera.
* 🎓 Portafolio listo para prácticas/empleo con minimum effort.

---

# Duoc-Point

Plataforma académica **MVP** para la comunidad de **Duoc UC**. Requiere correos `@duocuc.cl` y funciona como sitio web tradicional o como **PWA instalable** con soporte de notificaciones push.

---

## Inicio rápido (sin Docker)

Para probar el proyecto sin contenedores, asegúrate de tener **Python 3** y **pip**. Luego ejecuta:

### Windows (PowerShell)

```powershell
./run_local.ps1
```

### Linux/macOS

```bash
./run_local.sh
```

Los scripts crean un entorno virtual `.venv`, instalan las dependencias, aplican migraciones sobre SQLite y levantan el servidor en `http://localhost:8000`. Se habilita automáticamente un **modo demo** (`DEMO_MODE=1`) que desactiva la autenticación de la API para poder explorarla sin credenciales.

Funcionalidades que dependen de servicios externos (OAuth, Web Push, mapas con claves privadas, etc.) están deshabilitadas o usan valores de ejemplo para que el arranque local no requiera configuraciones adicionales. **No necesitas APIs ni servicios de pago** para ejecutar el proyecto en tu máquina.

El script también carga las variables de `infra/.env.example` (se copia automáticamente a `infra/.env`) y se apoya en `config/push.yaml`, que ya incluye claves VAPID de desarrollo para las notificaciones Web Push. Para producción, reemplaza estas claves y ajustes por valores propios.

### Pasos manuales

Si prefieres ejecutar los comandos uno a uno (por ejemplo, para entender cada paso), puedes usar estas instrucciones básicas:

```powershell
# 1. Crear y activar entorno virtual
python -m venv .venv
. .\.venv\Scripts\Activate.ps1

# 2. Instalar dependencias
pip install -r server/requirements.txt

# 3. Copiar variables de ejemplo
Copy-Item "infra/.env.example" "infra/.env"

# 4. Ejecutar migraciones y crear usuario admin
python server/manage.py migrate --noinput
$env:DJANGO_SUPERUSER_USERNAME="pa.avendano@duocuc.cl"
$env:DJANGO_SUPERUSER_PASSWORD="admin123"
$env:DJANGO_SUPERUSER_EMAIL="pa.avendano@duocuc.cl"
try { python server/manage.py createsuperuser --noinput | Out-Null } catch {}

# 5. Levantar el servidor
python server/manage.py runserver 8000
```

Usuario por defecto para entrar al panel de administración (`/admin/`):

* **Usuario**: `pa.avendano@duocuc.cl`
* **Contraseña**: `admin123`

URLs útiles tras el arranque:

* `http://localhost:8000/` – página inicial estática.
* `http://localhost:8000/horarios/` – ejemplo de vista estática adicional.
* `http://localhost:8000/admin/` – administración de Django.
* `http://localhost:8000/api/` – raíz de la API.
* `http://localhost:8000/api/docs/` – documentación interactiva.

---

## Inicio con Docker

Requiere **Docker**, **Docker Compose** y **GNU Make**. Se usa para replicar los servicios que la app empleará en producción (PostgreSQL, Redis, MinIO y un servidor de correo de pruebas) sin instalarlos manualmente, manteniendo un entorno consistente y listo para escalar. Desde la carpeta `infra`:

```bash
cp .env.example .env        # opcional: ajustar variables
make up                     # levanta postgres, redis, minio, mailhog, backend y nginx
make migrate                # aplica migraciones
make createsuperuser        # opcional
```

La aplicación queda disponible en `http://localhost:8000`. Para detener los servicios:

```bash
make down
```

---

## Tests

```bash
make test                    # con Docker
# o sin Docker
python server/manage.py test
```

---

## Stack y origen

Este proyecto se levantó desde una plantilla mínima de **Django 5** y se fue extendiendo con las siguientes herramientas:

- **Django REST Framework** para la API.
- **SimpleJWT** para la autenticación por tokens.
- **Celery + Redis** para tareas en segundo plano y notificaciones.
- **PyPDF2** para leer horarios desde PDF.
- **PyWebPush** para enviar notificaciones web.
- **WeasyPrint** para generar el PDF de portafolio.
- **PWA ligera** en JavaScript (manifest y service-worker).

El código está pensado como base académica; se puede adaptar o escalar según los requerimientos del proyecto final.

### Ajustes antes de desplegar

- Reemplazar las claves y URLs de ejemplo en `.env` y `config/*.yaml`.
- Desactivar `DEBUG` y ajustar `ALLOWED_HOSTS`/`CORS_ALLOWED_ORIGINS` para el entorno de despliegue.
- Revisar branding e íconos en `web/` para que reflejen el proyecto final.
- Configurar almacenamiento externo y logging si se publicará fuera del entorno local.

---

## Módulos incluidos

- **Accounts** – usuario extendido, login JWT y endpoint `/api/me`.
- **Campuses** – sedes y recorridos fotográficos para un mapa con Leaflet.
- **Forum** – foros por carrera, posts, comentarios, votos y moderación básica.
- **Polls** – encuestas ligadas a posts.
- **Schedules/Notifications** – importación de horarios desde PDF y alertas push 20 minutos antes de cada clase.
- **Reports** – reportes de infraestructura con fotos y flujo de estados.
- **OTEC** – publicación de cursos abiertos sin certificación.
- **Wellbeing** – recursos de bienestar por carrera con contenido Markdown.
- **Portfolio** – generador de PDF con datos del usuario.
- **PWA** – `manifest.webmanifest` y `service-worker.js` con caché y push.

---
## Importar horarios por PDF

1. Enviar `POST /api/horarios/import/pdf` con un PDF que contenga texto embebido.
2. Consultar el progreso en `GET /api/horarios/import/{id}`.
3. Los bloques generados se administran via `/api/horarios`.

**Configuración:**

- `config/security.yaml` controla tamaño máximo y extensiones permitidas.
- Coloca claves VAPID en `config/push.yaml` para habilitar las notificaciones web.  Puedes generarlas con `pywebpush`:

  ```bash
  python - <<'PY'
  from py_vapid import Vapid
  v = Vapid(); v.generate_keys()
  print(v.public_key, v.private_key)
  PY
  ```

---

## Opcional / Extensible

- **OCR para PDFs escaneados:** agregar `pytesseract` y `pdf2image` y ampliar `schedules.tasks.parse_schedule_pdf`.
- **PWA:** cambiar colores e íconos en `web/manifest.webmanifest` y el caché en `web/service-worker.js`.
- **Almacenamiento:** editar `config/storage.yaml` para usar S3/MinIO.
- **Throttling, CORS y límites de subida:** configurar en `.env` y `config/security.yaml`.
- **Exportar esquema OpenAPI:**

  ```bash
  python server/manage.py spectacular --file docs/api-openapi.yaml
  ```

---

---

## 🚀 Deployment y Configuración de Producción

### Requisitos Previos

- **Python 3.11+**
- **Node.js 18+** (para utilidades de desarrollo)
- **PostgreSQL 13+** (producción)
- **Redis 6+** (para Celery)
- **Docker y Docker Compose** (recomendado)

### Variables de Entorno Requeridas

Crear archivo `.env` en la raíz del proyecto:

```bash
# === CONFIGURACIÓN BÁSICA ===
DEBUG=0
SECRET_KEY=tu-clave-secreta-super-segura-aqui
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com
CORS_ALLOWED_ORIGINS=https://tu-dominio.com

# === BASE DE DATOS ===
DB_ENGINE=django.db.backends.postgresql
DB_NAME=duocpoint_prod
DB_USER=duocpoint_user
DB_PASSWORD=tu-password-seguro
DB_HOST=localhost
DB_PORT=5432

# === GOOGLE OAUTH ===
GOOGLE_OAUTH_CLIENT_ID=tu-google-client-id.apps.googleusercontent.com

# === GOOGLE MAPS/STREET VIEW ===
GOOGLE_MAPS_API_KEY=tu-google-maps-api-key

# === CELERY/REDIS ===
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# === ALMACENAMIENTO (OPCIONAL) ===
# Para usar S3 en lugar de almacenamiento local
AWS_ACCESS_KEY_ID=tu-access-key
AWS_SECRET_ACCESS_KEY=tu-secret-key
AWS_STORAGE_BUCKET_NAME=tu-bucket
AWS_S3_REGION_NAME=us-east-1
```

### Configuración de Google OAuth

1. **Crear proyecto en Google Cloud Console**:
   - Ir a [Google Cloud Console](https://console.cloud.google.com/)
   - Crear nuevo proyecto o seleccionar existente
   - Habilitar Google+ API

2. **Configurar OAuth 2.0**:
   - Ir a "Credenciales" → "Crear credenciales" → "ID de cliente OAuth 2.0"
   - Tipo: Aplicación web
   - Orígenes autorizados: `https://tu-dominio.com`
   - URIs de redirección: `https://tu-dominio.com/api/auth/google/callback`

3. **Configurar dominios permitidos**:
   - En "Pantalla de consentimiento OAuth"
   - Agregar `duocuc.cl` y `gmail.com` como dominios autorizados

### Configuración de Google Maps API

1. **Habilitar APIs necesarias**:
   - Maps JavaScript API
   - Street View Static API
   - Geocoding API

2. **Configurar restricciones**:
   - Restringir por HTTP referrer: `https://tu-dominio.com/*`
   - Configurar cuotas para evitar costos excesivos

### Deployment con Docker (Recomendado)

1. **Clonar y configurar**:
```bash
git clone https://github.com/tu-usuario/duoc-point.git
cd duoc-point
cp .env.example .env
# Editar .env con tus valores
```

2. **Levantar servicios**:
```bash
cd infra
make up
```

3. **Aplicar migraciones**:
```bash
make migrate
```

4. **Crear superusuario**:
```bash
make createsuperuser
```

5. **Configurar nginx** (opcional):
```bash
# Editar infra/nginx.conf para tu dominio
make restart
```

### Deployment Manual

1. **Instalar dependencias**:
```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r server/requirements.txt
```

2. **Configurar base de datos**:
```bash
# Crear base de datos PostgreSQL
createdb duocpoint_prod

# Aplicar migraciones
cd server
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser
```

3. **Configurar archivos estáticos**:
```bash
python manage.py collectstatic --noinput
```

4. **Configurar servidor web** (Nginx + Gunicorn):
```bash
# Instalar Gunicorn
pip install gunicorn

# Ejecutar con Gunicorn
gunicorn --bind 0.0.0.0:8000 duocpoint.wsgi:application
```

### Configuración de Nginx

```nginx
server {
    listen 80;
    server_name tu-dominio.com www.tu-dominio.com;
    
    # Redirigir HTTP a HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name tu-dominio.com www.tu-dominio.com;
    
    # Certificados SSL (usar Let's Encrypt)
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/private.key;
    
    # Configuración SSL
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    
    # Archivos estáticos
    location /static/ {
        alias /path/to/duoc-point/server/staticfiles/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
    
    location /media/ {
        alias /path/to/duoc-point/server/media/;
        expires 1y;
        add_header Cache-Control "public";
    }
    
    # API y admin
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /admin/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Frontend SPA
    location / {
        root /path/to/duoc-point/web;
        try_files $uri $uri/ /index.html;
        
        # Headers para PWA
        add_header Cache-Control "no-cache, no-store, must-revalidate";
        add_header Pragma "no-cache";
        add_header Expires "0";
    }
}
```

### Configuración de Celery (Tareas Asíncronas)

1. **Crear archivo de configuración**:
```bash
# /etc/systemd/system/celery-duocpoint.service
[Unit]
Description=Celery Service for DuocPoint
After=network.target

[Service]
Type=forking
User=www-data
Group=www-data
EnvironmentFile=/path/to/duoc-point/.env
WorkingDirectory=/path/to/duoc-point/server
ExecStart=/path/to/duoc-point/venv/bin/celery -A duocpoint worker --loglevel=info --detach
ExecStop=/path/to/duoc-point/venv/bin/celery -A duocpoint control shutdown
Restart=always

[Install]
WantedBy=multi-user.target
```

2. **Activar servicio**:
```bash
sudo systemctl enable celery-duocpoint
sudo systemctl start celery-duocpoint
```

### Monitoreo y Logs

1. **Configurar logs de Django**:
```python
# En settings/prod.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/duocpoint/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

2. **Monitoreo con systemd**:
```bash
# Ver logs de la aplicación
journalctl -u gunicorn-duocpoint -f

# Ver logs de Celery
journalctl -u celery-duocpoint -f
```

### Backup y Mantenimiento

1. **Backup de base de datos**:
```bash
# Backup diario
pg_dump duocpoint_prod > backup_$(date +%Y%m%d).sql

# Restaurar backup
psql duocpoint_prod < backup_20240101.sql
```

2. **Backup de archivos media**:
```bash
# Backup de archivos subidos
tar -czf media_backup_$(date +%Y%m%d).tar.gz /path/to/media/
```

3. **Actualizaciones**:
```bash
# Actualizar código
git pull origin main

# Aplicar migraciones
python manage.py migrate

# Recargar servicios
sudo systemctl reload gunicorn-duocpoint
sudo systemctl restart celery-duocpoint
```

### Checklist de Deployment

- [ ] Variables de entorno configuradas
- [ ] Base de datos PostgreSQL creada
- [ ] Google OAuth configurado
- [ ] Google Maps API configurado
- [ ] Certificados SSL instalados
- [ ] Nginx configurado
- [ ] Gunicorn ejecutándose
- [ ] Celery ejecutándose
- [ ] Archivos estáticos servidos
- [ ] Logs configurados
- [ ] Backup configurado
- [ ] Monitoreo configurado

### Troubleshooting

**Error de migraciones**:
```bash
python manage.py showmigrations
python manage.py migrate --fake-initial
```

**Error de permisos**:
```bash
sudo chown -R www-data:www-data /path/to/duoc-point/
sudo chmod -R 755 /path/to/duoc-point/
```

**Error de Celery**:
```bash
celery -A duocpoint inspect active
celery -A duocpoint purge
```

**Error de Google OAuth**:
- Verificar que el dominio esté autorizado
- Verificar que las URIs de redirección sean correctas
- Verificar que la API esté habilitada

---

## 📋 Estado del Proyecto

### ✅ Funcionalidades Completadas

- [x] **Sistema de autenticación** con Google OAuth
- [x] **Mapa interactivo** con Leaflet y Street View
- [x] **Foros por carrera** con moderación automática
- [x] **Sistema de encuestas** completo con analytics
- [x] **Notificaciones** con Web Push
- [x] **Reportes de infraestructura** con flujo de estados
- [x] **Sistema de bienestar** por carrera
- [x] **Cursos abiertos** (OTEC)
- [x] **Sistema de compra/venta** con OpenGraph
- [x] **Portafolio automático** con generación PDF
- [x] **PWA** instalable con service worker
- [x] **API REST** completa con documentación

### 🔄 Funcionalidades en Desarrollo

- [ ] **Sistema de gestión de proyectos/sprints** (no implementado)
- [ ] **Integración con sistemas externos de Duoc UC**
- [ ] **Notificaciones push avanzadas**
- [ ] **Analytics avanzados**

### 🚀 Próximas Mejoras

- [ ] **Chat en tiempo real** con WebSockets
- [ ] **Sistema de calificaciones** de profesores
- [ ] **Integración con Moodle**
- [ ] **App móvil nativa** (React Native/Flutter)
- [ ] **Sistema de badges** y gamificación

---

## 📞 Soporte

Para soporte técnico o reportar problemas:

- **Issues**: [GitHub Issues](https://github.com/tu-usuario/duoc-point/issues)
- **Documentación**: Ver este README y `/docs/`
- **API Docs**: `/api/docs/` (Swagger)
- **Admin**: `/admin/` (Django Admin)

---

## Licencia

MIT — ver [LICENSE](LICENSE).

