# Documentación Técnica - DuocPoint

## Arquitectura del Sistema

### Backend
- **Framework**: Django 5.0 + Django REST Framework
- **Base de Datos**: PostgreSQL (producción) / SQLite (desarrollo)
- **Autenticación**: JWT con validación de dominios
- **Tareas Asíncronas**: Celery + Redis
- **API**: RESTful con documentación Swagger

### Frontend
- **Tecnologías**: HTML5, CSS3, JavaScript ES6+
- **Framework CSS**: Bootstrap 5
- **PWA**: Service Worker + Manifest
- **Mapas**: Leaflet.js
- **Notificaciones**: Web Push (VAPID)

### Infraestructura
- **Contenedores**: Docker + Docker Compose
- **Servidor Web**: Nginx + Gunicorn
- **Almacenamiento**: Local (desarrollo) / S3 (producción)

## Estructura de Aplicaciones

```
duocpoint/
├── apps/
│   ├── accounts/          # Gestión de usuarios
│   ├── campuses/          # Sedes y recorridos
│   ├── forum/            # Sistema de foros
│   ├── market/           # Compra/venta
│   ├── portfolio/        # Portafolio automático
│   ├── polls/            # Encuestas
│   ├── notifications/    # Notificaciones push
│   ├── schedules/        # Horarios
│   ├── reports/          # Reportes de infraestructura
│   ├── otec/             # Cursos abiertos
│   └── wellbeing/        # Bienestar estudiantil
```

## Modelos de Datos Principales

### User (Usuario Extendido)
- Campos personalizados para estudiantes Duoc UC
- Validación de dominios @duocuc.cl y @gmail.com
- Roles: student, moderator, director_carrera, admin_global

### Forum (Sistema de Foros)
- Posts con moderación automática
- Sistema de reportes
- Comentarios y votos
- Filtros por sede y carrera

### Market (Compra/Venta)
- Productos con categorización
- Sistema de favoritos
- Analytics de productos
- Integración OpenGraph

### Portfolio (Portafolio)
- Logros, proyectos, experiencias
- Generación automática de PDF
- Sugerencias de mejora
- Analytics de completitud

## API Endpoints Principales

### Autenticación
- `POST /api/auth/login/` - Login
- `POST /api/auth/refresh/` - Refresh token
- `GET /api/accounts/me/` - Perfil usuario

### Foros
- `GET /api/forum/foros/` - Lista foros
- `GET /api/forum/posts/` - Lista posts
- `POST /api/forum/posts/` - Crear post
- `POST /api/forum/posts/{id}/reportar/` - Reportar post
- `POST /api/forum/posts/{id}/moderar/` - Moderar post

### Mercado
- `GET /api/market/productos/` - Lista productos
- `POST /api/market/productos/` - Crear producto
- `GET /api/market/categorias/` - Categorías

### Portafolio
- `GET /api/portfolio/portafolio-completo/` - Portafolio completo
- `POST /api/portfolio/generar-pdf/` - Generar PDF

## Seguridad

### Autenticación y Autorización
- JWT tokens con expiración
- Validación de dominios de email
- Roles y permisos granulares
- CORS configurado

### Moderación de Contenido
- Filtros automáticos de palabras prohibidas
- Sistema de reportes de usuarios
- Panel de moderación para administradores
- Historial de acciones de moderación

### Validación de Datos
- Serializers con validación
- Sanitización de HTML
- Límites de tamaño de archivos
- Rate limiting en endpoints críticos

## Deployment

### Desarrollo
```bash
python manage.py runserver
```

### Producción
```bash
# Con Docker
docker-compose up -d

# Manual
gunicorn duocpoint.wsgi:application
```

### Variables de Entorno
- `DEBUG`: Modo debug
- `SECRET_KEY`: Clave secreta Django
- `DB_*`: Configuración base de datos
- `CELERY_*`: Configuración Celery
- `GOOGLE_*`: APIs de Google (opcional)

## Testing

### Tests Unitarios
```bash
python manage.py test
```

### Tests de Integración
- Tests de API con requests
- Tests de autenticación
- Tests de moderación
- Tests de generación PDF

## Monitoreo y Logs

### Logs
- Logs de Django en archivos
- Logs de Celery
- Logs de Nginx
- Logs de errores de aplicación

### Métricas
- Uso de API endpoints
- Actividad de usuarios
- Reportes de moderación
- Performance de base de datos

## Backup y Recuperación

### Base de Datos
```bash
pg_dump duocpoint_prod > backup.sql
```

### Archivos Media
```bash
tar -czf media_backup.tar.gz media/
```

### Restauración
```bash
psql duocpoint_prod < backup.sql
tar -xzf media_backup.tar.gz
```
