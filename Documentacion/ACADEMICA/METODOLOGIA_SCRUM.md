# Metodología Scrum - DuocPoint

## 1. Introducción a la Metodología

### ¿Qué es Scrum?

Scrum es un marco de trabajo ágil para el desarrollo de software que se basa en iteraciones cortas llamadas "sprints". Permite al equipo entregar valor de forma incremental y adaptarse rápidamente a los cambios en los requerimientos.

### ¿Por qué Scrum para DuocPoint?

- **Entrega incremental**: Permite mostrar progreso constante al profesor y stakeholders
- **Adaptabilidad**: Facilita ajustes basados en feedback recibido
- **Transparencia**: Proporciona visibilidad clara del progreso del proyecto
- **Colaboración**: Fomenta el trabajo en equipo y la comunicación constante
- **Calidad**: Incluye revisiones y retrospectivas para mejorar continuamente

## 2. Roles del Equipo

### Product Owner: Pablo Avendaño
**Responsabilidades:**
- Definir y priorizar el Product Backlog
- Aceptar o rechazar funcionalidades completadas
- Comunicar la visión del producto al equipo
- Tomar decisiones sobre requerimientos
- Representar a los usuarios finales

**En DuocPoint:**
- Define las funcionalidades de la plataforma
- Prioriza características según valor para la comunidad estudiantil
- Valida que las entregas cumplan con los objetivos académicos

### Scrum Master: Darosh Luco
**Responsabilidades:**
- Facilitar las ceremonias de Scrum
- Eliminar impedimentos del equipo
- Asegurar que el equipo siga los principios de Scrum
- Proteger al equipo de interrupciones externas
- Promover la mejora continua

**En DuocPoint:**
- Organiza reuniones diarias y ceremonias
- Identifica y resuelve bloqueos técnicos
- Mantiene el foco del equipo en los objetivos del sprint

### Development Team: Isaac Paz
**Responsabilidades:**
- Desarrollar las funcionalidades del producto
- Estimar el esfuerzo requerido para cada tarea
- Participar en la planificación de sprints
- Mantener la calidad del código
- Colaborar con otros miembros del equipo

**En DuocPoint:**
- Implementa las funcionalidades técnicas
- Realiza testing y corrección de bugs
- Mantiene la documentación técnica

## 3. Artefactos de Scrum

### Product Backlog
Lista priorizada de todas las funcionalidades, mejoras y correcciones que se desean implementar en DuocPoint.

**Ejemplos de User Stories:**
- Como estudiante, quiero poder crear posts en el foro para comunicarme con mis compañeros
- Como moderador, quiero poder aprobar o rechazar posts para mantener la calidad del contenido
- Como estudiante, quiero poder publicar productos en el mercado para vender mis artículos
- Como usuario, quiero poder generar un PDF de mi portafolio para postular a trabajos

### Sprint Backlog
Lista de tareas específicas que el equipo se compromete a completar durante un sprint.

**Ejemplo Sprint 1:**
- Configurar entorno de desarrollo Django
- Implementar modelo de Usuario
- Crear sistema de autenticación JWT
- Configurar base de datos PostgreSQL
- Crear documentación técnica básica

### Incremento
Versión funcional del producto al final de cada sprint que cumple con la definición de "Terminado".

**Definición de "Terminado" para DuocPoint:**
- Código implementado y probado
- Tests unitarios escritos y pasando
- Documentación actualizada
- Revisión de código completada
- Funcionalidad demostrable

## 4. Ceremonias de Scrum

### Sprint Planning (2 horas)
**Frecuencia**: Al inicio de cada sprint (cada 2 semanas)
**Participantes**: Todo el equipo Scrum
**Objetivo**: Planificar el trabajo del sprint

**Agenda:**
1. Revisión del Product Backlog
2. Selección de User Stories para el sprint
3. Descomposición en tareas técnicas
4. Estimación de esfuerzo
5. Compromiso del equipo

