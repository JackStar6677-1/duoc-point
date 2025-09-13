# StudentsPoint

Una aplicación web progresiva (PWA) integral diseñada para la comunidad estudiantil global. StudentsPoint proporciona un ecosistema integrado de herramientas y servicios para mejorar la experiencia académica y profesional de estudiantes en todo el mundo.

## Descripción General

StudentsPoint es una plataforma de código abierto que combina múltiples aplicaciones enfocadas en estudiantes en una experiencia única y cohesiva. Construida con Django y tecnologías web modernas, ofrece una gama de características desde herramientas académicas hasta recursos de desarrollo profesional.

## Público Objetivo

- **Estudiantes**: Usuarios principales que buscan herramientas académicas y de desarrollo profesional
- **Instituciones Educativas**: Organizaciones que buscan proporcionar servicios estudiantiles integrales
- **Desarrolladores**: Contribuidores interesados en tecnología educativa y desarrollo PWA
- **Educadores**: Profesores y administradores que desean mejorar el compromiso estudiantil

## Características Principales

### Sistema de Autenticación
- Autenticación tradicional con email/contraseña
- Integración con Google OAuth para inicio de sesión fluido
- Validación de email flexible que soporta múltiples dominios
- Gestión segura de tokens basada en JWT

### Aplicaciones Principales

#### Herramientas Académicas
- **Foros**: Tableros de discusión con moderación automatizada
- **Horarios**: Gestión de horarios de clases con capacidades de importación PDF
- **Encuestas**: Sistema de votación y encuestas para retroalimentación estudiantil
- **Directorio de Profesores**: Información y detalles de contacto de la facultad

#### Desarrollo Profesional
- **Portafolio**: Gestión de perfil profesional con generación de PDF
- **Cursos (OTEC)**: Plataforma de intercambio de cursos abiertos
- **Marketplace**: Intercambio de productos a través de enlaces externos (Facebook Marketplace, MercadoLibre)

#### Servicios Estudiantiles
- **Bienestar**: Recursos de salud y bienestar
- **Reportes**: Sistema de reportes de infraestructura e instalaciones
- **Notificaciones**: Sistema de notificaciones push para actualizaciones importantes
- **Tours Virtuales**: Implementación personalizada de vista de calle

### Características Técnicas
- **Aplicación Web Progresiva**: Funcionalidad offline y experiencia similar a una app
- **Diseño Responsivo**: Enfoque mobile-first con Bootstrap 5
- **API RESTful**: API integral con documentación Swagger
- **Notificaciones en Tiempo Real**: Soporte para notificaciones push web
- **Generación de PDF**: Creación de documentos profesionales usando ReportLab

## Stack Tecnológico

### Backend
- **Django 5.0+**: Framework web
- **Django REST Framework**: Desarrollo de API
- **PostgreSQL/SQLite**: Gestión de base de datos
- **Celery + Redis**: Procesamiento de tareas asíncronas
- **ReportLab**: Generación de PDF
- **Google OAuth**: Integración de autenticación

### Frontend
- **HTML5/CSS3/JavaScript**: Tecnologías web principales
- **Bootstrap 5**: Framework de UI
- **Font Awesome**: Biblioteca de iconos
- **Service Workers**: Funcionalidad PWA

### Herramientas de Desarrollo
- **pytest**: Framework de testing
- **Docker**: Soporte de contenedores
- **Git**: Control de versiones

## Instalación

### Prerrequisitos
- Python 3.11 o superior
- PostgreSQL (opcional, SQLite usado por defecto)
- Git

### Inicio Rápido

1. **Clonar el repositorio**
```bash
git clone <repository-url>
cd students-point
```

2. **Ejecutar el script de desarrollo**
```bash
# Windows
iniciar_desarrollo.bat

# Linux/Mac
chmod +x iniciar_desarrollo.sh
./iniciar_desarrollo.sh
```

3. **Acceder a la aplicación**
- Aplicación: http://127.0.0.1:8000
- Panel de Administración: http://127.0.0.1:8000/admin/
- Documentación de API: http://127.0.0.1:8000/api/docs/

### Instalación Manual

1. **Instalar dependencias**
```bash
cd proyecto/src/backend
pip install -r requirements.txt
```

