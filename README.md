# DuocPoint - Sistema de Gestión Estudiantil

## Descripción del Sistema

DuocPoint es una aplicación web progresiva (PWA) desarrollada para la comunidad estudiantil de Duoc UC. El sistema implementa una arquitectura de microservicios con backend Django REST Framework y frontend PWA, proporcionando funcionalidades integrales para la gestión estudiantil.

## Arquitectura del Sistema

### Backend
- **Framework**: Django 4.2 con Django REST Framework
- **Base de Datos**: PostgreSQL (producción), SQLite (desarrollo)
- **Autenticación**: JWT con refresh tokens
- **API**: RESTful con documentación OpenAPI/Swagger
- **Cache**: Redis para optimización de rendimiento

### Frontend
- **Tecnología**: PWA (Progressive Web App)
- **Lenguajes**: HTML5, CSS3, JavaScript ES6+
- **Service Worker**: Funcionamiento offline y cache inteligente
- **Responsive Design**: Mobile-first approach
- **Manifest**: Instalación como aplicación nativa

### Infraestructura
- **Contenedores**: Docker con docker-compose
- **Proxy Reverso**: Nginx
- **Monitoreo**: Logs estructurados y métricas
- **Deployment**: Configuración para desarrollo y producción

## Módulos del Sistema

### 1. Gestión de Usuarios (accounts)
- Registro con validación de dominio institucional
- Autenticación JWT con roles y permisos
- Perfiles de usuario con información académica
- Sistema de recuperación de credenciales

### 2. Sistema de Foros (forum)
- Foros categorizados por carrera y sede
- Sistema de votación y comentarios anidados
- Moderación automática y manual
- Reportes de contenido inapropiado

### 3. Mercado de Compra/Venta (market)
- Publicación de productos con categorías
- Sistema de favoritos y búsqueda
- Upload de imágenes y previsualización OpenGraph
- Reportes de productos inapropiados

### 4. Portafolio Profesional (portfolio)
- Gestión de logros académicos y proyectos
- Historial laboral y habilidades técnicas
- Generación de PDF profesional
- Cálculo de completitud del perfil

### 5. Sistema de Encuestas (polls)
- Encuestas con opciones múltiples
- Votación anónima y con identificación
- Resultados en tiempo real
- Analytics de participación

### 6. Recorridos Virtuales (campuses)
- Mapa interactivo de sedes
- Recorridos 360° con Street View
- Información de puntos de interés
- Navegación offline

### 7. Notificaciones (notifications)
- Web Push notifications
- Configuración de preferencias
- Recordatorios automáticos
- Sistema de alertas

### 8. Reportes de Infraestructura (reports)
- Reportes de problemas de infraestructura
- Sistema de tickets
- Seguimiento de resolución
- Analytics de reportes

### 9. Bienestar Estudiantil (wellbeing)
- Rutinas de kinesiología
- Recursos de bienestar
- Seguimiento de actividades
- Integración con servicios de salud

## Instalación y Configuración

### Requisitos del Sistema
- Python 3.9+
- Node.js 16+ (para herramientas de desarrollo)
- PostgreSQL 13+ (producción)
- Redis 6+ (cache)

### Instalación Rápida
```bash
# Clonar el repositorio
git clone https://github.com/JackStar6677-1/duoc-point.git
cd duoc-point

# Instalar dependencias
pip install -r src/backend/requirements.txt

# Iniciar el sistema
python start.py
```

### Configuración Avanzada
```bash
# Configuración personalizada
python start.py --host 0.0.0.0 --port 8080

# Omitir migraciones (si ya están ejecutadas)
python start.py --no-migrate

# Solo iniciar servidor
python start.py --no-migrate --no-superuser --no-data
```

## Estructura del Proyecto

```
duoc-point/
├── src/
│   ├── backend/              # Backend Django
│   │   ├── duocpoint/        # Configuración principal
│   │   ├── apps/             # Aplicaciones del sistema
│   │   ├── manage.py         # Script de administración
│   │   └── requirements.txt  # Dependencias Python
│   └── frontend/             # Frontend PWA
│       ├── index.html        # Página principal
│       ├── manifest.json     # Manifest PWA
│       ├── sw.js            # Service Worker
│       └── [módulos]/       # Módulos de funcionalidad
├── deployment/               # Configuración Docker
├── docs/                    # Documentación API
├── releases/                # Archivos de distribución
├── dist/                    # PWA compilada
└── start.py                 # Iniciador del sistema
```

## API del Sistema

### Endpoints Principales
- `GET /api/` - Información de la API
- `POST /api/auth/login/` - Autenticación
- `GET /api/forum/` - Lista de foros
- `GET /api/market/products/` - Productos del mercado
- `GET /api/portfolio/` - Portafolio del usuario
- `GET /api/campuses/` - Información de sedes

### Documentación API
- Swagger UI: `http://localhost:8000/api/docs/`
- OpenAPI Schema: `http://localhost:8000/api/schema/`

## Desarrollo

### Ejecutar Tests
```bash
cd src/backend
python manage.py test
```

### Generar PWA
```bash
python generate_pwa.py
```

### Deployment con Docker
```bash
cd deployment/production
docker-compose up -d
```

## Configuración de Producción

### Variables de Entorno
```bash
DJANGO_SETTINGS_MODULE=duocpoint.settings.prod
DATABASE_URL=postgresql://user:pass@host:port/db
REDIS_URL=redis://host:port
SECRET_KEY=your-secret-key
DEBUG=False
```

### Nginx Configuration
```nginx
server {
    listen 80;
    server_name duocpoint.duocuc.cl;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Seguridad

### Implementaciones de Seguridad
- Validación de entrada en todos los endpoints
- Autenticación JWT con refresh tokens
- Rate limiting para prevenir abuso
- CORS configurado para dominios autorizados
- Sanitización de contenido HTML
- Encriptación de contraseñas con bcrypt

### Políticas de Acceso
- Registro limitado a dominios @duocuc.cl y @gmail.com
- Roles y permisos granulares
- Moderación automática de contenido
- Logs de auditoría para acciones críticas

## Monitoreo y Logs

### Métricas del Sistema
- Tiempo de respuesta de API
- Uso de memoria y CPU
- Errores y excepciones
- Actividad de usuarios

### Logs Estructurados
```json
{
  "timestamp": "2025-01-07T17:30:00Z",
  "level": "INFO",
  "module": "forum.views",
  "action": "create_post",
  "user_id": 123,
  "duration_ms": 150
}
```

## Equipo de Desarrollo

- **Pablo Avendaño** - Desarrollador Full Stack (pa.avendano@duocuc.cl)
- **Isaac Paz** - Desarrollador Backend y Documentación
- **Darosh Luco** - Desarrollador Frontend

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## Soporte Técnico

Para reportar problemas o solicitar funcionalidades:
- Crear un issue en el repositorio GitHub
- Contactar al equipo de desarrollo
- Revisar la documentación técnica en `/docs/`

---

**Versión**: 1.2.0  
**Última actualización**: Enero 2025  
**Estado**: Producción
