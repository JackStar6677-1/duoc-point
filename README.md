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
```bash
# Doble clic en:
iniciar_desarrollo.bat
```

### 🏭 **Para Producción**
```bash
# Doble clic en:
iniciar_produccion.bat
```

### 📱 **Para Configurar PWA**
```bash
# Doble clic en:
setup-pwa-complete.bat
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

## 🎨 **Características del Diseño**

### 🌟 **Tema Personalizado Duoc UC**
- **Colores oficiales**: Dorado (#D4AF37), Morado (#4A148C), Azul (#1565C0)
- **Animaciones profesionales**: Efectos hover, transiciones suaves, animaciones 3D
- **Responsive**: Perfecto en móviles y desktop
- **PWA**: Instalable como aplicación nativa

### 🎭 **Animaciones Implementadas**
- **Fade In Up**: Entrada suave desde abajo
- **Slide In Left/Right**: Deslizamiento lateral
- **Hover Effects**: Transformaciones 3D
- **Pulse**: Efectos de pulso en iconos
- **Glow**: Efectos de brillo
- **Float**: Animaciones flotantes

## 📚 **Módulos Implementados**

1. **💬 Foros** - Sistema de discusión por carrera y sede
2. **🛒 Mercado** - Compra/venta de productos
3. **💼 Portafolio** - Gestión profesional
4. **🗺️ Recorridos Virtuales** - Mapas interactivos 360°
5. **❤️ Bienestar Estudiantil** - Rutinas de salud
6. **📊 Reportes** - Sistema de tickets
7. **📚 Cursos OTEC** - Cursos abiertos
8. **📋 Encuestas** - Sistema de votación
9. **⏰ Horarios** - Gestión de horarios
10. **🔔 Notificaciones** - Sistema de alertas

## 🔧 **Características Técnicas**

### 🎨 **Frontend**
- **Tema personalizado**: Colores oficiales de Duoc UC
- **Animaciones CSS**: Efectos profesionales y fluidos
- **Responsive design**: Perfecto en todos los dispositivos
- **PWA optimizada**: Service worker mejorado
- **Performance**: Carga rápida y optimizada

### ⚙️ **Backend**
- **Django 5.2.6** con Django REST Framework
- **Autenticación JWT** con refresh tokens
- **API REST** completamente documentada
- **Base de datos** SQLite (desarrollo) / PostgreSQL (producción)
- **Cache Redis** para optimización
- **Celery** para tareas asíncronas

### 🔒 **Seguridad**
- **Validación de entrada** en todos los endpoints
- **Rate limiting** para prevenir abuso
- **CORS** configurado correctamente
- **Sanitización** de contenido HTML
- **Encriptación** de contraseñas con bcrypt

## 📱 **PWA (Progressive Web App)**

### ✅ **Características PWA**
- **Instalable**: Como aplicación nativa desde el navegador
- **Offline**: Funciona sin conexión a internet
- **Notificaciones**: Push notifications
- **Cache inteligente**: Almacenamiento optimizado
- **Actualizaciones**: Automáticas y transparentes

### 🚀 **Instalación PWA**
1. Abre http://localhost:8000 en Chrome/Edge
2. Haz clic en el botón "Instalar" en la barra de direcciones
3. O usa el botón "Instalar App" en la aplicación
4. La PWA se instalará como aplicación nativa

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
├── src/
│   ├── backend/                     # Backend Django
│   │   ├── duocpoint/              # Configuración principal
│   │   ├── apps/                   # Aplicaciones del sistema
│   │   ├── create_test_users.py    # ← Script de usuarios de prueba
│   │   └── requirements.txt        # Dependencias Python
│   └── frontend/                   # Frontend PWA
│       ├── index.html              # Página principal
│       ├── login-duoc.html         # ← Login mejorado
│       ├── duoc-theme.css          # ← Tema personalizado
│       ├── manifest.json           # Manifest PWA
│       ├── sw.js                   # Service Worker
│       ├── pwa.js                  # PWA Manager
│       └── [módulos]/              # Módulos de funcionalidad
└── README.md                       # ← Este archivo
```

## 🔄 **Actualizaciones**

Para actualizar la aplicación:
1. Descarga la nueva versión
2. Ejecuta `iniciar_desarrollo.bat`
3. Las migraciones se ejecutarán automáticamente
4. Los usuarios de prueba se recrearán

## 📞 **Soporte**

Si tienes problemas:
1. Revisa esta documentación
2. Verifica que Python esté instalado correctamente
3. Asegúrate de tener conexión a internet
4. Ejecuta como administrador si es necesario

## 🎉 **¡Tu aplicación está lista!**

**DuocPoint** es una aplicación web progresiva completa con:

✅ **Diseño impresionante** con colores oficiales de Duoc UC  
✅ **Animaciones profesionales** y efectos visuales  
✅ **Sistema de login funcional** con usuarios de prueba  
✅ **PWA optimizada** para instalación nativa  
✅ **Todas las funcionalidades** implementadas  
✅ **Completamente probada** y verificada  

**Solo necesitas hacer doble clic en `iniciar_facil.bat` y tendrás todo funcionando en segundos.**

---

**Desarrollado con ❤️ por el equipo DuocPoint**  
**Versión**: 1.2.0  
**Última actualización**: Enero 2025  
**Estado**: ✅ Completamente funcional y probado