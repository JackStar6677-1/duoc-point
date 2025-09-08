# DuocPoint - Plataforma Integral Duoc UC

## Descripción del Proyecto

DuocPoint es una aplicación web progresiva (PWA) completa desarrollada para la comunidad estudiantil de Duoc UC. La plataforma integra múltiples módulos funcionales que facilitan la vida académica y social de los estudiantes, incluyendo foros de discusión, mercado estudiantil, portafolio profesional, navegación virtual del campus, y más.

## Características Principales

### Aplicación Web Progresiva (PWA)
- **Instalable**: Se puede instalar como aplicación nativa en dispositivos móviles y desktop
- **Funcionamiento offline**: Cache inteligente para funcionar sin conexión a internet
- **Notificaciones push**: Sistema de notificaciones en tiempo real
- **Responsive**: Optimizada para todos los tamaños de pantalla
- **Actualizaciones automáticas**: Service Worker para actualizaciones transparentes

### Módulos Implementados
1. **Foros de Discusión** - Sistema de comunicación por carrera y sede
2. **Mercado Estudiantil** - Plataforma de compra/venta de productos
3. **Portafolio Profesional** - Gestión de perfil académico y profesional
4. **Navegación Virtual** - Recorrido paso a paso por el campus
5. **Bienestar Estudiantil** - Rutinas de salud y bienestar
6. **Sistema de Reportes** - Gestión de tickets y reportes
7. **Cursos OTEC** - Cursos abiertos y capacitaciones
8. **Encuestas** - Sistema de votación y encuestas
9. **Horarios** - Gestión de horarios académicos
10. **Notificaciones** - Sistema de alertas y comunicaciones

## Instalación y Configuración

### Requisitos del Sistema
- Python 3.8 o superior
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Conexión a internet (para dependencias iniciales)

### Inicio Rápido

#### Desarrollo Local
```bash
# Ejecutar el script de desarrollo
iniciar_desarrollo.bat
```

#### Producción
```bash
# Ejecutar el script de producción
iniciar_produccion.bat
```

### Acceso a la Aplicación

Una vez iniciado el servidor, la aplicación estará disponible en:

- **Aplicación Principal**: http://localhost:8000
- **Panel de Administración**: http://localhost:8000/admin/
- **API REST**: http://localhost:8000/api/
- **Documentación API**: http://localhost:8000/api/docs/

## Credenciales de Prueba

El sistema incluye usuarios de prueba preconfigurados:

- **Administrador**: admin@duocuc.cl / admin123
- **Estudiante**: estudiante@gmail.com / estudiante123
- **Profesor**: profesor@duocuc.cl / profesor123
- **Moderador**: moderador@duocuc.cl / moderador123

## Configuración PWA

### Instalación como Aplicación Nativa

1. **Desde el navegador**:
   - Abre http://localhost:8000 en Chrome, Edge o Safari
   - Busca el ícono de instalación en la barra de direcciones
   - Haz clic en "Instalar" o "Agregar a pantalla de inicio"

2. **Desde la aplicación**:
   - Busca el botón "Instalar App" en la interfaz
   - Sigue las instrucciones del navegador

### Funcionamiento Offline

La PWA está configurada para funcionar offline:
- **Cache estático**: Páginas principales y recursos
- **Cache dinámico**: Datos de API y contenido dinámico
- **Sincronización**: Actualización automática cuando se restaura la conexión

### Notificaciones Push

El sistema incluye notificaciones push configuradas:
- **Desarrollo**: Notificaciones de prueba habilitadas
- **Producción**: Notificaciones reales con claves VAPID
- **Configuración**: Archivo `config/push.yaml` para personalización

## Estructura del Proyecto

