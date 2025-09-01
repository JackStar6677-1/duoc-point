# Duoc-Point

Plataforma académica **MVP** para la comunidad de **Duoc UC**.  
Requiere correos `@duocuc.cl` y funciona como sitio web tradicional o como
**PWA instalable** con soporte de notificaciones push.

---

## Módulos incluidos

- **Accounts** – usuario extendido, login JWT y endpoint `/api/me`.
- **Campuses** – sedes y recorridos fotográficos para un mapa con Leaflet.
- **Forum** – foros por carrera, posts, comentarios, votos y moderación básica.
- **Polls** – encuestas ligadas a posts.
- **Schedules/Notifications** – importación de horarios desde PDF y alertas push
  20 minutos antes de cada clase.
- **Reports** – reportes de infraestructura con fotos y flujo de estados.
- **OTEC** – publicación de cursos abiertos sin certificación.
- **Wellbeing** – recursos de bienestar por carrera con contenido Markdown.
- **Portfolio** – generador de PDF con datos del usuario.
- **PWA** – `manifest.webmanifest` y `service-worker.js` con caché y push.

---

## Requisitos

- Docker y Docker Compose
- GNU Make

---

## Configuración inicial

```bash
git clone https://github.com/<owner>/duoc-point.git
cd duoc-point/infra
cp .env.example .env        # ajustar variables si es necesario
# generar una SECRET_KEY única para producción
python -c 'import secrets, sys; sys.stdout.write(secrets.token_urlsafe(50))'
make up                     # levanta postgres, redis, backend y frontend
make celery beat            # arranca worker y scheduler de Celery
make migrate                # aplica migraciones
make createsuperuser        # opcional
```

La aplicación queda disponible en `http://localhost:8000`.

Para detener los servicios:

```bash
make down
```

---

## Tests

```bash
make test
```

---

## Importar horarios por PDF

1. Enviar `POST /api/horarios/import/pdf` con un PDF que contenga texto
   embebido.
2. Consultar el progreso en `GET /api/horarios/import/{id}`.
3. Los bloques generados se administran via `/api/horarios`.

**Configuración:**

- `config/security.yaml` controla tamaño máximo y extensiones permitidas.
- Coloca claves VAPID en `config/push.yaml` para habilitar las notificaciones
  web.  Puedes generarlas con `pywebpush`:

  ```bash
  python - <<'PY'
  from py_vapid import Vapid
  v = Vapid(); v.generate_keys()
  print(v.public_key, v.private_key)
  PY
  ```

---

## Opcional / Extensible

- **OCR para PDFs escaneados:** agregar `pytesseract` y `pdf2image` y ampliar
  `schedules.tasks.parse_schedule_pdf`.
- **PWA:** cambiar colores e íconos en `web/manifest.webmanifest` y el caché en
  `web/service-worker.js`.
- **Almacenamiento:** editar `config/storage.yaml` para usar S3/MinIO.
- **Throttling, CORS y límites de subida:** configurar en `.env` y
  `config/security.yaml`.
- **Exportar esquema OpenAPI:**

  ```bash
  python server/manage.py spectacular --file docs/api-openapi.yaml
  ```

---

## Licencia

MIT — ver [LICENSE](LICENSE).

