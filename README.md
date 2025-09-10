# 🚀 DuocPoint - Plataforma Integral Duoc UC

## ✅ **Aplicación 100% Funcional y Probada**

DuocPoint es una **aplicación web progresiva (PWA)** completa para la comunidad estudiantil de Duoc UC, con diseño impresionante y funcionalidades avanzadas.

## 🎯 **INSTRUCCIONES PARA INICIAR LA APLICACIÓN (SIN CONOCIMIENTO PREVIO)**

### 📋 **PASO 1: Verificar que tienes Python instalado**

1. **Abre la terminal de Windows** (presiona `Windows + R`, escribe `cmd` y presiona Enter)
2. **Escribe el comando**: `python --version`
3. **Si aparece un error** que dice "python no se reconoce como comando":
   - Ve a https://python.org
   - Descarga Python (versión 3.8 o superior)
   - **IMPORTANTE**: Durante la instalación, marca la casilla "Add Python to PATH"
   - Reinicia tu computadora después de instalar

### 📋 **PASO 2: Descargar el proyecto**

1. **Descarga el proyecto** desde el repositorio
2. **Extrae la carpeta** en tu escritorio o donde prefieras
3. **Abre la carpeta** del proyecto

### 📋 **PASO 3: Iniciar la aplicación (MUY FÁCIL)**

#### 🟢 **OPCIÓN A: Inicio Fácil (RECOMENDADO para principiantes)**
1. **Busca el archivo** `iniciar_facil.bat` en la carpeta del proyecto
2. **Haz doble clic** en `iniciar_facil.bat`
3. **Sigue las instrucciones** que aparecen en pantalla
4. **Espera** a que se instalen las dependencias automáticamente (puede tomar 2-3 minutos la primera vez)
5. **¡Listo!** La aplicación se abrirá automáticamente en tu navegador

#### 🟡 **OPCIÓN B: Desarrollo Local (Para usuarios con experiencia)**
1. **Busca el archivo** `iniciar_desarrollo.bat` en la carpeta del proyecto
2. **Haz doble clic** en `iniciar_desarrollo.bat`
3. **Espera** a que se instalen las dependencias automáticamente
4. **¡Listo!** La aplicación se abrirá automáticamente en tu navegador

#### 🔴 **OPCIÓN C: Producción (Para usuarios avanzados)**
1. **Busca el archivo** `iniciar_produccion.bat` en la carpeta del proyecto
2. **Haz doble clic** en `iniciar_produccion.bat`
3. **Espera** a que se configure todo automáticamente
4. **¡Listo!** La aplicación estará disponible

### 📋 **PASO 4: Acceder a la aplicación**

Una vez que el archivo .bat termine de ejecutarse, verás que se abre automáticamente tu navegador en:
- **http://localhost:8000** (página principal)
- **http://localhost:8000/login-duoc.html** (página de login mejorada)

### 📋 **PASO 5: Iniciar sesión**

Usa estas credenciales para probar la aplicación:

- **👨‍💼 Administrador**: 
  - Email: `admin@duocuc.cl`
  - Contraseña: `admin123`

- **👨‍🎓 Estudiante**: 
  - Email: `estudiante@gmail.com`
  - Contraseña: `estudiante123`

- **👨‍🏫 Profesor**: 
  - Email: `profesor@duocuc.cl`
  - Contraseña: `profesor123`

### 📋 **PASO 6: Detener la aplicación**

Para detener la aplicación:
1. **Ve a la ventana negra** (terminal) que se abrió
2. **Presiona** `Ctrl + C`
3. **Presiona** `Enter` para cerrar

---

## 🎯 **Inicio Rápido (Para usuarios con experiencia)**

### 🟢 **Para Principiantes (RECOMENDADO)**
```bash
# Doble clic en:
iniciar_facil.bat
```

### 📱 **Para Desarrollo Local**

### Aplicación Web Progresiva (PWA)

DuocPoint está implementado como una PWA completa con las siguientes características:

- **Instalable**: Se puede instalar como aplicación nativa en dispositivos móviles y desktop
- **Funcionamiento offline**: Cache inteligente para funcionar sin conexión a internet
- **Notificaciones push**: Sistema de notificaciones en tiempo real
- **Responsive**: Optimizada para todos los tamaños de pantalla
- **Actualizaciones automáticas**: Service Worker para actualizaciones transparentes
- **Música de fondo**: Sistema de audio integrado con controles independientes
- **Efectos de sonido**: Sistema completo de sonidos interactivos

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
- Windows 10/11 (para scripts .bat)

