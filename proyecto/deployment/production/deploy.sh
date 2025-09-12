#!/bin/bash

# Script de deployment para DuocPoint
# Versión: 1.0.0

set -e

echo "🚀 Iniciando deployment de DuocPoint..."

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para logging
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Verificar que Docker esté instalado
if ! command -v docker &> /dev/null; then
    error "Docker no está instalado. Por favor instala Docker primero."
fi

if ! command -v docker-compose &> /dev/null; then
    error "Docker Compose no está instalado. Por favor instala Docker Compose primero."
fi

# Verificar que el archivo .env exista
if [ ! -f .env ]; then
    warning "Archivo .env no encontrado. Creando archivo .env de ejemplo..."
    cat > .env << EOF
# Configuración de base de datos
POSTGRES_DB=duocpoint_prod
POSTGRES_USER=duocpoint
POSTGRES_PASSWORD=your_secure_password_here

# Configuración de Django
SECRET_KEY=your_secret_key_here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,your_domain.com

# Configuración de Redis
REDIS_URL=redis://redis:6379/0

# Configuración de email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

# Configuración de Web Push
VAPID_PUBLIC_KEY=your_vapid_public_key
VAPID_PRIVATE_KEY=your_vapid_private_key
VAPID_ADMIN_EMAIL=admin@duocuc.cl

# Configuración de Google (opcional)
GOOGLE_OAUTH2_CLIENT_ID=
GOOGLE_OAUTH2_CLIENT_SECRET=
GOOGLE_MAPS_API_KEY=
EOF
    warning "Por favor edita el archivo .env con tus configuraciones antes de continuar."
    exit 1
fi

# Función para backup
backup_database() {
    log "Creando backup de la base de datos..."
    if [ -f "backup_$(date +%Y%m%d_%H%M%S).sql" ]; then
        warning "Backup ya existe para esta fecha y hora"
    else
        docker-compose -f docker-compose.prod.yml exec postgres pg_dump -U duocpoint duocpoint_prod > "backup_$(date +%Y%m%d_%H%M%S).sql"
        success "Backup creado exitosamente"
    fi
}

# Función para migraciones
run_migrations() {
    log "Ejecutando migraciones de base de datos..."
    docker-compose -f docker-compose.prod.yml exec django python manage.py migrate
    success "Migraciones ejecutadas exitosamente"
}

# Función para recolección de archivos estáticos
collect_static() {
    log "Recolectando archivos estáticos..."
    docker-compose -f docker-compose.prod.yml exec django python manage.py collectstatic --noinput
    success "Archivos estáticos recolectados exitosamente"
}

# Función para crear superusuario
create_superuser() {
    log "Creando superusuario..."
    docker-compose -f docker-compose.prod.yml exec django python manage.py createsuperuser --noinput --username admin --email admin@duocuc.cl || true
    success "Superusuario creado o ya existe"
}

# Función para poblar datos iniciales
populate_data() {
    log "Poblando datos iniciales..."
    docker-compose -f docker-compose.prod.yml exec django python manage.py shell -c "
from duocpoint.apps.campuses.models import Sede
from duocpoint.apps.accounts.models import User
from django.contrib.auth import get_user_model

# Crear sede si no existe
if not Sede.objects.exists():
    Sede.objects.create(
        nombre='Sede Maipú',
        direccion='Av. Américo Vespucio 1501, Maipú',
        lat=-33.5115,
        lng=-70.7525
    )
    print('Sede Maipú creada')

# Crear usuarios de ejemplo si no existen
User = get_user_model()
if not User.objects.filter(email='admin@duocuc.cl').exists():
    User.objects.create_superuser(
        email='admin@duocuc.cl',
        password='admin123',
        name='Administrador',
        role='admin_global',
        campus_id=1,
        career='Administración'
    )
    print('Usuario administrador creado')

if not User.objects.filter(email='moderator@duocuc.cl').exists():
    User.objects.create_user(
        email='moderator@duocuc.cl',
        password='moderator123',
        name='Moderador',
        role='moderator',
        campus_id=1,
        career='Ingeniería en Informática'
    )
    print('Usuario moderador creado')

if not User.objects.filter(email='student@duocuc.cl').exists():
    User.objects.create_user(
        email='student@duocuc.cl',
        password='student123',
        name='Estudiante',
        role='student',
        campus_id=1,
        career='Ingeniería en Informática'
    )
    print('Usuario estudiante creado')
"
    success "Datos iniciales poblados exitosamente"
}