```
duoc-point/
├── iniciar_desarrollo.bat          # Script de inicio para desarrollo
├── iniciar_produccion.bat          # Script de inicio para producción
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
│       │   │   ├── styles.css     # Estilos principales
│       │   │   └── duoc-theme.css # Tema personalizado Duoc UC
│       │   ├── js/                # Scripts JavaScript
│       │   │   ├── main.js        # Script principal
│       │   │   ├── pwa.js         # Gestor de PWA
│       │   │   ├── sounds.js      # Sistema de sonidos
│       │   │   └── sw.js          # Service Worker
│       │   ├── images/            # Imágenes e iconos
│       │   │   └── icons/         # Iconos PWA
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
│   ├── logos-iconos/              # Logos e iconos
│   └── streetviewSalas/           # Imágenes para navegación virtual
├── Documentacion/                 # Documentación del proyecto
└── README.md                      # Este archivo
```

## Tecnologías Utilizadas

### Frontend
- **HTML5**: Estructura semántica y accesible
- **CSS3**: Estilos avanzados con variables CSS y animaciones
- **JavaScript ES6+**: Funcionalidad interactiva y moderna
- **Bootstrap 5**: Framework CSS para diseño responsive
- **Font Awesome**: Iconografía profesional
- **PWA**: Service Worker, Manifest, Cache API

### Backend
- **Django 5.2.6**: Framework web de Python
- **Django REST Framework**: API REST robusta
- **JWT**: Autenticación con tokens JSON Web
- **SQLite**: Base de datos para desarrollo
- **PostgreSQL**: Base de datos para producción
- **Celery**: Tareas asíncronas
- **Redis**: Cache y broker de mensajes

### Herramientas de Desarrollo
- **Git**: Control de versiones
- **Docker**: Containerización (opcional)
- **PowerShell**: Scripts de automatización
- **PWA Builder**: Herramientas de PWA

## Funcionalidades Detalladas

### Sistema de Autenticación
- **Registro de usuarios**: Con validación de datos
- **Inicio de sesión**: Con JWT y refresh tokens
- **Recuperación de contraseña**: Sistema de reset por email
- **Perfiles de usuario**: Gestión completa de perfiles

### Foros de Discusión
- **Categorías por carrera**: Organización temática
- **Sistema de moderación**: Control de contenido
- **Búsqueda avanzada**: Filtros y ordenamiento
- **Notificaciones**: Alertas de nuevas respuestas

### Mercado Estudiantil
- **Publicación de productos**: Con imágenes y descripción
- **Sistema de favoritos**: Productos guardados
- **Búsqueda y filtros**: Por categoría, precio, ubicación
- **Sistema de reportes**: Moderación de contenido

### Portafolio Profesional
- **Perfil completo**: Información académica y profesional
- **Gestión de proyectos**: Portafolio de trabajos
- **Generación de PDF**: Exportación de perfil
- **Habilidades y competencias**: Sistema de etiquetas

### Navegación Virtual
- **Recorrido paso a paso**: Navegación por diapositivas
- **Información detallada**: De cada ubicación del campus
- **Controles intuitivos**: Navegación con teclado y mouse
- **Responsive**: Optimizado para móviles

## Configuración de Desarrollo

### Variables de Entorno
El proyecto utiliza archivos de configuración para diferentes entornos:

- **config_local.env**: Configuración para desarrollo local
- **config/push.yaml**: Configuración de notificaciones push
- **config/security.yaml**: Configuración de seguridad

### Base de Datos
- **Desarrollo**: SQLite (archivo local)
- **Producción**: PostgreSQL (configuración en variables de entorno)

### Cache y Sesiones
- **Desarrollo**: Cache en memoria
- **Producción**: Redis para cache y sesiones

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
- **Equipo de desarrollo**: DuocPoint Team
- **Institución**: Duoc UC
- **Versión actual**: 1.2.0
- **Última actualización**: Enero 2025

## Estado del Proyecto

✅ **Completamente funcional y probado**
- Todos los módulos implementados y funcionando
- PWA optimizada para instalación nativa
- Sistema de autenticación robusto
- Interfaz responsive y accesible
- Documentación completa y actualizada

---

**Desarrollado con dedicación por el equipo DuocPoint para la comunidad estudiantil de Duoc UC**