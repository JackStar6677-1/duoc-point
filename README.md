# Duoc-Point

**Plataforma Duoc-Point (MVP estudiantil, curso Ingeniería en Informática Duoc UC)**  
Aplicación académica desarrollada como **PWA (Progressive Web App)** y aplicación web tradicional, enfocada en la comunidad estudiantil de **Duoc UC**, con acceso exclusivo mediante correos `@duocuc.cl`.

---

## Descripción General

Duoc-Point es un proyecto que busca centralizar en una sola plataforma digital distintas herramientas para estudiantes y docentes de Duoc UC.  
El objetivo es crear un espacio cerrado y seguro donde los usuarios puedan acceder a mapas de sedes, foros por carrera, cursos abiertos, votaciones, reportes de infraestructura y secciones de bienestar.

La aplicación está diseñada para funcionar tanto como:

- **Web tradicional:** accesible desde navegadores con diseño responsivo.  
- **PWA (Progressive Web App):** instalable en dispositivos móviles mediante "Agregar a la pantalla de inicio", con soporte de notificaciones push y experiencia similar a una aplicación nativa.

---

## Funcionalidades

### Módulos principales

1. **Mapa virtual con recorrido en fotos**  
   - Visualización de sedes Duoc UC en un mapa interactivo.  
   - Recorrido tipo *Street View básico* a través de **slides fotográficos** desde la entrada de la sede hasta aulas y espacios clave.  
   - Uso de **Leaflet.js** y almacenamiento de imágenes optimizadas en el backend.

2. **Foro entre carreras**  
   - Subforos por sede y por carrera (ejemplo: *Informática Point*, *Arquitectura Point*).  
   - Publicaciones de texto, comentarios en hilo, votos positivos/negativos.  
   - Moderación automática con filtros de spam, lenguaje inapropiado y descargo de responsabilidad.  
   - Desarrollado desde cero con **Django REST Framework** (API) y consumo desde web/PWA.

3. **Notificaciones de clases**  
   - Los estudiantes cargan sus horarios.  
   - Recordatorios automáticos 20 minutos antes de cada clase.  
   - Implementación: **Service Workers (web push)** y **FCM (Firebase Cloud Messaging)** para PWA.

4. **Cursos abiertos**  
   - Espacio para compartir cursos subidos por estudiantes, docentes o directores de carrera.  
   - Los cursos son temporales, sin certificación, y enfocados en el aprendizaje.  
   - Desarrollado con formularios propios y lógica de expiración en backend.

5. **Bienestar estudiantil por carrera**  
   - Rutinas de estiramientos y masajes específicos según las necesidades de cada carrera (ejemplo: Informática → ejercicios para muñecas y túnel carpiano).  
   - Consejos de salud psicológica (hábitos de sueño, manejo de estrés).  
   - Material multimedia administrado desde el backend.

6. **Reportes de infraestructura y equipamiento**  
   - Envío de reportes de fallas: mobiliario defectuoso, grietas, problemas en talleres.  
   - Los reportes incluyen categoría, ubicación en mapa, descripción y fotos.  
   - Flujo de estados: *Abierto → En revisión → Resuelto*.

7. **Compra y venta segura**  
   - Sección de clasificados internos donde los estudiantes publican enlaces externos (Facebook Marketplace, Yapo.cl, MercadoLibre).  
   - La plataforma actúa como visualizador seguro mediante previsualización de links (OpenGraph).  
   - No se permite subida directa de imágenes, reduciendo riesgos de spam/fraude.

8. **Votaciones y encuestas**  
   - Herramienta de encuestas creada por moderadores o directores de carrera.  
   - Permite a los estudiantes votar y generar feedback útil para priorizar recursos.  

9. **Portafolio automático**  
   - Herramienta para generar portafolios/CVs en PDF.  
   - Incluye datos básicos del usuario y recomendaciones para enriquecer su perfil.  
   - Desarrollado con plantillas HTML-to-PDF (WeasyPrint).

---

## Qué se desarrollará desde cero

- **API y backend completo:** Django + Django REST Framework.  
- **Foros, comentarios, votos y encuestas.**  
- **Notificaciones de horarios (programación con Celery + push).**  
- **Generador de portafolio PDF.**  
- **Sistema de reportes con estados.**  
- **Carga de cursos abiertos.**  
- **Módulo de bienestar con contenido multimedia administrado.**

---

## Qué aprovechará herramientas existentes

- **Leaflet.js** para mapas interactivos.  
- **Google OAuth** restringido a `@duocuc.cl` para autenticación.  
- **Bootstrap 5** para el diseño responsivo del frontend.  
- **Service Workers + PWA estándar** para instalación en móviles y push notifications.  
- **OpenGraph Preview** para mostrar información de links en compra/venta.  
- **PostgreSQL** para base de datos relacional.  
- **Redis + Celery** para tareas en segundo plano.  

---

## Tecnologías Principales

- **Backend:** Django, Django REST Framework, Celery, Redis, PostgreSQL.  
- **Frontend Web/PWA:** HTML, CSS, JavaScript, Bootstrap 5, Service Workers, Leaflet.js.  
- **Integración Móvil:** Instalación como PWA + notificaciones push (FCM).  
- **Infraestructura:** Docker Compose (Postgres, Redis, backend, frontend).  

---

## Instalación y Uso (resumen)

1. Clonar el repositorio:

   git clone https://github.com/<owner>/duoc-point.git
   cd duoc-point

2. Crear archivo `.env` a partir de `.env.example`.

3. Levantar servicios básicos con Docker:

   docker-compose up

4. Ejecutar migraciones de Django:

   docker-compose exec backend python manage.py migrate

5. Acceder a la aplicación web en:

   http://localhost:8000

6. Instalar la aplicación como PWA desde el navegador en móvil.