**Ejemplo Sprint Planning DuocPoint:**
- **Sprint Goal**: Implementar sistema de foros básico
- **User Stories seleccionadas**: 3
- **Tareas técnicas**: 8
- **Estimación total**: 20 story points

### Daily Standup (15 minutos)
**Frecuencia**: Diariamente
**Participantes**: Todo el equipo Scrum
**Objetivo**: Sincronizar el trabajo del equipo

**Preguntas clave:**
1. ¿Qué hice ayer?
2. ¿Qué haré hoy?
3. ¿Tengo algún impedimento?

**Ejemplo Daily Standup:**
- **Pablo**: Ayer completé el diseño de la base de datos. Hoy trabajaré en la API de foros. No tengo impedimentos.
- **Darosh**: Ayer revisé el código de autenticación. Hoy organizaré la reunión de sprint review. Necesito acceso al servidor de testing.
- **Isaac**: Ayer implementé los tests unitarios. Hoy trabajaré en la interfaz de usuario. No tengo impedimentos.

### Sprint Review (1 hora)
**Frecuencia**: Al final de cada sprint
**Participantes**: Todo el equipo Scrum + stakeholders
**Objetivo**: Demostrar el trabajo completado

**Agenda:**
1. Demostración de funcionalidades
2. Revisión del Sprint Goal
3. Feedback de stakeholders
4. Actualización del Product Backlog

**Ejemplo Sprint Review DuocPoint:**
- **Funcionalidades demostradas**: Sistema de foros, moderación básica
- **Feedback recibido**: Mejorar interfaz de usuario, agregar filtros
- **Próximas prioridades**: Sistema de compra/venta

### Sprint Retrospective (1 hora)
**Frecuencia**: Al final de cada sprint
**Participantes**: Solo el equipo Scrum
**Objetivo**: Mejorar el proceso de trabajo

**Preguntas clave:**
1. ¿Qué salió bien?
2. ¿Qué se puede mejorar?
3. ¿Qué acciones tomaremos?

**Ejemplo Retrospectiva:**
- **Qué salió bien**: Comunicación del equipo, calidad del código
- **Qué mejorar**: Estimaciones de tiempo, testing
- **Acciones**: Implementar pair programming, aumentar tiempo de testing

## 5. Planificación de Sprints

### Sprint 1: Configuración Inicial (Semanas 1-2)
**Sprint Goal**: Establecer la base técnica del proyecto

**User Stories:**
- Como desarrollador, quiero tener un entorno de desarrollo configurado
- Como usuario, quiero poder registrarme en la plataforma
- Como usuario, quiero poder iniciar sesión de forma segura

**Tareas técnicas:**
- Configurar Django + DRF
- Configurar PostgreSQL
- Implementar modelo de Usuario
- Crear sistema de autenticación JWT
- Configurar Docker para desarrollo
- Crear documentación técnica básica

**Criterios de aceptación:**
- Usuario puede registrarse con email @duocuc.cl o @gmail.com
- Usuario puede iniciar sesión y recibir token JWT
- Sistema valida dominios de email correctamente

### Sprint 2: Sistema de Foros (Semanas 3-4)
**Sprint Goal**: Implementar comunicación básica entre estudiantes

**User Stories:**
- Como estudiante, quiero crear posts en foros por carrera
- Como estudiante, quiero comentar en posts de otros
- Como moderador, quiero aprobar o rechazar posts

**Tareas técnicas:**
- Crear modelos de Foro, Post, Comentario
- Implementar API REST para foros
- Crear interfaz de usuario para foros
- Implementar sistema de moderación básico
- Agregar filtros de palabras prohibidas
- Crear tests unitarios

**Criterios de aceptación:**
- Usuario puede crear posts en foros específicos
- Usuario puede comentar en posts existentes
- Moderador puede aprobar/rechazar posts
- Sistema filtra contenido inapropiado automáticamente

### Sprint 3: Sistema de Compra/Venta (Semanas 5-6)
**Sprint Goal**: Facilitar comercio seguro entre estudiantes