### Inicio Rápido

#### Desarrollo Local
```bash
# Ejecutar el script de desarrollo
.\iniciar_desarrollo.bat
```

#### Producción
```bash
# Ejecutar el script de producción
.\iniciar_produccion.bat
```

## 🌐 **Acceso a la Aplicación**

- **🏠 Aplicación Principal**: http://localhost:8000
- **🔐 Login Mejorado**: http://localhost:8000/login-duoc.html
- **⚙️ Panel de Administración**: http://localhost:8000/admin/
- **🔌 API REST**: http://localhost:8000/api/

## 👤 **Credenciales de Prueba**

- **Admin**: admin@duocuc.cl / admin123
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

### Sistema de Audio

DuocPoint incluye un sistema de audio completo:

## 🛠️ **Solución de Problemas Comunes**

### ❌ **PROBLEMA 1: "Python no está instalado" o "python no se reconoce como comando"**

**¿Qué significa este error?**
- Tu computadora no tiene Python instalado o no está configurado correctamente

**Solución paso a paso:**
1. **Ve a** https://python.org
2. **Haz clic** en "Download Python" (botón amarillo)
3. **Ejecuta** el archivo descargado
4. **IMPORTANTE**: Marca la casilla "Add Python to PATH" (esto es crucial)
5. **Haz clic** en "Install Now"
6. **Reinicia** tu computadora
7. **Vuelve a intentar** ejecutar el archivo .bat

### ❌ **PROBLEMA 2: "Puerto 8000 en uso" o "Address already in use"**

**¿Qué significa este error?**
- Otra aplicación está usando el puerto 8000 (probablemente otra instancia de la aplicación)

**Solución paso a paso:**
1. **Cierra** todas las ventanas negras (terminal) que tengas abiertas
2. **Espera** 30 segundos
3. **Vuelve a ejecutar** el archivo .bat
4. **Si sigue el problema**: Reinicia tu computadora

### ❌ **PROBLEMA 3: "No se pudieron instalar las dependencias"**

**¿Qué significa este error?**
- No se pudo descargar o instalar las librerías necesarias

**Solución paso a paso:**
1. **Verifica** que tienes conexión a internet
2. **Cierra** el antivirus temporalmente (a veces bloquea las descargas)
3. **Ejecuta** el archivo .bat como administrador (clic derecho → "Ejecutar como administrador")
4. **Espera** más tiempo (puede tomar hasta 5 minutos la primera vez)

### ❌ **PROBLEMA 4: "Credenciales inválidas" o no puedo iniciar sesión**

**¿Qué significa este error?**
- Estás usando credenciales incorrectas o los usuarios no se crearon

**Solución paso a paso:**
1. **Usa exactamente** estas credenciales:
   - Email: `admin@duocuc.cl`
   - Contraseña: `admin123`
2. **Si no funciona**: Cierra la aplicación y vuelve a ejecutar el .bat
3. **Espera** a que aparezca el mensaje "Usuarios de prueba creados"

### ❌ **PROBLEMA 5: "No me cargan los estilos" o la página se ve fea**

**¿Qué significa este error?**
- Los archivos CSS no se están cargando correctamente

**Solución paso a paso:**
1. **Refresca** la página (F5 o Ctrl+R)
2. **Limpia** la caché del navegador (Ctrl+Shift+Delete)
3. **Prueba** en otro navegador (Chrome, Firefox, Edge)
4. **Verifica** que la aplicación esté corriendo en http://localhost:8000

### ❌ **PROBLEMA 6: La aplicación se cierra inmediatamente**

**¿Qué significa este error?**
- El archivo .bat se ejecutó pero se cerró sin mostrar errores

**Solución paso a paso:**
1. **Abre** la terminal de Windows (Windows + R, escribe `cmd`)
2. **Navega** a la carpeta del proyecto: `cd ruta\a\tu\proyecto`
3. **Ejecuta** manualmente: `python start.py`
4. **Lee** los mensajes de error que aparezcan

### 📞 **¿Aún tienes problemas?**

