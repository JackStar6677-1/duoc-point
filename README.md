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

1. **Mapa y recorrido virtual**: mapa por sede con Leaflet y recorridos fotográficos en slides.
2. **Foro por carrera** tipo Reddit con posts de texto, comentarios en hilo y votos ↑↓.
3. **Notificaciones de clases**: carga de horarios y recordatorio 20 minutos antes vía Web Push.
4. **Cursos abiertos** sin certificado.
5. **Bienestar** por carrera con material en texto, imágenes o videos.
6. **Reportes de infraestructura** con fotos y flujo de estados.
7. **Compra/Venta segura** con previsualización OpenGraph.
8. **Votaciones y encuestas** creadas por roles autorizados.
9. **Portafolio automático** en PDF con datos del usuario.

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

## Roadmap corto (~3 meses)

1. Base: auth dominio, PWA mínima, sedes+mapa, foros texto.
2. Productividad: horarios + push 20 min; reportes con fotos/estados.
3. Contenido: cursos abiertos, bienestar, encuestas.
4. Salida: portafolio PDF + pulido y demo.

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

## Ejecución con Docker

### Requisitos

- Docker y Docker Compose
- GNU Make

### Pasos

```bash
git clone https://github.com/<owner>/duoc-point.git
cd duoc-point/infra
cp .env.example .env        # ajustar variables si es necesario
# generar una SECRET_KEY única para producción
python -c 'import secrets, sys; sys.stdout.write(secrets.token_urlsafe(50))'
make up                     # levanta postgres, redis, backend y frontend
make migrate                # aplica migraciones
make createsuperuser        # opcional, crea un usuario administrador
make celery beat            # arranca worker y scheduler de Celery
```

La aplicación queda disponible en `http://localhost:8000`.

Para detener los servicios:

```bash
make down
```

---

## Inicio rápido (sin Docker)

Para probar el proyecto sin contenedores, asegúrate de tener **Python 3** y **pip**. Luego ejecuta:

```bash
bash run_local.sh
```

El script crea un entorno virtual `.venv`, instala las dependencias, aplica migraciones sobre SQLite y levanta el servidor en `http://localhost:8000`.

Funcionalidades que dependen de servicios externos (OAuth, Web Push, mapas con claves privadas, etc.) están deshabilitadas o usan valores de ejemplo para que el arranque local no requiera configuraciones adicionales.

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

## Servicios externos y costos

No es necesario contratar APIs de pago para ejecutar el proyecto en el entorno de desarrollo. Las integraciones utilizadas son de código abierto o cuentan con planes gratuitos:

- **Google OAuth**: autenticación restringida al dominio `@duocuc.cl`. Requiere crear credenciales en Google Cloud, pero el uso es gratuito dentro de los límites estándar.
- **Web Push / FCM**: envío de notificaciones a navegadores y móviles; ambos tienen niveles gratuitos.
- **Almacenamiento**: en desarrollo se usa el sistema de archivos local; en producción puede configurarse MinIO (open source) o servicios tipo S3.

### Checklist antes de desplegar

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

## Tests

```bash
make test
```

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