**User Stories:**
- Como estudiante, quiero publicar productos para vender
- Como estudiante, quiero buscar productos por categoría
- Como estudiante, quiero marcar productos como favoritos

**Tareas técnicas:**
- Crear modelos de Producto, Categoría, Favorito
- Implementar API REST para mercado
- Crear interfaz de usuario para mercado
- Implementar sistema de búsqueda y filtros
- Agregar funcionalidad de favoritos
- Implementar subida de imágenes

**Criterios de aceptación:**
- Usuario puede publicar productos con imágenes
- Usuario puede buscar y filtrar productos
- Usuario puede marcar productos como favoritos
- Sistema muestra productos por categoría

### Sprint 4: Portafolio y Street View (Semanas 7-8)
**Sprint Goal**: Implementar herramientas de desarrollo profesional y orientación

**User Stories:**
- Como estudiante, quiero crear mi portafolio profesional
- Como estudiante, quiero generar PDF de mi portafolio
- Como estudiante, quiero explorar la sede virtualmente

**Tareas técnicas:**
- Crear modelos de Portafolio, Logro, Proyecto
- Implementar generación de PDF
- Crear interfaz de usuario para portafolio
- Implementar Street View personalizado
- Agregar mapa interactivo de la sede
- Crear sistema de sugerencias

**Criterios de aceptación:**
- Usuario puede completar su portafolio
- Usuario puede generar PDF profesional
- Usuario puede navegar por la sede virtualmente
- Sistema calcula porcentaje de completitud

### Sprint 5: Funcionalidades Avanzadas (Semanas 9-10)
**Sprint Goal**: Completar funcionalidades restantes

**User Stories:**
- Como estudiante, quiero participar en encuestas
- Como estudiante, quiero recibir notificaciones push
- Como administrador, quiero ver reportes de infraestructura

**Tareas técnicas:**
- Implementar sistema de encuestas
- Configurar notificaciones Web Push
- Crear sistema de reportes
- Implementar bienestar estudiantil
- Agregar analytics y métricas
- Optimizar performance

**Criterios de aceptación:**
- Usuario puede participar en encuestas
- Usuario recibe notificaciones push
- Administrador puede ver reportes
- Sistema muestra métricas de uso

### Sprint 6: Testing y Deployment (Semanas 11-12)
**Sprint Goal**: Asegurar calidad y preparar para producción

**User Stories:**
- Como desarrollador, quiero que el sistema tenga tests completos
- Como usuario, quiero que la plataforma esté disponible en producción
- Como administrador, quiero poder monitorear el sistema

**Tareas técnicas:**
- Escribir tests de integración
- Implementar tests de aceptación
- Configurar CI/CD
- Preparar deployment en producción
- Configurar monitoreo y logs
- Crear documentación de usuario

**Criterios de aceptación:**
- Cobertura de tests > 80%
- Sistema desplegado en producción
- Monitoreo configurado
- Documentación completa

## 6. Herramientas de Gestión

### GitHub
**Uso**: Control de versiones y colaboración
**Configuración**:
- Repositorio principal: `duoc-point`
- Ramas por feature: `feature/nombre-funcionalidad`
- Pull requests para revisión de código
- Issues para tracking de bugs y mejoras

**Flujo de trabajo**:
1. Crear rama desde `main`
2. Desarrollar funcionalidad
3. Crear pull request
4. Revisión de código
5. Merge a `main`

### Trello
**Uso**: Gestión de tareas y seguimiento de progreso
**Configuración**:
- Board: "DuocPoint - Proyecto APT"
- Listas: Backlog, En Progreso, En Revisión, Terminado
- Tarjetas por User Story
- Etiquetas por prioridad y tipo

**Ejemplo de tarjeta**:
- **Título**: Como estudiante, quiero crear posts en el foro
- **Descripción**: Implementar funcionalidad de creación de posts
- **Criterios de aceptación**: Lista de criterios
- **Estimación**: 5 story points
- **Asignado**: Isaac Paz

