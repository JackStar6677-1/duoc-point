# Plan de Trabajo - DuocPoint

## 1. Resumen Ejecutivo

### Información del Proyecto
- **Nombre**: DuocPoint - Plataforma Integral para la Comunidad Duoc UC
- **Duración**: 18 semanas (1 semestre académico)
- **Metodología**: Scrum con sprints de 2 semanas
- **Equipo**: 3 desarrolladores (Pablo Avendaño, Darosh Luco, Isaac Paz)
- **Institución**: Duoc UC - Sede Maipú

### Objetivo General
Desarrollar una plataforma digital integral que mejore la experiencia universitaria de la comunidad Duoc UC, facilitando la comunicación, el aprendizaje y el desarrollo profesional de los estudiantes.

## 2. Cronograma General

### Fase 1: Inicialización (Semanas 1-2)
**Objetivo**: Establecer la base técnica del proyecto

#### Semana 1: Configuración del Entorno
- **Lunes**: Configuración del entorno de desarrollo Django
- **Martes**: Configuración de base de datos PostgreSQL
- **Miércoles**: Configuración de Docker para desarrollo
- **Jueves**: Configuración de herramientas de gestión (GitHub, Trello)
- **Viernes**: Creación de documentación técnica básica

#### Semana 2: Autenticación y Usuarios
- **Lunes**: Implementación del modelo de Usuario
- **Martes**: Sistema de autenticación JWT
- **Miércoles**: Validación de dominios de email
- **Jueves**: Interfaz de usuario para login/registro
- **Viernes**: Testing y documentación

### Fase 2: Funcionalidades Core (Semanas 3-8)
**Objetivo**: Implementar las funcionalidades principales de la plataforma

#### Semana 3: Sistema de Foros (Parte 1)
- **Lunes**: Modelos de Foro, Post, Comentario
- **Martes**: API REST para foros
- **Miércoles**: Interfaz de usuario básica
- **Jueves**: Sistema de votos
- **Viernes**: Testing unitario

#### Semana 4: Sistema de Foros (Parte 2)
- **Lunes**: Sistema de moderación automática
- **Martes**: Panel de moderación para administradores
- **Miércoles**: Sistema de reportes
- **Jueves**: Filtros y búsqueda
- **Viernes**: Testing de integración

#### Semana 5: Sistema de Compra/Venta (Parte 1)
- **Lunes**: Modelos de Producto, Categoría
- **Martes**: API REST para mercado
- **Miércoles**: Interfaz de usuario para publicar
- **Jueves**: Sistema de subida de imágenes
- **Viernes**: Testing unitario

#### Semana 6: Sistema de Compra/Venta (Parte 2)
- **Lunes**: Sistema de búsqueda y filtros
- **Martes**: Funcionalidad de favoritos
- **Miércoles**: Sistema de reportes de productos
- **Jueves**: Integración OpenGraph
- **Viernes**: Testing de integración

#### Semana 7: Portafolio (Parte 1)
- **Lunes**: Modelos de Portafolio, Logro, Proyecto
- **Martes**: API REST para portafolio
- **Miércoles**: Interfaz de usuario para completar perfil
- **Jueves**: Sistema de sugerencias
- **Viernes**: Testing unitario

#### Semana 8: Portafolio (Parte 2)
- **Lunes**: Generación de PDF
- **Martes**: Analytics de completitud
- **Miércoles**: Integración con LinkedIn/GitHub
- **Jueves**: Optimización de performance
- **Viernes**: Testing de integración

### Fase 3: Funcionalidades Avanzadas (Semanas 9-14)
**Objetivo**: Completar funcionalidades restantes y optimizar

#### Semana 9: Street View y Mapas
- **Lunes**: Implementación de Street View personalizado
- **Martes**: Mapa interactivo con Leaflet
- **Miércoles**: Puntos de interés de la sede
- **Jueves**: Navegación 360°
- **Viernes**: Testing y optimización

#### Semana 10: Sistema de Encuestas
- **Lunes**: Modelos de Poll, PollOpcion, PollVoto
- **Martes**: API REST para encuestas
- **Miércoles**: Interfaz de usuario para crear encuestas
- **Jueves**: Sistema de votación
- **Viernes**: Analytics de resultados

#### Semana 11: Notificaciones Push
- **Lunes**: Configuración de Web Push
- **Martes**: Sistema de notificaciones
- **Miércoles**: Configuración de preferencias
- **Jueves**: Integración con eventos
- **Viernes**: Testing de notificaciones

#### Semana 12: Bienestar Estudiantil
- **Lunes**: Modelos de recursos de bienestar
- **Martes**: API REST para bienestar
- **Miércoles**: Interfaz de usuario
- **Jueves**: Personalización por carrera
- **Viernes**: Testing y documentación

