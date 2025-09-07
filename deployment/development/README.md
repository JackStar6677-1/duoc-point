# Configuración de Desarrollo

## Requisitos
- Docker y Docker Compose
- Python 3.11+
- Node.js 18+

## Configuración Local

### Backend
```bash
cd src/backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend
```bash
cd src/frontend
# El frontend actual es estático, se sirve desde el backend
```

## Docker Development
```bash
cd deployment/development
docker-compose -f docker-compose.dev.yml up -d
```

## Variables de Entorno
Copia `env.example` a `.env` y configura:
- `DEBUG=True`
- `SECRET_KEY=tu-clave-secreta`
- `DATABASE_URL=postgresql://...`

