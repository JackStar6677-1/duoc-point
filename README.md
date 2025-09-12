# StudentsPoint - Plataforma Integral Estudiantil

## Aplicación Web Progresiva (PWA) Completa

StudentsPoint es una aplicación web progresiva desarrollada desde cero para la comunidad estudiantil global. La plataforma integra múltiples módulos funcionales con un diseño responsive y arquitectura moderna, inspirada en sistemas como Blackboard pero con un enfoque open-source.

## Características Principales

- **Aplicación Web Progresiva (PWA)**: Instalable como aplicación nativa
- **Arquitectura Full-Stack**: Backend Django con API REST y Frontend vanilla
- **Funcionamiento Offline**: Cache inteligente con Service Worker
- **Sistema de Audio**: Música de fondo y efectos de sonido interactivos
- **Notificaciones Push**: Sistema de alertas en tiempo real
- **Diseño Responsive**: Optimizado para todos los dispositivos

## Módulos Implementados

1. **Sistema de Foros**: Comunicación por carrera y sede
2. **Mercado Estudiantil**: Plataforma de compra/venta de productos
3. **Portafolio Profesional**: Gestión de perfil académico y profesional
4. **Navegación Virtual**: Recorrido interactivo por el campus
5. **Bienestar Estudiantil**: Rutinas de salud y bienestar
6. **Sistema de Reportes**: Gestión de tickets y reportes
7. **Cursos OTEC**: Cursos abiertos y capacitaciones
8. **Sistema de Encuestas**: Votación y encuestas interactivas
9. **Gestión de Horarios**: Horarios académicos
10. **Sistema de Notificaciones**: Alertas y comunicaciones

## Requisitos del Sistema

- Python 3.8 o superior
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Conexión a internet (para dependencias iniciales)
- Windows 10/11 (para scripts de automatización)

## Instalación y Configuración

### Opción 1: Instalación Automática (Recomendado)

Para usuarios sin experiencia técnica:

1. Descargar el proyecto desde el repositorio
2. Extraer la carpeta en el escritorio
3. Ejecutar `iniciar_desarrollo.bat` con doble clic
4. Esperar la instalación automática
5. La aplicación se abrirá automáticamente en el navegador

### Opción 2: Instalación Manual

#### Paso 1: Instalar Python
```bash
# Windows (PowerShell como Administrador)
winget install Python.Python.3.11

# Verificar instalación
python --version
pip --version
```

#### Paso 2: Instalar Git
```bash
# Windows (PowerShell como Administrador)
winget install Git.Git

# Verificar instalación
git --version
```

#### Paso 3: Clonar el Proyecto
```bash
# Clonar repositorio
git clone https://github.com/JackStar6677-1/students-point.git
cd students-point

# Cambiar a branch de desarrollo
git checkout main
```

#### Paso 4: Instalar Dependencias
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r src/backend/requirements.txt
```

#### Paso 5: Configurar Base de Datos
```bash
# Ir al directorio del backend
cd src/backend

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Crear usuarios de prueba
python create_test_users.py
```

#### Paso 6: Iniciar Servidor
```bash
# Iniciar servidor de desarrollo
python manage.py runserver 0.0.0.0:8000