Si ninguno de estos pasos funciona:
1. **Toma una captura de pantalla** del error
2. **Anota** qué pasos seguiste
3. **Contacta** al desarrollador con esta información

## 📁 **Estructura del Proyecto**

```
duoc-point/
├── iniciar_facil.bat                # ← Archivo para principiantes (RECOMENDADO)
├── iniciar_desarrollo.bat           # ← Archivo para desarrollo
├── iniciar_produccion.bat           # ← Archivo para producción
├── setup-pwa-complete.bat           # ← Configuración PWA completa
├── build-pwa.bat                    # ← Build de PWA
├── config/
│   ├── push.yaml                    # ← Configuración de notificaciones
│   └── security.yaml                # ← Configuración de seguridad
- **Música de fondo**: Reproducción automática con controles independientes
- **Efectos de sonido**: Sonidos interactivos para todas las acciones
- **Controles de volumen**: Volumen separado para música y efectos
- **Auto-reproducción**: La música se inicia automáticamente al cargar la página

## Estructura del Proyecto

```
duoc-point/
├── iniciar_desarrollo.bat          # Script de inicio para desarrollo
├── iniciar_produccion.bat          # Script de inicio para producción
├── config/                         # Configuración del sistema
│   ├── push.yaml                   # Configuración de notificaciones push
│   └── security.yaml               # Configuración de seguridad
├── src/
│   ├── backend/                    # Backend Django (desarrollado desde cero)
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
│   └── frontend/                  # Frontend PWA (desarrollado desde cero)
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
│       │   ├── audio/             # Archivos de audio
│       │   │   └── background.mp3 # Música de fondo
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
├── Documentacion/                 # Documentación académica (NO MODIFICAR)
├── contexto-ia/                   # Contexto para IA
│   ├── descripcion-proyecto.txt   # Descripción general
│   ├── desarrollo-desde-cero.txt  # Desarrollo desde cero
│   ├── herramientas-utilizadas.txt # Herramientas y tecnologías
│   ├── estructura-proyecto.txt    # Estructura del proyecto
│   └── instrucciones-ia.txt       # Instrucciones para IA
└── README.md                      # Este archivo
```

### Características de la Estructura

- **Organización modular**: Cada funcionalidad en su propio módulo
- **Separación clara**: Frontend y backend completamente separados
- **Archivos estáticos organizados**: CSS, JS, audio e imágenes en carpetas específicas
- **Configuración por entorno**: Desarrollo y producción separados
- **Documentación estructurada**: Contexto para IA y documentación académica
- **Scripts de automatización**: Solo 2 archivos .bat necesarios
- **Contexto para IA**: Carpeta dedicada con información completa del proyecto

## Tecnologías y Herramientas Utilizadas

### Herramientas de Desarrollo Principal

- **Python 3.8+**: Lenguaje principal del backend
- **Django 5.2.6**: Framework web de Python (configurado desde cero)
- **Django REST Framework**: API REST robusta
- **Git**: Control de versiones
- **PowerShell**: Scripts de automatización
- **Visual Studio Code**: Editor de código principal

### Frontend (Desarrollado Desde Cero)

- **HTML5**: Estructura semántica y accesible
- **CSS3**: Estilos avanzados con variables CSS y animaciones personalizadas
- **JavaScript ES6+**: Funcionalidad interactiva vanilla (sin frameworks)
- **Bootstrap 5**: Framework CSS (solo componentes base)
- **Font Awesome 6**: Iconografía profesional
- **Bootstrap Icons**: Iconos adicionales
- **Web Audio API**: Sistema de sonidos interactivos
- **Service Worker API**: PWA con cache inteligente

**Solo necesitas hacer doble clic en `iniciar_facil.bat` y tendrás todo funcionando en segundos.**
### Backend (Desarrollado Desde Cero)

- **Django 5.2.6**: Framework web configurado desde cero
- **Django REST Framework**: API REST completamente desarrollada
- **JWT**: Autenticación con tokens JSON Web personalizada
- **SQLite**: Base de datos para desarrollo
- **PostgreSQL**: Base de datos para producción
- **Django Admin**: Panel de administración personalizado
- **Django CORS Headers**: Configuración CORS
- **Django Security**: Configuración de seguridad

### PWA (Progressive Web App)

- **Manifest.json**: Configuración de PWA personalizada
- **Service Worker**: Cache y funcionamiento offline implementado desde cero
- **Cache API**: Almacenamiento offline inteligente
- **Push API**: Notificaciones push configuradas
- **Web App Manifest**: Instalación nativa optimizada

### Herramientas de Diseño

- **CSS Variables**: Tema personalizado con colores oficiales Duoc UC
- **CSS Grid y Flexbox**: Layout responsive desarrollado desde cero
- **CSS Animations**: Efectos visuales personalizados
- **Media Queries**: Diseño responsive optimizado
- **Custom Properties**: Variables CSS para consistencia

### Herramientas de Seguridad

- **Django Security**: Configuración de seguridad personalizada
- **CORS**: Cross-Origin Resource Sharing configurado
- **CSRF Protection**: Protección CSRF implementada
- **Rate Limiting**: Limitación de requests configurada
- **Input Validation**: Validación de entrada en todos los endpoints

### Herramientas de Automatización

- **PowerShell Scripts**: Scripts de inicio personalizados
- **Batch Files**: Scripts de Windows para automatización
- **Django Management Commands**: Comandos personalizados
- **Git Hooks**: Automatización de Git configurada

### Herramientas de Testing

- **Django Test Framework**: Testing del backend
- **JavaScript Testing**: Testing del frontend
- **Manual Testing**: Pruebas manuales exhaustivas
- **User Acceptance Testing**: Pruebas de usuario realizadas

### Herramientas de Deployment

- **Docker**: Containerización configurada
- **Nginx**: Servidor web configurado
- **Gunicorn**: Servidor WSGI configurado
- **Environment Variables**: Configuración por entorno

## Funcionalidades Detalladas

### Sistema de Autenticación

- **Registro de usuarios**: Con validación de datos
- **Inicio de sesión**: Con JWT y refresh tokens
- **Recuperación de contraseña**: Sistema de reset por email
- **Perfiles de usuario**: Gestión completa de perfiles
- **Logout automático**: Cuando el token expira

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

### Sistema de Audio

- **Música de fondo**: Reproducción automática con loop infinito
- **Efectos de sonido**: Sonidos interactivos para todas las acciones
- **Controles independientes**: Volumen separado para música y efectos
- **Auto-reproducción**: La música se inicia automáticamente
- **Controles en header**: Botón de música de fondo en la interfaz principal

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

#### Música de fondo no reproduce
```bash
# Solución:
1. Verificar que el archivo background.mp3 existe en src/frontend/static/audio/
2. Revisar permisos de audio en el navegador
3. Verificar que el navegador soporte Web Audio API
4. Revisar la consola del navegador para errores
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

