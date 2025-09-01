# Duoc-Point — resumen claro de qué es y qué tendrá

## Qué es

Plataforma web **cerrada** para la comunidad de **Duoc UC**, hecha como **PWA** (se puede “instalar” en el celular) y web tradicional. El acceso es **exclusivo con correos `@duocuc.cl`**. La idea es centralizar lo que el estudiante necesita día a día: orientación en la sede, comunicación por carrera, recordatorios, bienestar, reportes y feedback.

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

### 7) Compra/Venta segura

* Publicación de **links** (FB Marketplace, Yapo, MercadoLibre).
* **Previsualización OpenGraph**.
* Sin subir fotos propias → menos spam/fraude.

### 8) Votaciones y encuestas

* Creación por **moderadores/directores** o roles con permiso.
* Útiles para priorizar mejoras e **insights por sede/carrera**.
* Opción de ver resultados al cierre o en vivo.

### 9) Portafolio automático

* Genera **CV/portafolio PDF** con datos básicos del usuario.
* Sugerencias para mejorar (proyectos, logros, participación).

---

## Integraciones clave

* Login Google OAuth restringido a `@duocuc.cl`.
* PWA: manifest, service worker y soporte offline básico.
* Notificaciones: Web Push (VAPID) + FCM.
* OpenGraph para previsualizar enlaces en compra/venta.

---

## Arquitectura y stack

* **Backend**: Django + DRF, Celery, Redis.
* **DB**: PostgreSQL (prod) / SQLite (dev).
* **Frontend**: HTML/CSS/JS + Bootstrap 5, Leaflet, PWA.
* **Almacenamiento**: local en dev; S3/MinIO en prod.
* **Tiempo real (futuro)**: Django Channels.

---

## Seguridad y moderación

* Acceso solo `@duocuc.cl`.
* Moderación automática.
* Descargo legal visible.
* Roles: estudiante, moderador, director de carrera, staff sede, admin.

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

## Licencia

MIT — ver [LICENSE](LICENSE).