2. **Configurar base de datos**
```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

3. **Crear superusuario**
```bash
python ensure_superuser.py
```

4. **Iniciar servidor de desarrollo**
```bash
python manage.py runserver
```

## Configuración de Base de Datos

### Desarrollo (SQLite)
- **Ubicación**: `proyecto/src/backend/db.sqlite3`
- **Tamaño actual**: ~608 KB
- **Uso**: Desarrollo local y pruebas
- **Configuración**: Automática, no requiere configuración adicional

### Producción (PostgreSQL)
- **Host**: localhost
- **Puerto**: 5432
- **Usuario**: postgres
- **Contraseña**: 214526867
- **Base de datos**: studentspoint_prod
- **Configuración**: Usar archivo `.env` con variables de entorno

## Credenciales por Defecto

- **Email**: admin@studentspoint.app
- **Contraseña**: admin123

## Configuración de Google OAuth

### Configuración Requerida
Para habilitar la funcionalidad de Google OAuth, configure lo siguiente en Google Cloud Console:

**Client ID**: `307562557576-0fd8ta7i09i1e6it5hstla13jsomeq2s.apps.googleusercontent.com`

### URIs de Redirección Autorizadas
Agregue estas URLs a su configuración OAuth de Google Cloud Console:

```
http://localhost:8000/api/auth/google/callback/web/
http://127.0.0.1:8000/api/auth/google/callback/web/
https://studentspoint.app/api/auth/google/callback/web/
https://yourdomain.com/api/auth/google/callback/web/
```

## Documentación de API

La aplicación proporciona una API REST integral con los siguientes endpoints principales:

### Autenticación
- `POST /api/auth/login/` - Inicio de sesión de usuario
- `POST /api/auth/register/` - Registro de usuario
- `GET /api/auth/google/login/` - Iniciación de Google OAuth
- `POST /api/auth/google/callback/` - Callback de Google OAuth

### Aplicaciones
- `GET /api/forum/` - Gestión de foros
- `GET /api/market/` - Operaciones de marketplace
- `GET /api/portfolio/` - Gestión de portafolio
- `GET /api/portfolio/generate_pdf/` - Generación de PDF
- `GET /api/polls/` - Gestión de encuestas y votaciones
- `GET /api/schedules/` - Gestión de horarios
- `GET /api/notifications/` - Sistema de notificaciones
- `GET /api/reports/` - Sistema de reportes
- `GET /api/otec/` - Gestión de cursos

## Estructura del Proyecto

```
students-point/
├── Documentacion/           # Documentación del proyecto
├── FASE 1/                 # Evidencias de desarrollo
├── proyecto/
│   ├── src/backend/        # Backend Django
│   │   ├── studentspoint/  # Configuración principal
│   │   ├── staticfiles/    # Archivos estáticos servidos
│   │   ├── db.sqlite3      # Base de datos SQLite (desarrollo)
│   │   └── manage.py       # Script de gestión Django
│   └── imagenes/           # Imágenes y logos
├── iniciar_desarrollo.bat  # Script de inicio de desarrollo
├── iniciar_produccion.bat  # Script de inicio de producción
└── README.md              # Este archivo
```

## Desarrollo

### Ejecutar Pruebas
```bash
cd proyecto/src/backend
python manage.py test
```

### Estilo de Código
El proyecto sigue las mejores prácticas de Django y las pautas PEP 8.

### Contribuir
1. Fork del repositorio
2. Crear una rama de característica (`git checkout -b feature/AmazingFeature`)
3. Commit de los cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Consideraciones de Seguridad

- Tokens JWT para autenticación segura
- Configuración CORS para desarrollo
- Protección CSRF para formularios web
- Validación de email para registro de usuarios
- Integración OAuth 2.0 para autenticación de terceros

## Soporte de Navegadores

- Chrome 80+
- Firefox 75+
- Safari 13+
- Edge 80+

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para detalles.

## Soporte

Para soporte y preguntas:
- Crear un issue en el repositorio de GitHub
- Contacto: admin@studentspoint.app

## Roadmap

- Experiencia móvil mejorada
- Proveedores OAuth adicionales
- Panel de análisis avanzado
- Integración con sistemas de gestión de aprendizaje
- Soporte multi-idioma

## Agradecimientos

- Comunidad Django por el excelente framework
- Equipo Bootstrap por los componentes de UI
- Google por la integración OAuth
- Todos los contribuidores y testers

---

**StudentsPoint** - Empoderando estudiantes a través de la tecnología