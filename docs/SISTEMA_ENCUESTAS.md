# Sistema de Encuestas DuocPoint

## Descripción General

El sistema de encuestas de DuocPoint es una solución completa que permite a moderadores y directores crear encuestas interactivas con capacidades avanzadas de análisis y filtrado por sede/carrera.

## Características Principales

### ✅ Funcionalidades Implementadas

#### 1. **Creación de Encuestas Avanzadas**
- **Tipos de encuesta**: Selección única o múltiple
- **Configuración flexible**: Votos anónimos, justificación requerida
- **Filtros por audiencia**: Restricción por sede y/o carrera
- **Control de visibilidad**: Resultados en tiempo real, al cierre, o solo moderadores
- **Programación**: Fechas de inicio y cierre automáticas

#### 2. **Sistema de Votación Seguro**
- **Validación única**: Un voto por usuario por encuesta
- **Metadatos de auditoría**: IP, User-Agent, timestamp
- **Justificación opcional**: Comentarios en votos cuando se requiere
- **Verificación de permisos**: Validación automática por sede/carrera

#### 3. **Análisis y Estadísticas**
- **Analytics en tiempo real**: Distribución por sede y carrera
- **Gráficos interactivos**: Visualización con Chart.js
- **Exportación CSV**: Datos completos con metadatos
- **Dashboard ejecutivo**: Estadísticas generales del sistema

#### 4. **Interfaz Responsive**
- **PWA Ready**: Funciona como app móvil instalable
- **Gráficos dinámicos**: Barras y dona interactivos
- **Filtros avanzados**: Por estado, fecha, búsqueda
- **UX optimizada**: Modales, toasts, animaciones

#### 5. **Seguridad y Validaciones**
- **Autenticación JWT**: Tokens seguros
- **Permisos granulares**: Roles diferenciados
- **Validaciones robustas**: Frontend y backend
- **Auditoría completa**: Logs de todas las acciones

## Arquitectura Técnica

### Backend (Django)

```
duocpoint/apps/polls/
├── models.py          # Modelos mejorados con analytics
├── serializers.py     # Serialización completa y exportación
├── views.py          # API REST con filtros avanzados
├── urls.py           # Endpoints organizados
├── admin.py          # Administración avanzada
└── tests.py          # Tests comprehensivos
```

#### Modelos Principales

**Poll (Encuesta)**
- Campos básicos: título, descripción, creador
- Configuración: multi, anónima, requiere justificación
- Filtros: sedes, carreras (JSONField)
- Estado: borrador, activa, cerrada, archivada
- Visibilidad: tiempo real, al cierre, solo moderador

**PollOpcion (Opción)**
- Texto y descripción
- Color para gráficos
- Orden de visualización
- Propiedades calculadas (total votos, porcentaje)

**PollVoto (Voto)**
- Relación con encuesta, opción y usuario
- Metadatos: justificación, IP, User-Agent
- Datos del votante: sede y carrera al momento del voto
- Timestamps para auditoría

**PollAnalytics (Estadísticas)**
- Distribución por sede y carrera
- Total de participantes únicos
- Actualización automática
- Cache de estadísticas

### Frontend (JavaScript Vanilla)

```
web/encuestas/
├── index.html        # Estructura HTML completa
├── encuestas.css     # Estilos responsive y temas
└── encuestas.js      # Aplicación SPA completa
```

#### Características del Frontend

**Clase EncuestasApp**
- Gestión de estado centralizada
- Autenticación automática
- API calls con manejo de errores
- Renderizado dinámico

**Componentes UI**
- Lista de encuestas con filtros
- Modal de creación con validaciones
- Modal de visualización/votación
- Dashboard con gráficos
- Sistema de notificaciones (toasts)

**Gráficos Interactivos**
- Chart.js para visualizaciones
- Gráficos de barras para rankings
- Gráficos de dona para resultados
- Colores personalizables por opción

## API Endpoints

### Encuestas CRUD
```
GET    /api/polls/                 # Listar con filtros
POST   /api/polls/                 # Crear nueva
GET    /api/polls/{id}/            # Detalle
PUT    /api/polls/{id}/            # Actualizar
DELETE /api/polls/{id}/            # Eliminar
```

### Acciones Específicas
```
POST   /api/polls/{id}/votar/      # Votar en encuesta
POST   /api/polls/{id}/cerrar/     # Cerrar manualmente
POST   /api/polls/{id}/export/     # Exportar resultados
GET    /api/polls/{id}/analytics/  # Analytics detallados
```

### Vistas Especiales
```
GET    /api/polls/mis-encuestas/   # Encuestas del usuario
GET    /api/polls/dashboard/       # Estadísticas generales
```

## Filtros y Búsqueda

### Parámetros de Filtrado
- `estado`: activa, cerrada, borrador, archivada
- `fecha_desde`: Filtro por fecha de inicio
- `fecha_hasta`: Filtro por fecha de inicio
- `creador`: ID del creador
- `search`: Búsqueda en título y descripción

### Filtros Automáticos
- **Por sede**: Solo encuestas de la sede del usuario
- **Por carrera**: Solo encuestas que incluyan su carrera
- **Por permisos**: Solo encuestas que el usuario puede ver

## Permisos y Roles

