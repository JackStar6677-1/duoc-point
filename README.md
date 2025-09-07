# 🎓 DuocPoint - Plataforma Integral Duoc UC

[![Version](https://img.shields.io/badge/version-1.2.0-blue.svg)](https://github.com/duocpoint/duocpoint/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-27%2F27%20passing-brightgreen.svg)](src/backend/tests/)
[![PWA](https://img.shields.io/badge/PWA-ready-orange.svg)](src/frontend/manifest.json)

> **Plataforma integral para la comunidad estudiantil de DUOC UC** - Una aplicación web y móvil que conecta estudiantes, facilita el aprendizaje y mejora la experiencia universitaria.

## 🚀 Inicio Rápido

### Opción 1: Servidor de Desarrollo (Recomendado)
```bash
# Clonar el repositorio
git clone https://github.com/duocpoint/duocpoint.git
cd duoc-point

# Activar entorno virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r src/backend/requirements.txt

# Iniciar servidor
python start.py
```

### Opción 2: Docker (Producción)
```bash
# Construir y ejecutar con Docker
docker-compose -f deployment/production/docker-compose.yml up --build
```

### Opción 3: PWA Instalable
```bash
# Descargar PWA
wget https://github.com/duocpoint/duocpoint/releases/latest/download/DuocPoint-PWA-v1.2.0.zip
unzip DuocPoint-PWA-v1.2.0.zip
# Abrir index.html en navegador y instalar como PWA
```

## 📱 Acceso a la Aplicación

- **Web**: http://localhost:8000
- **API**: http://localhost:8000/api/
- **Documentación**: http://localhost:8000/api/docs/
- **Admin**: http://localhost:8000/admin/

### Credenciales de Prueba
- **Email**: `admin@duocuc.cl`
- **Password**: `admin123`
- **Estudiante**: `estudiante@duocuc.cl` / `estudiante123`

## 🎯 Funcionalidades Principales

### 1. 🗺️ **Mapa Virtual de Salas**
- **Búsqueda por número de sala**
- **Recorridos 360° interactivos**
- **Imágenes secuenciales** (entrada → torre → piso → sala)
- **Caché inteligente** de imágenes frecuentes
- **Navegación offline** para salas visitadas

**URL**: `/streetview/` | **API**: `/api/campuses/`

### 2. 💬 **Foro Entre Carreras (Estilo Reddit)**
- **Autenticación Microsoft Entra ID** (MFA)
- **Subforos por carrera y tema**
- **Sistema de votación** (upvote/downvote)
- **Moderación comunitaria** y reportes
- **Comentarios anidados**
- **Filtrado automático** de contenido inapropiado

**URL**: `/forum/` | **API**: `/api/posts/`

### 3. 📅 **Notificaciones de Clases**
- **Importación de horarios PDF**
- **Extracción automática** de asignaturas y horarios
- **Notificaciones push** 20 minutos antes de cada clase
- **Sincronización** con calendario personal
- **Recordatorios personalizables**

**URL**: `/horarios/` | **API**: `/api/schedules/`

### 4. 📚 **Cursos Abiertos OTEC**
- **Catálogo de cursos** disponibles al público
- **Filtros por sede y carrera**
- **Información detallada** de cada curso
- **Inscripción directa**
- **Seguimiento de progreso**

**URL**: `/cursos/` | **API**: `/api/otec/`

### 5. 💚 **Bienestar Estudiantil**
- **Rutinas de kinesiología** por carrera
- **Recomendaciones psicológicas**
- **Consejos de hábitos de sueño**
- **Material multimedia** (texto, imágenes, videos)
- **Seguimiento personalizado**

**URL**: `/bienestar/` | **API**: `/api/bienestar/`

### 6. 🚨 **Reportes de Infraestructura**
- **Reporte de incidencias** (proyector, PC, infraestructura)
- **Categorización automática**
- **Seguimiento de estado**
- **Notificaciones a administración**
- **Historial de reportes**

**URL**: `/reportes/` | **API**: `/api/reports/`

### 7. 🛒 **Compra y Venta Segura**
- **Mercado estudiantil** integrado
- **Categorías de productos**
- **Sistema de favoritos**
- **Moderación comunitaria**
- **Enlaces filtrados** a Facebook Marketplace

**URL**: `/market/` | **API**: `/api/market/`

### 8. 📊 **Votaciones y Encuestas**
- **Creación de encuestas** en foros
- **Resultados en tiempo real**
- **Análisis estadístico**
- **Exportación de datos**
- **Dashboard de administración**

**URL**: `/encuestas/` | **API**: `/api/polls/`

### 9. 📋 **Portafolio Automático**
- **Historial digital** de participación
- **Evidencia de actividades** (foros, cursos, encuestas)
- **Generación automática** de portafolio
- **Exportación a PDF**
- **Configuración personalizable**

**URL**: `/portfolio/` | **API**: `/api/portfolio/`

## 🏗️ Arquitectura Técnica

### Backend
- **Framework**: Django 5.2 + Django REST Framework
- **Base de Datos**: PostgreSQL (producción) / SQLite (desarrollo)
- **Autenticación**: JWT + Microsoft Entra ID
- **Tareas Asíncronas**: Celery + Redis
- **Documentación**: Swagger UI
- **Tests**: 27/27 pasando ✅

### Frontend
- **Tecnología**: HTML5, CSS3, JavaScript ES6+
- **Framework**: Bootstrap 5.3
- **PWA**: Service Worker + Manifest
- **Notificaciones**: Web Push API
- **Mapas**: Leaflet.js
- **Responsive**: Mobile-first design

### Móvil
- **Framework**: Ionic 7 + Angular
- **Plataforma**: Capacitor
- **Compilación**: Android APK
- **PWA**: Instalable como app nativa

## 📦 Instalación PWA

### En Navegador Web
1. Abrir http://localhost:8000
2. Hacer clic en "Instalar DuocPoint" en la barra de navegación
3. Confirmar instalación
4. La app aparecerá en el escritorio/menú de aplicaciones

### En Móvil
1. Abrir http://localhost:8000 en Chrome/Safari
2. Tocar el menú del navegador
3. Seleccionar "Agregar a pantalla de inicio"
4. La app se instalará como aplicación nativa

## 🧪 Testing

```bash
# Ejecutar todos los tests
cd src/backend
python manage.py test --verbosity=2

# Tests específicos
python manage.py test tests.test_authentication
python manage.py test tests.test_forum

# Verificar cobertura
python manage.py test --coverage
```

## 🚀 Deployment

### Desarrollo Local
```bash
python start.py local
```

### Red Local
```bash
python start.py network
```

### Producción con HTTPS
```bash
python start.py ngrok
```

### Docker
```bash
docker-compose -f deployment/production/docker-compose.yml up -d
```

## 📊 Estado del Proyecto

| Componente | Estado | Tests | Funcionalidades |
|------------|--------|-------|-----------------|
| Backend | ✅ Completo | 27/27 | 9/9 |
| Frontend | ✅ Completo | - | 9/9 |
| PWA | ✅ Completo | - | 9/9 |
| Móvil | ✅ Completo | - | 9/9 |
| APIs | ✅ Completo | 27/27 | 9/9 |
| Base de Datos | ✅ Completo | - | 9/9 |

## 🔧 Comandos Útiles

```bash
# Iniciar servidor
python start.py

# Ejecutar tests
python manage.py test

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Cargar datos de prueba
python manage.py loaddata fixtures/initial_data.json

# Generar documentación API
python manage.py spectacular --file docs/api-openapi.yaml
```

## 📱 Aplicación Móvil

### Generar APK
```bash
cd src/mobile
npm install
ionic capacitor build android
cd android
./gradlew assembleDebug
```

### Instalar en Dispositivo
```bash
# Conecta tu dispositivo Android
adb install android/app/build/outputs/apk/debug/app-debug.apk
```

## 🌐 URLs Importantes

| Funcionalidad | URL Web | API Endpoint |
|---------------|---------|--------------|
| Inicio | `/` | `/api/` |
| Foros | `/forum/` | `/api/posts/` |
| Mercado | `/market/` | `/api/market/` |
| Portafolio | `/portfolio/` | `/api/portfolio/` |
| Recorridos | `/streetview/` | `/api/campuses/` |
| Bienestar | `/bienestar/` | `/api/bienestar/` |
| Reportes | `/reportes/` | `/api/reports/` |
| Cursos | `/cursos/` | `/api/otec/` |
| Encuestas | `/encuestas/` | `/api/polls/` |
| Horarios | `/horarios/` | `/api/schedules/` |
| Login | `/login.html` | `/api/auth/login/` |
| Registro | `/register.html` | `/api/auth/register/` |
| Admin | `/admin/` | - |
| API Docs | `/api/docs/` | `/api/schema/` |

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.

## 👥 Equipo

- **Pablo Avendaño** - Desarrollador Full Stack
- **Isaac Paz** - Desarrollador Backend
- **Darosh Luco** - Desarrollador Frontend

## 📞 Soporte

- **Email**: soporte@duocpoint.duocuc.cl
- **Issues**: [GitHub Issues](https://github.com/duocpoint/duocpoint/issues)
- **Documentación**: [Wiki](https://github.com/duocpoint/duocpoint/wiki)

## 🎉 Agradecimientos

- **DUOC UC** por el apoyo institucional
- **Comunidad estudiantil** por el feedback y testing
- **Contribuidores** que han ayudado a mejorar la plataforma

---

**DuocPoint v1.2.0** - Conectando la comunidad estudiantil de DUOC UC 🎓