#### Semana 13: Reportes de Infraestructura
- **Lunes**: Modelos de reportes
- **Martes**: API REST para reportes
- **Miércoles**: Interfaz de usuario
- **Jueves**: Sistema de seguimiento
- **Viernes**: Testing y documentación

#### Semana 14: Optimización y Performance
- **Lunes**: Optimización de consultas de base de datos
- **Martes**: Implementación de cache
- **Miércoles**: Optimización de frontend
- **Jueves**: Compresión de imágenes
- **Viernes**: Testing de performance

### Fase 4: Finalización (Semanas 15-18)
**Objetivo**: Testing integral, documentación y deployment

#### Semana 15: Testing Integral
- **Lunes**: Tests de integración completos
- **Martes**: Tests de aceptación
- **Miércoles**: Tests de performance
- **Jueves**: Tests de seguridad
- **Viernes**: Corrección de bugs encontrados

#### Semana 16: Documentación Final
- **Lunes**: Manual de usuario completo
- **Martes**: Documentación técnica
- **Miércoles**: Documentación de deployment
- **Jueves**: Documentación de API
- **Viernes**: Revisión y corrección

#### Semana 17: Deployment y Configuración
- **Lunes**: Configuración de servidor de producción
- **Martes**: Deployment de la aplicación
- **Miércoles**: Configuración de monitoreo
- **Jueves**: Configuración de backup
- **Viernes**: Testing en producción

#### Semana 18: Presentación Final
- **Lunes**: Preparación de presentación
- **Martes**: Demostración final
- **Miércoles**: Entrega de documentación
- **Jueves**: Retrospectiva final
- **Viernes**: Cierre del proyecto

## 3. Recursos Necesarios

### Recursos Humanos
- **3 Desarrolladores** (tiempo completo)
- **1 Product Owner** (Pablo Avendaño)
- **1 Scrum Master** (Darosh Luco)
- **1 Tester** (Isaac Paz)

### Recursos Técnicos
- **Servidor de desarrollo**: Computadoras personales del equipo
- **Base de datos**: PostgreSQL (gratuita)
- **Herramientas de desarrollo**: VS Code, Git (gratuitas)
- **Servicios en la nube**: Opcional para deployment

### Recursos Materiales
- **Documentación técnica**: Django, DRF, PWA
- **Recursos de diseño**: Bootstrap, iconos, imágenes
- **Imágenes para Street View**: Fotografías de la sede Maipú

## 4. Facilitadores del Proyecto

### Conocimiento Técnico
- **Experiencia previa** con Django y Python
- **Conocimiento de** tecnologías web modernas
- **Familiaridad con** metodologías ágiles
- **Acceso a** documentación y recursos de aprendizaje

### Herramientas Disponibles
- **GitHub** para control de versiones
- **Trello** para gestión de tareas
- **Discord** para comunicación
- **Google Drive** para documentación compartida

### Apoyo Institucional
- **Acceso a** laboratorios de computación
- **Apoyo de** profesores y personal técnico
- **Comunidad estudiantil** para testing
- **Recursos de** la biblioteca y centro de documentación

### Factores Externos Positivos
- **Tecnologías gratuitas** y de código abierto
- **Comunidad activa** de desarrolladores
- **Documentación abundante** disponible online
- **Herramientas colaborativas** gratuitas

## 5. Obstaculizadores del Proyecto

### Desafíos Técnicos
- **Complejidad** de algunas funcionalidades
- **Integración** entre diferentes módulos
- **Performance** con gran cantidad de usuarios
- **Seguridad** y protección de datos

### Limitaciones de Tiempo
- **18 semanas** para desarrollo completo
- **Horas limitadas** por asignatura
- **Múltiples asignaturas** simultáneas
- **Compromisos** personales del equipo

### Recursos Limitados
- **Presupuesto** limitado para servicios externos
- **Acceso limitado** a servidores de producción
- **Tiempo limitado** para testing exhaustivo
- **Recursos limitados** para diseño gráfico

### Factores Externos
- **Dependencias** de servicios externos
- **Cambios** en requerimientos académicos
- **Problemas** de conectividad o hardware
- **Coordinación** entre miembros del equipo

## 6. Estrategias de Mitigación

### Para Desafíos Técnicos
- **Planificación detallada** con buffers de tiempo
- **Prototipado temprano** de funcionalidades complejas
- **Consultas** con profesores y expertos
- **Documentación** de decisiones técnicas

### Para Limitaciones de Tiempo
- **Priorización** de funcionalidades críticas
- **Desarrollo incremental** con entregas parciales
- **Eliminación** de funcionalidades no esenciales
- **Optimización** del tiempo de trabajo

### Para Recursos Limitados
- **Uso de tecnologías gratuitas** cuando sea posible
- **Optimización** de recursos disponibles
- **Colaboración** con otros equipos
- **Búsqueda** de alternativas de bajo costo