### Creación de Encuestas
- ✅ Moderador
- ✅ Director de Carrera  
- ✅ Administrador Global
- ❌ Estudiante

### Votación
- ✅ Todos los usuarios autenticados (según filtros de la encuesta)
- Validaciones: sede, carrera, estado de encuesta, voto previo

### Ver Resultados
- **Tiempo Real**: Todos los usuarios
- **Al Cierre**: Solo después de cerrar
- **Solo Moderador**: Solo creador y moderadores

### Gestión
- **Cerrar**: Creador o moderadores
- **Exportar**: Creador o moderadores
- **Analytics**: Creador o moderadores
- **Eliminar**: Solo administradores o creador

## Exportación de Datos

### Formato CSV
```csv
Opción,Votos,Porcentaje,Sede,Carrera,Fecha Voto,Justificación
Opción 1,1,,Sede Central,Informática,2024-01-15 14:30:00,Mi justificación
```

### Opciones de Exportación
- `formato`: csv, json
- `incluir_metadatos`: true/false
- `incluir_justificaciones`: true/false

## Instalación y Configuración

### 1. Aplicar Migraciones
```bash
python manage.py makemigrations polls
python manage.py migrate
```

### 2. Configurar Permisos
Los permisos se manejan automáticamente basados en el campo `role` del usuario.

### 3. Acceder a la Interfaz
- **URL**: `/encuestas/`
- **Requiere**: Usuario autenticado con correo @duocuc.cl
- **Compatible**: Navegadores modernos, PWA

### 4. Configuración de Admin
El sistema incluye configuración completa del Django Admin:
- Gestión de encuestas con inlines
- Filtros y búsquedas avanzadas
- Analytics visuales
- Acciones masivas

## Casos de Uso Típicos

### 1. Crear Encuesta de Satisfacción
```javascript
// Moderador crea encuesta para su carrera
{
  titulo: "Satisfacción con Laboratorios",
  carreras: ["Informática"],
  opciones: [
    {texto: "Muy satisfecho", color: "#28a745"},
    {texto: "Satisfecho", color: "#ffc107"},
    {texto: "Insatisfecho", color: "#dc3545"}
  ],
  mostrar_resultados: "al_cierre"
}
```

### 2. Encuesta de Prioridades Institucionales
```javascript
// Director crea encuesta multi-sede
{
  titulo: "Prioridades de Mejora 2024",
  multi: true,
  sedes_ids: [1, 2, 3], // Todas las sedes
  carreras: [], // Todas las carreras
  mostrar_resultados: "tiempo_real"
}
```

### 3. Consulta Rápida con Justificación
```javascript
{
  titulo: "Horario Preferido Biblioteca",
  requiere_justificacion: true,
  cierra_at: "2024-01-20T18:00:00Z"
}
```

## Monitoreo y Analytics

### Métricas Disponibles
- **Participación**: Total de votos únicos por encuesta
- **Distribución geográfica**: Votos por sede
- **Distribución académica**: Votos por carrera
- **Tendencias temporales**: Actividad por período
- **Top encuestas**: Ranking por participación

### Dashboard Ejecutivo
- Estadísticas generales del sistema
- Gráfico de encuestas más populares
- Actividad reciente (últimos 30 días)
- Métricas personales del usuario

## Consideraciones de Rendimiento

### Optimizaciones Implementadas
- **Consultas optimizadas**: Select related y prefetch
- **Índices de base de datos**: Campos frecuentemente filtrados
- **Cache de analytics**: Actualización cada 5 minutos
- **Paginación**: 20 elementos por página por defecto

### Escalabilidad
- **Arquitectura modular**: Fácil extensión
- **API REST**: Separación frontend/backend
- **Validaciones distribuidas**: Cliente y servidor
- **Carga asíncrona**: Datos bajo demanda

## Extensiones Futuras

### Funcionalidades Propuestas
- **Notificaciones push**: Recordatorios de encuestas
- **Plantillas de encuesta**: Reutilización de estructuras
- **Integración calendario**: Programación avanzada
- **Análisis ML**: Detección de patrones
- **API webhooks**: Integración con sistemas externos

### Mejoras Técnicas
- **Cache Redis**: Mejora de rendimiento
- **WebSockets**: Resultados en tiempo real
- **OCR**: Procesamiento de encuestas físicas
- **Exportación avanzada**: Excel, PDF con gráficos

## Soporte y Mantenimiento

### Logs y Debugging
- **Django logging**: Configurado para errores de API
- **Console logging**: Frontend para desarrollo
- **Auditoría completa**: Todos los votos registrados

### Backup y Recuperación
- **Modelos con timestamps**: Auditoría temporal
- **Soft deletes**: Recuperación de datos
- **Exportación completa**: Respaldo en CSV/JSON

---

## Contacto y Soporte

Para dudas técnicas o reportar problemas:
- **Documentación**: Ver este archivo
- **Tests**: Ejecutar `python manage.py test polls`
- **API Docs**: `/api/docs/` (Swagger)
- **Admin**: `/admin/` (Django Admin)

El sistema de encuestas DuocPoint está diseñado para ser robusto, escalable y fácil de usar, proporcionando todas las herramientas necesarias para la toma de decisiones basada en datos dentro de la comunidad académica.
