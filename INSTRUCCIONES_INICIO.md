# 🚀 Instrucciones de Inicio Rápido - DuocPoint

## Inicio con un Solo Clic

### Opción 1: Inicio Completo (Recomendado)
```bash
# Doble clic en el archivo:
iniciar_duocpoint.bat
```

**¿Qué hace?**
- ✅ Verifica que Python esté instalado
- ✅ Instala/verifica todas las dependencias
- ✅ Ejecuta migraciones de base de datos
- ✅ Crea superusuario si no existe
- ✅ Carga datos iniciales
- ✅ Inicia el servidor en http://localhost:8000

### Opción 2: Inicio Rápido
```bash
# Doble clic en el archivo:
iniciar_rapido.bat
```

**¿Qué hace?**
- ✅ Inicia el servidor directamente
- ⚠️ Omite migraciones y configuración inicial
- ⚠️ Solo para uso cuando ya tienes todo configurado

## 🌐 Acceso a la Aplicación

Una vez iniciada, la aplicación estará disponible en:

- **Aplicación Principal**: http://localhost:8000
- **Panel de Administración**: http://localhost:8000/admin/
- **API REST**: http://localhost:8000/api/
- **Documentación API**: http://localhost:8000/api/docs/

## 👤 Credenciales por Defecto

- **Email**: admin@duocuc.cl
- **Contraseña**: admin123

## 📱 Funcionalidades Disponibles

### 🏠 Página Principal
- Dashboard con acceso a todos los módulos
- Navegación intuitiva
- Estado de conexión en tiempo real

### 📚 Módulos Principales
1. **Foros** - Comunicación por carrera y sede
2. **Mercado** - Compra/venta de productos
3. **Portafolio** - Gestión profesional
4. **Recorridos** - Mapas interactivos 360°
5. **Bienestar** - Rutinas de kinesiología
6. **Reportes** - Problemas de infraestructura
7. **Cursos** - Cursos OTEC y abiertos
8. **Encuestas** - Votaciones comunitarias
9. **Horarios** - Importación de PDFs
10. **Notificaciones** - Sistema de alertas

### 🔧 Características Técnicas
- **PWA**: Instalable como app nativa
- **Offline**: Funciona sin conexión
- **Responsive**: Adaptado a móviles
- **JWT**: Autenticación segura
- **API REST**: Documentada con Swagger

## 🛠️ Solución de Problemas

### Error: "Python no está instalado"
```bash
# Descarga Python desde: https://python.org
# Asegúrate de marcar "Add Python to PATH" durante la instalación
```

### Error: "No se pudieron instalar las dependencias"
```bash
# Verifica tu conexión a internet
# Ejecuta como administrador si es necesario
```

### Error: "Puerto 8000 en uso"
```bash
# Cierra otras aplicaciones que usen el puerto 8000
# O modifica el puerto en start.py
```

### La aplicación no carga
```bash
# Verifica que el firewall no bloquee el puerto 8000
# Asegúrate de que no hay otros servidores ejecutándose
```

## 📁 Estructura del Proyecto

```
duoc-point/
├── iniciar_duocpoint.bat      # ← Archivo principal de inicio
├── iniciar_rapido.bat         # ← Inicio rápido
├── config_local.env           # ← Configuración local
├── start.py                   # ← Script de inicio Python
├── src/
│   ├── backend/              # Backend Django
│   └── frontend/             # Frontend PWA
└── deployment/               # Configuración Docker
```

## 🔄 Actualizaciones

Para actualizar la aplicación:
1. Descarga la nueva versión
2. Ejecuta `iniciar_duocpoint.bat`
3. Las migraciones se ejecutarán automáticamente

## 📞 Soporte

Si tienes problemas:
1. Revisa esta documentación
2. Verifica que Python esté instalado correctamente
3. Asegúrate de tener conexión a internet
4. Ejecuta como administrador si es necesario

---

**Desarrollado con ❤️ por el equipo DuocPoint**  
**Versión**: 1.2.0  
**Última actualización**: Enero 2025
