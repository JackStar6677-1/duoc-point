# 🎓 DuocPoint - Plataforma Integral Duoc UC

Plataforma integral para la comunidad estudiantil de Duoc UC que integra foros, mercado, portafolio profesional y recorridos virtuales.

## 🚀 Inicio Súper Rápido

### Un Solo Comando

```bash
# 1. Clonar repositorio
git clone https://github.com/JackStar6677-1/duoc-point.git
cd duoc-point

# 2. Instalar todo (una sola vez)
python install.py

# 3. Iniciar DuocPoint (PWA completo)
python start.py
```

¡Eso es todo! 🎉

## 📱 PWA en Móvil

### Para PWA completo en móvil:

```bash
# Con ngrok (HTTPS)
python start.py ngrok

# O solo localhost
python start.py local
```

### URLs Disponibles:
- **💻 Local**: http://localhost:8000/ (PWA completo)
- **📱 Red Local**: http://192.168.x.x:8000/ (PWA limitado)
- **🌍 HTTPS**: https://xxxxx.ngrok.io (PWA completo en móvil)

## 🔐 Credenciales de Prueba

- **Email**: `student@duocuc.cl`
- **Password**: `student123`

- **Email**: `moderator@duocuc.cl`
- **Password**: `moderator123`

- **Email**: `admin@duocuc.cl`
- **Password**: `admin123`

## 🧪 Testing

```bash
# Tests completos
python start.py test

# Test PWA
http://localhost:8000/test-all.html
```

## 📊 Características Completas

- **🔐 Autenticación JWT**: Login/registro funcionando
- **💬 Foros**: Comunicación por carrera y sede
- **🛒 Mercado**: Compra/venta entre estudiantes
- **📁 Portafolio**: Perfil profesional automático
- **🏫 Recorridos Virtuales**: Street View personalizado
- **📱 PWA**: Instalable como app nativa
- **🔔 Notificaciones**: Push notifications completas
- **👥 Moderación**: Sistema de moderación automática
- **👨‍🏫 Profesores**: Información de profesores
- **🏢 Sedes**: Información de campus
- **👤 Cuenta**: Gestión de perfil de usuario

## 🌐 Despliegue en Producción

### AMP Cubecoders (Ejemplo)

```bash
# 1. Subir código al servidor
git clone https://github.com/JackStar6677-1/duoc-point.git
cd duoc-point

# 2. Instalar dependencias
python install.py

# 3. Configurar variables de entorno
export DEBUG=False
export SECRET_KEY="tu-secret-key"
export DATABASE_URL="postgresql://user:pass@host:port/db"

# 4. Iniciar con Gunicorn
cd server
gunicorn duocpoint.wsgi:application --bind 0.0.0.0:8000

# 5. Configurar Nginx (opcional)
# /etc/nginx/sites-available/duocpoint
server {
    listen 80;
    server_name tu-dominio.com;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
    
    location /static/ {
        alias /path/to/duoc-point/server/staticfiles/;
    }
}
```

## 🔧 Comandos Disponibles

```bash
# Iniciar todo (localhost + red local + ngrok)
python start.py all

# Solo localhost (PWA completo)
python start.py local

# Solo red local
python start.py network

# Con ngrok (HTTPS para móvil)
python start.py ngrok

# Con Tailscale (HTTPS para móvil - RECOMENDADO)
python start.py tailscale
# O directamente:
python start_tailscale.py

# Solo tests
python start.py test
```

## 📱 PWA Installation

### Con Tailscale (RECOMENDADO):
1. **Ejecuta**: `python start_tailscale.py`
2. **Ve a la URL HTTPS de Tailscale en tu móvil**
3. **Deberías ver "Instalar App"**
4. **La app se instalará como aplicación nativa**

### Con localhost:
1. **Ve a http://localhost:8000/ en Chrome móvil**
2. **Deberías ver "Instalar App" en lugar de "Añadir acceso directo"**
3. **La app se instalará como aplicación nativa**
4. **Aparecerá en tu escritorio con el icono de DuocPoint**

## 🧪 Páginas de Test

- **http://localhost:8000/test-all.html** - Test completo
- **http://localhost:8000/test-pwa.html** - Test solo PWA
- **http://localhost:8000/login.html** - Login
- **http://localhost:8000/forum/** - Foros
- **http://localhost:8000/market/** - Mercado
- **http://localhost:8000/portfolio/** - Portafolio

## 📝 API Documentation

- **Swagger UI**: http://localhost:8000/api/docs/
- **Schema**: http://localhost:8000/api/schema/

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👥 Equipo

- **Desarrollador Principal**: Pablo Elías Miranda
- **Institución**: Duoc UC
- **Proyecto**: Capstone - Ingeniería en Informática

## 📞 Soporte

Para soporte, contacta a [pablo.elias.miranda.292003@gmail.com](mailto:pablo.elias.miranda.292003@gmail.com)

---

## 🎉 ¡DuocPoint está 100% funcional!

**Versión**: 1.2.0  
**Estado**: ✅ Completamente funcional  
**PWA**: ✅ Instalable en móvil  
**API**: ✅ Todas las funcionalidades  
**Base de datos**: ✅ Poblada con datos de prueba