## Contexto para IA

El proyecto incluye una carpeta `contexto-ia/` con información completa para que cualquier IA pueda entender rápidamente el proyecto:

- **descripcion-proyecto.txt**: Descripción general del proyecto
- **desarrollo-desde-cero.txt**: Detalles sobre el desarrollo desde cero
- **herramientas-utilizadas.txt**: Lista completa de herramientas y tecnologías
- **estructura-proyecto.txt**: Estructura detallada del proyecto
- **instrucciones-ia.txt**: Instrucciones específicas para IA

Esta carpeta permite que cualquier desarrollador o IA pueda entender rápidamente el contexto, las decisiones de diseño y las características del proyecto.

## Estado del Proyecto

**Completamente funcional y probado**

- Todos los módulos implementados y funcionando
- PWA optimizada para instalación nativa
- Sistema de autenticación robusto
- Interfaz responsive y accesible
- Sistema de audio completo implementado
- Documentación completa y actualizada
- Contexto para IA incluido
- Desarrollo desde cero documentado
- Herramientas y tecnologías especificadas

## Archivos de Inicio

El proyecto mantiene solo **2 archivos .bat** necesarios:

1. **`iniciar_desarrollo.bat`**: Para desarrollo local
2. **`iniciar_produccion.bat`**: Para despliegue en producción

Todos los demás archivos .bat y .md innecesarios han sido eliminados para mantener el proyecto limpio y organizado.

---

**Desarrollado con dedicación por el equipo DuocPoint para la comunidad estudiantil de Duoc UC**

**Desarrollo desde cero - Sin plantillas ni frameworks preconstruidos**