# Función para verificar salud del sistema
health_check() {
    log "Verificando salud del sistema..."
    
    # Verificar que los contenedores estén corriendo
    if ! docker-compose -f docker-compose.prod.yml ps | grep -q "Up"; then
        error "Algunos contenedores no están corriendo"
    fi
    
    # Verificar que la aplicación responda
    if ! curl -f http://localhost/health/ > /dev/null 2>&1; then
        warning "La aplicación no responde en /health/"
    fi
    
    success "Sistema verificado exitosamente"
}

# Función para mostrar logs
show_logs() {
    log "Mostrando logs del sistema..."
    docker-compose -f docker-compose.prod.yml logs --tail=50
}

# Función para mostrar estado
show_status() {
    log "Estado del sistema:"
    docker-compose -f docker-compose.prod.yml ps
}

# Función para limpiar sistema
clean_system() {
    log "Limpiando sistema..."
    docker-compose -f docker-compose.prod.yml down
    docker system prune -f
    success "Sistema limpiado exitosamente"
}

# Función principal de deployment
deploy() {
    log "Iniciando deployment completo..."
    
    # Parar servicios existentes
    log "Parando servicios existentes..."
    docker-compose -f docker-compose.prod.yml down
    
    # Construir imágenes
    log "Construyendo imágenes Docker..."
    docker-compose -f docker-compose.prod.yml build --no-cache
    
    # Iniciar servicios
    log "Iniciando servicios..."
    docker-compose -f docker-compose.prod.yml up -d
    
    # Esperar a que los servicios estén listos
    log "Esperando a que los servicios estén listos..."
    sleep 30
    
    # Ejecutar migraciones
    run_migrations
    
    # Recolectar archivos estáticos
    collect_static
    
    # Crear superusuario
    create_superuser
    
    # Poblar datos iniciales
    populate_data
    
    # Verificar salud del sistema
    health_check
    
    success "Deployment completado exitosamente!"
    log "La aplicación está disponible en: http://localhost"
    log "Admin panel: http://localhost/admin/"
    log "API: http://localhost/api/"
}

# Función para actualización
update() {
    log "Iniciando actualización..."
    
    # Crear backup
    backup_database
    
    # Parar servicios
    docker-compose -f docker-compose.prod.yml down
    
    # Construir nuevas imágenes
    docker-compose -f docker-compose.prod.yml build
    
    # Iniciar servicios
    docker-compose -f docker-compose.prod.yml up -d
    
    # Esperar a que los servicios estén listos
    sleep 30
    
    # Ejecutar migraciones
    run_migrations
    
    # Recolectar archivos estáticos
    collect_static
    
    # Verificar salud del sistema
    health_check
    
    success "Actualización completada exitosamente!"
}

# Función para mostrar ayuda
show_help() {
    echo "DuocPoint Deployment Script"
    echo ""
    echo "Uso: $0 [COMANDO]"
    echo ""
    echo "Comandos disponibles:"
    echo "  deploy     - Deployment completo del sistema"
    echo "  update     - Actualizar sistema existente"
    echo "  backup     - Crear backup de la base de datos"
    echo "  migrate    - Ejecutar migraciones"
    echo "  static     - Recolectar archivos estáticos"
    echo "  superuser  - Crear superusuario"
    echo "  populate   - Poblar datos iniciales"
    echo "  health     - Verificar salud del sistema"
    echo "  logs       - Mostrar logs del sistema"
    echo "  status     - Mostrar estado del sistema"
    echo "  clean      - Limpiar sistema"
    echo "  help       - Mostrar esta ayuda"
    echo ""
}

# Procesar argumentos
case "${1:-deploy}" in
    deploy)
        deploy
        ;;
    update)
        update
        ;;
    backup)
        backup_database
        ;;
    migrate)
        run_migrations
        ;;
    static)
        collect_static
        ;;
    superuser)
        create_superuser
        ;;
    populate)
        populate_data
        ;;
    health)
        health_check
        ;;
    logs)
        show_logs
        ;;
    status)
        show_status
        ;;
    clean)
        clean_system
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        error "Comando desconocido: $1. Usa '$0 help' para ver comandos disponibles."
        ;;
esac
