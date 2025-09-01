# Duoc-Point

**Plataforma Duoc-Point (MVP estudiantil, curso Ingeniería en Informática Duoc UC)**  
Aplicación académica desarrollada como **PWA (Progressive Web App)** y aplicación web tradicional, enfocada en la comunidad estudiantil de **Duoc UC**, con acceso exclusivo mediante correos `@duocuc.cl`.

---

## Descripción General

Duoc-Point es un proyecto que centraliza en una sola plataforma digital distintas herramientas para estudiantes y docentes de Duoc UC.  
El objetivo es crear un espacio cerrado y seguro donde los usuarios puedan acceder a mapas de sedes, foros por carrera, cursos abiertos, votaciones, reportes de infraestructura y secciones de bienestar.

La aplicación está diseñada para funcionar como:

- **Web tradicional:** accesible desde navegadores con diseño responsivo.  
- **PWA (Progressive Web App):** instalable en dispositivos móviles mediante "Agregar a la pantalla de inicio", con soporte de notificaciones push y experiencia similar a una aplicación nativa.

---

## Funcionalidades

### Módulos principales

1. **Mapa virtual con recorrido en fotos**  
   - Visualización de sedes Duoc UC en un mapa interactivo.  
   - Recorridos en formato de slides fotográficos, desde la entrada de la sede hasta aulas y espacios clave.  
   - Uso de Leaflet.js y almacenamiento de imágenes optimizadas en el backend.

2. **Foro entre carreras**  
   - Subforos por sede y por carrera (ejemplo: Informática Point, Arquitectura Point).  
   - Publicaciones de texto, comentarios en hilo y votos positivos/negativos.  
   - Moderación automática con filtros de spam y lenguaje inapropiado, acompañado de descargos de responsabilidad.  
   - API desarrollada con Django REST Framework y consumo desde la web/PWA.

3. **Notificaciones de clases**  
   - Los estudiantes cargan sus horarios.  
   - Recordatorios automáticos 20 minutos antes de cada clase.  
   - Implementación con Service Workers (web push) y FCM (Firebase Cloud Messaging).

4. **Cursos abiertos**  
   - Espacio para compartir cursos creados o subidos por estudiantes, docentes o directores de carrera.  
   - Los cursos son temporales, sin certificación, y orientados al aprendizaje.  
   - Formulario de alta y expiración gestionados en backend.

5. **Bienestar estudiantil por carrera**  
   - Rutinas de estiramientos y masajes según las necesidades de cada carrera (ejemplo: Informática → ejercicios para muñecas y túnel carpiano).  
   - Consejos de salud psicológica (hábitos de sueño, manejo de estrés).  
   - Material multimedia administrado desde el backend.

6. **Reportes de infraestructura y equipamiento**  
   - Reportes de fallas: mobiliario defectuoso, grietas, problemas en talleres.  
   - Incluye categoría, ubicación en mapa, descripción y fotos opcionales.  
   - Flujo de estados: Abierto → En revisión → Resuelto.

7. **Compra y venta segura**  
   - Clasificados internos con enlaces externos (Facebook Marketplace, Yapo.cl, MercadoLibre).  
   - Visualización segura mediante previsualización de links (OpenGraph).  
   - No se permite la subida directa de imágenes para reducir riesgos de spam o fraude.

8. **Votaciones y encuestas**  
   - Creación de encuestas por moderadores o directores de carrera.  
   - Herramienta de votación estudiantil para obtener feedback y priorizar recursos.

9. **Portafolio automático**  
   - Generador de portafolios/CVs en PDF.  
   - Incluye datos básicos del usuario y sugerencias para enriquecer el perfil.  
   - Implementado con plantillas HTML-to-PDF (WeasyPrint).

---

## Desarrollo desde cero

- API y backend completo con Django + Django REST Framework.  
- Foros, comentarios, votos y encuestas.  
- Notificaciones de horarios (Celery + push).  
- Generador de portafolio PDF.  
- Sistema de reportes con estados.  
- Carga y gestión de cursos abiertos.  
- Módulo de bienestar con contenido multimedia.

---

## Integración de herramientas existentes

- **Leaflet.js** para mapas interactivos.  
- **Google OAuth** restringido a `@duocuc.cl` para autenticación.  
- **Bootstrap 5** para diseño responsivo.  
- **Service Workers y PWA estándar** para instalación y notificaciones.  
- **OpenGraph Preview** para previsualizar links en la sección de compra/venta.  
- **PostgreSQL** como base de datos relacional.  
- **Redis + Celery** para tareas programadas y en segundo plano.  

---

## Tecnologías Principales

- **Backend:** Django, Django REST Framework, Celery, Redis, PostgreSQL.  
- **Frontend Web/PWA:** HTML, CSS, JavaScript, Bootstrap 5, Service Workers, Leaflet.js.  
- **Integración móvil:** Instalación como PWA + notificaciones push (FCM).  
- **Infraestructura:** Docker Compose (Postgres, Redis, backend, frontend).  

---

## Instalación y Uso

1. Clonar el repositorio:

   `git clone https://github.com/<owner>/duoc-point.git
   cd duoc-point`

2. Crear archivo `.env` a partir de `.env.example`.
   Ajusta las variables según tu entorno local (clave secreta, base de datos, etc.).

3. Revisar los archivos de configuración YAML en `config/` y reemplazar los
   valores *dummy* según corresponda (dominios, remitentes de correo,
   parámetros de seguridad, claves de push).

4. Levantar servicios básicos con Docker:

   `docker-compose up`

5. Ejecutar migraciones de Django:

   `docker-compose exec backend python manage.py migrate`

6. Acceder a la aplicación web en:

   `http://localhost:8000`

7. En móviles, instalar la aplicación como PWA desde el navegador.