### Para Factores Externos
- **Planificación de contingencia** para problemas
- **Comunicación constante** con stakeholders
- **Flexibilidad** en la implementación
- **Documentación** de cambios y decisiones

## 7. Hitos del Proyecto

### Hito 1: Base Técnica (Semana 2)
**Criterios de éxito:**
- Entorno de desarrollo configurado
- Sistema de autenticación funcionando
- Base de datos configurada
- Documentación técnica básica

**Entregables:**
- Código fuente en GitHub
- Documentación de instalación
- Demo de autenticación
- Tests unitarios básicos

### Hito 2: Funcionalidades Core (Semana 8)
**Criterios de éxito:**
- Sistema de foros completo
- Sistema de compra/venta funcional
- Portafolio con generación de PDF
- Testing de integración pasando

**Entregables:**
- Demo de funcionalidades principales
- Documentación de usuario
- Tests de integración
- Feedback de usuarios beta

### Hito 3: Funcionalidades Avanzadas (Semana 14)
**Criterios de éxito:**
- Street View personalizado funcionando
- Sistema de encuestas completo
- Notificaciones push implementadas
- Performance optimizada

**Entregables:**
- Demo de funcionalidades avanzadas
- Documentación técnica completa
- Tests de performance
- Métricas de calidad

### Hito 4: Producto Final (Semana 18)
**Criterios de éxito:**
- Todas las funcionalidades implementadas
- Testing integral completado
- Documentación final entregada
- Sistema desplegado en producción

**Entregables:**
- Producto final funcional
- Documentación completa
- Presentación final
- Retrospectiva del proyecto

## 8. Métricas de Seguimiento

### Métricas de Progreso
- **Funcionalidades completadas**: Número de User Stories terminadas
- **Código implementado**: Líneas de código por módulo
- **Tests escritos**: Número de tests unitarios e integración
- **Documentación**: Páginas de documentación creadas

### Métricas de Calidad
- **Cobertura de tests**: Porcentaje de código cubierto
- **Bugs encontrados**: Número de defectos por sprint
- **Performance**: Tiempo de respuesta de la aplicación
- **Usabilidad**: Feedback de usuarios beta

### Métricas de Equipo
- **Velocity**: Story points completados por sprint
- **Satisfacción**: Encuesta de retrospectiva
- **Comunicación**: Frecuencia de reuniones
- **Colaboración**: Número de pull requests

## 9. Plan de Contingencia

### Escenario 1: Retraso en Desarrollo
**Causa**: Complejidad técnica mayor a la esperada
**Acción**: Priorizar funcionalidades críticas, eliminar funcionalidades opcionales
**Tiempo de recuperación**: 1-2 semanas

### Escenario 2: Problemas de Integración
**Causa**: Dificultades en la integración entre módulos
**Acción**: Dedicar sprint completo a integración, consultar con expertos
**Tiempo de recuperación**: 2-3 semanas

### Escenario 3: Problemas de Performance
**Causa**: Sistema lento con datos reales
**Acción**: Optimizar consultas, implementar cache, reducir funcionalidades
**Tiempo de recuperación**: 1-2 semanas

### Escenario 4: Problemas de Equipo
**Causa**: Falta de disponibilidad de miembros del equipo
**Acción**: Redistribuir tareas, buscar apoyo externo
**Tiempo de recuperación**: 1 semana

## 10. Conclusiones

El plan de trabajo para DuocPoint está diseñado para maximizar las posibilidades de éxito del proyecto dentro de las limitaciones de tiempo y recursos disponibles. La metodología Scrum permite adaptabilidad y entrega incremental de valor, mientras que la planificación detallada asegura que se cumplan los objetivos académicos.

### Factores Críticos de Éxito
1. **Comunicación constante** del equipo
2. **Priorización** de funcionalidades críticas
3. **Testing temprano** y continuo
4. **Documentación** actualizada
5. **Flexibilidad** para adaptarse a cambios

### Riesgos Principales
1. **Complejidad técnica** mayor a la esperada
2. **Limitaciones de tiempo** para testing
3. **Problemas de integración** entre módulos
4. **Recursos limitados** para deployment

### Estrategias de Mitigación
1. **Planificación detallada** con buffers
2. **Desarrollo incremental** con entregas parciales
3. **Testing continuo** durante el desarrollo
4. **Comunicación constante** con stakeholders

El plan de trabajo está diseñado para ser realista y alcanzable, considerando las competencias del equipo, los recursos disponibles y los objetivos académicos del proyecto.

---

**Documento preparado por**:  
Pablo Avendaño, Darosh Luco, Isaac Paz  
**Fecha**: Enero 2024  
**Proyecto**: DuocPoint  
**Asignatura**: APT122 - Proyecto de Título