### Discord
**Uso**: Comunicación diaria del equipo
**Configuración**:
- Servidor: "DuocPoint Team"
- Canales: general, desarrollo, testing, documentación
- Reuniones diarias por voz
- Compartir pantalla para demos

## 7. Métricas y Seguimiento

### Métricas de Sprint
- **Velocity**: Story points completados por sprint
- **Burndown**: Progreso diario hacia el objetivo del sprint
- **Lead Time**: Tiempo desde creación hasta completado
- **Cycle Time**: Tiempo en desarrollo activo

### Métricas de Calidad
- **Cobertura de tests**: Porcentaje de código cubierto
- **Bugs encontrados**: Número de defectos por sprint
- **Tiempo de resolución**: Tiempo promedio para corregir bugs
- **Satisfacción del equipo**: Encuesta de retrospectiva

### Métricas de Producto
- **Funcionalidades completadas**: Número de User Stories terminadas
- **Performance**: Tiempo de respuesta de la aplicación
- **Usabilidad**: Feedback de usuarios beta
- **Adopción**: Número de usuarios activos

## 8. Retrospectivas y Mejoras

### Sprint 1 Retrospectiva
**Qué salió bien:**
- Configuración rápida del entorno
- Buena comunicación del equipo
- Documentación técnica clara

**Qué se puede mejorar:**
- Estimaciones de tiempo más precisas
- Testing más temprano en el proceso
- Mejor organización de tareas

**Acciones tomadas:**
- Implementar pair programming para tareas complejas
- Agregar tiempo de testing en cada tarea
- Usar estimaciones de story points más detalladas

### Sprint 2 Retrospectiva
**Qué salió bien:**
- Implementación exitosa de foros
- Sistema de moderación funcionando
- Feedback positivo de usuarios beta

**Qué se puede mejorar:**
- Interfaz de usuario más intuitiva
- Performance de búsqueda
- Documentación de usuario

**Acciones tomadas:**
- Rediseñar interfaz de usuario
- Optimizar consultas de base de datos
- Crear tutorial de usuario

### Mejoras Continuas
- **Proceso**: Ajustar duración de sprints si es necesario
- **Herramientas**: Evaluar nuevas herramientas de gestión
- **Comunicación**: Mejorar canales de comunicación
- **Calidad**: Implementar más prácticas de calidad
- **Documentación**: Mantener documentación actualizada

## 9. Beneficios de Scrum para DuocPoint

### Para el Equipo
- **Visibilidad clara** del progreso del proyecto
- **Comunicación constante** entre miembros
- **Adaptabilidad** a cambios en requerimientos
- **Mejora continua** del proceso de trabajo
- **Satisfacción** por entregas incrementales

### Para el Proyecto
- **Calidad** asegurada por revisiones constantes
- **Riesgo reducido** por entregas incrementales
- **Flexibilidad** para ajustar prioridades
- **Transparencia** en el progreso
- **Valor entregado** de forma continua

### Para los Stakeholders
- **Visibilidad** del progreso del proyecto
- **Oportunidad de feedback** en cada sprint
- **Confianza** en la entrega del producto
- **Participación** en la definición del producto
- **Satisfacción** con el resultado final

## 10. Conclusiones

La metodología Scrum ha sido fundamental para el éxito del proyecto DuocPoint, permitiendo:

1. **Entrega incremental** de valor al profesor y stakeholders
2. **Adaptabilidad** a cambios en requerimientos académicos
3. **Transparencia** en el progreso del proyecto
4. **Colaboración efectiva** entre miembros del equipo
5. **Calidad asegurada** por revisiones constantes

El uso de Scrum no solo ha mejorado la gestión del proyecto, sino que también ha demostrado competencias profesionales en metodologías ágiles, esenciales para el campo laboral de la Ingeniería en Informática.

---

**Documento preparado por**:  
Darosh Luco (Scrum Master)  
**Fecha**: Enero 2024  
**Proyecto**: DuocPoint  
**Metodología**: Scrum