# O usar el script de inicio
cd ../..
python start.py
```

## Configuración de Red

### Detección Automática de IP

El sistema incluye detección automática de IP local:

- **Detección automática**: El sistema detecta la IP local del PC
- **Configuración independiente**: Cada PC tiene su propia configuración
- **Acceso desde otros dispositivos**: Disponible desde otros dispositivos en la red local
- **Sin configuración manual**: Todo es automático

### URLs de Acceso

#### Acceso Local
- **Aplicación Principal**: http://localhost:8000
- **Panel de Administración**: http://localhost:8000/admin/
- **API REST**: http://localhost:8000/api/

#### Acceso desde Red Local
- **IP detectada automáticamente**: http://[IP-LOCAL]:8000
- **Acceso desde otros dispositivos**: Móviles, tablets, otras PCs en la misma red

## Credenciales de Prueba

- **Administrador**: admin@studentspoint.app / admin123
- **Estudiante**: estudiante@gmail.com / estudiante123
- **Profesor**: profesor@studentspoint.app / profesor123
- **Moderador**: moderador@studentspoint.app / moderador123

## Estructura del Proyecto

```
students-point/
├── iniciar_desarrollo.bat          # Script de inicio para desarrollo
├── iniciar_produccion.bat          # Script de inicio para producción
├── detect_ip.py                    # Detector automático de IP local
├── update_django_config.py         # Actualizador de configuración Django
├── test_config.py                  # Script de prueba de configuración
├── start.py                        # Iniciador del servidor
├── config/                         # Configuración del sistema
│   ├── push.yaml                   # Configuración de notificaciones push
│   └── security.yaml               # Configuración de seguridad
├── src/
│   ├── backend/                    # Backend Django
│   │   ├── duocpoint/             # Configuración principal de Django
│   │   ├── apps/                  # Aplicaciones del sistema
│   │   │   ├── accounts/          # Gestión de usuarios
│   │   │   ├── forum/             # Sistema de foros
│   │   │   ├── market/            # Mercado estudiantil
│   │   │   ├── portfolio/         # Portafolio profesional
│   │   │   ├── polls/             # Sistema de encuestas
│   │   │   ├── reports/           # Sistema de reportes
│   │   │   ├── schedules/         # Gestión de horarios
│   │   │   ├── otec/              # Cursos OTEC
│   │   │   ├── wellbeing/         # Bienestar estudiantil
│   │   │   ├── campuses/          # Gestión de sedes
│   │   │   └── notifications/     # Sistema de notificaciones
│   │   ├── create_test_users.py   # Script para crear usuarios de prueba
│   │   └── requirements.txt       # Dependencias de Python
│   └── frontend/                  # Frontend PWA
│       ├── index.html             # Página principal
│       ├── login.html             # Página de inicio de sesión
│       ├── register.html          # Página de registro
│       ├── static/                # Archivos estáticos organizados
│       │   ├── css/               # Hojas de estilo
│       │   ├── js/                # Scripts JavaScript
│       │   ├── audio/             # Archivos de audio
│       │   ├── images/            # Imágenes e iconos
│       │   ├── manifest.json      # Manifest de la PWA
│       │   └── pwa-config.js      # Configuración PWA
│       ├── forum/                 # Módulo de foros
│       ├── market/                # Módulo de mercado
│       ├── portfolio/             # Módulo de portafolio
│       ├── streetview/            # Navegación virtual
│       ├── bienestar/             # Bienestar estudiantil
│       ├── encuestas/             # Sistema de encuestas
│       ├── reportes/              # Sistema de reportes
│       ├── cursos/                # Cursos OTEC
│       └── horarios/              # Gestión de horarios
├── imagenes/                      # Imágenes del proyecto
├── Documentacion/                 # Documentación académica
└── README.md                      # Este archivo
```

## Tecnologías Utilizadas

### Backend
- **Python 3.8+**: Lenguaje principal
- **Django 5.2.6**: Framework web
- **Django REST Framework**: API REST
- **JWT**: Autenticación con tokens
- **SQLite**: Base de datos para desarrollo
- **PostgreSQL**: Base de datos para producción

### Frontend
- **HTML5**: Estructura semántica
- **CSS3**: Estilos avanzados con variables CSS
- **JavaScript ES6+**: Funcionalidad interactiva vanilla
- **Bootstrap 5**: Framework CSS
- **Font Awesome 6**: Iconografía
- **Web Audio API**: Sistema de sonidos
- **Service Worker API**: PWA con cache inteligente

### PWA
- **Manifest.json**: Configuración de PWA
- **Service Worker**: Cache y funcionamiento offline
- **Cache API**: Almacenamiento offline inteligente
- **Push API**: Notificaciones push

## Configuración PWA

### Instalación como Aplicación Nativa

1. **Desde el navegador**:
   - Abrir http://localhost:8000 en Chrome, Edge o Safari
   - Buscar el ícono de instalación en la barra de direcciones
   - Hacer clic en "Instalar" o "Agregar a pantalla de inicio"

2. **Desde la aplicación**:
   - Buscar el botón "Instalar App" en la interfaz
   - Seguir las instrucciones del navegador

### Funcionamiento Offline

La PWA está configurada para funcionar offline:

- **Cache estático**: Páginas principales y recursos
- **Cache dinámico**: Datos de API y contenido dinámico
- **Sincronización**: Actualización automática cuando se restaura la conexión

## Despliegue en Producción

### Configuración para AMP (CubeCoders)

#### Variables de Entorno
```env
DEBUG=False
SECRET_KEY=tu_secret_key_muy_segura
DB_ENGINE=django.db.backends.postgresql
DB_NAME=duocpoint_prod
DB_USER=postgres
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=tu-dominio.com,localhost
```

#### Script de Inicio
```bash
#!/bin/bash
pip install -r src/backend/requirements.txt
python src/backend/manage.py migrate --settings=duocpoint.settings.production
python src/backend/manage.py collectstatic --settings=duocpoint.settings.production --noinput
cd src/backend
gunicorn --bind 0.0.0.0:8000 --workers 4 duocpoint.wsgi:application
```

## Solución de Problemas

### Problemas Comunes

#### Error: "Python no está instalado"
```bash
# Solución:
1. Descargar Python desde: https://python.org
2. Durante la instalación, marcar "Add Python to PATH"
3. Reiniciar la terminal
4. Ejecutar el script .bat nuevamente
```

#### Error: "Puerto 8000 en uso"
```bash
# Solución:
1. Cerrar otras aplicaciones que usen el puerto 8000
2. O modificar el puerto en start.py
3. Reiniciar el script .bat
```

#### PWA no se instala
```bash
# Solución:
1. Usar localhost en lugar de IP local
2. Verificar que el navegador soporte PWA
3. Revisar la consola del navegador para errores
4. Verificar que el manifest.json sea válido
```

#### Notificaciones no funcionan
```bash
# Solución:
1. Verificar permisos de notificación en el navegador
2. Revisar configuración en config/push.yaml
3. Verificar claves VAPID válidas
4. Comprobar conexión a internet
```

## Contribución

### Cómo Contribuir

1. Fork del repositorio
2. Crear rama para nueva funcionalidad
3. Realizar cambios y pruebas
4. Crear pull request con descripción detallada

### Estándares de Código

- **Python**: PEP 8
- **JavaScript**: ESLint con configuración estándar
- **CSS**: BEM methodology
- **HTML**: Estructura semántica

## Licencia

Este proyecto está desarrollado para Duoc UC y su uso está restringido a fines académicos y educativos.

## Contacto y Soporte

Para soporte técnico o consultas sobre el proyecto:

- **Equipo de desarrollo**: StudentsPoint Team
- **Proyecto**: Open Source
- **Versión actual**: 1.2.0
- **Última actualización**: Enero 2025

## Estado del Proyecto

**Completamente funcional y probado**

- Todos los módulos implementados y funcionando
- PWA optimizada para instalación nativa
- Sistema de autenticación robusto
- Interfaz responsive y accesible
- Sistema de audio completo implementado
- Documentación completa y actualizada
- Desarrollo desde cero documentado

---

**Desarrollado por el equipo StudentsPoint para la comunidad estudiantil global**

**Desarrollo desde cero - Proyecto Open Source sin plantillas ni frameworks preconstruidos**