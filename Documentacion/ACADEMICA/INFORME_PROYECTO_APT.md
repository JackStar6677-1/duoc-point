# Informe de Presentación del Proyecto APT - DuocPoint

## 1. Descripción Breve del Proyecto APT

**Nombre del Proyecto**: DuocPoint  
**Versión**: 1.0.0  
**Fecha**: Enero 2024  
**Equipo**: Pablo Avendaño, Darosh Luco, Isaac Paz  
**Institución**: Duoc UC - Sede Maipú  

### Descripción del Proyecto

DuocPoint es una plataforma digital integral destinada a mejorar la experiencia universitaria de la comunidad de Duoc UC, incluyendo a estudiantes, docentes y personal administrativo. La plataforma proporciona herramientas de comunicación, acceso a recursos académicos, apoyo al bienestar estudiantil y fomenta la interacción entre carreras.

### Características Principales

- **Mapa interactivo de sedes** con recorridos virtuales 360°
- **Foros por carreras** con sistema de moderación automática
- **Notificaciones push** para recordatorios de clases y eventos
- **Sistema de compra/venta segura** entre estudiantes
- **Portafolio automático** con generación de PDF profesional
- **Sistema de reportes de infraestructura** para mantenimiento
- **Bienestar estudiantil personalizado** por carrera
- **Sistema de encuestas** para participación estudiantil

### Justificación de Relevancia

DuocPoint aborda problemas reales identificados en la comunidad estudiantil de Duoc UC:

1. **Comunicación deficiente** entre estudiantes, docentes y personal administrativo
2. **Acceso limitado** a recursos académicos y bienestar estudiantil
3. **Dificultad para interactuar** entre sedes y con otras carreras
4. **Falta de herramientas** para el desarrollo profesional estudiantil
5. **Necesidad de orientación** dentro del campus

La plataforma tiene un **impacto directo en el campo laboral** de la carrera de Ingeniería en Informática, ya que:

- Demuestra competencias en **desarrollo de software** moderno
- Aplica **metodologías ágiles** de gestión de proyectos
- Implementa **mejores prácticas** de seguridad y calidad
- Utiliza **tecnologías emergentes** como PWA y Web Push
- Resuelve **problemas reales** de la comunidad educativa

## 2. Relación con las Competencias del Perfil de Egreso

DuocPoint se vincula directamente con las competencias del perfil de egreso de la carrera de Ingeniería en Informática:

### Desarrollo de Software
- **Implementación**: Creación de una plataforma robusta utilizando Django 5.0 + DRF para backend y PWA para frontend
- **Tecnologías**: HTML5, CSS3, JavaScript ES6+, Bootstrap 5, Leaflet.js
- **Arquitectura**: Patrón MVC con API RESTful y separación clara de responsabilidades
- **Escalabilidad**: Diseño modular que permite crecimiento horizontal

### Gestión de Proyectos Informáticos
- **Metodología**: Implementación de Scrum con sprints de 2 semanas
- **Herramientas**: GitHub para control de versiones, Trello para gestión de tareas
- **Planificación**: Entregas iterativas con retroalimentación continua
- **Control**: Seguimiento de hitos y métricas de progreso

### Modelado de Datos
- **Diseño**: Estructuras de base de datos relacionales optimizadas
- **Tecnologías**: PostgreSQL para producción, SQLite para desarrollo
- **Normalización**: Diseño normalizado con índices apropiados
- **Escalabilidad**: Arquitectura preparada para crecimiento de datos

### Ciberseguridad
- **Autenticación**: JWT con validación de dominios de email
- **Autorización**: Roles granulares (estudiante, moderador, director, admin)
- **Validación**: Sanitización de inputs y protección contra ataques comunes
- **Moderación**: Sistema automático y manual de contenido inapropiado

### Calidad de Software (QA)
- **Testing**: Suite de pruebas unitarias, de integración y de aceptación
- **Cobertura**: Objetivo de cobertura > 80%
- **Performance**: Optimización para < 2 segundos de respuesta
- **Monitoreo**: Logs y métricas de rendimiento

## 3. Relación con los Intereses Profesionales

### Intereses del Equipo

**Pablo Avendaño**: Especialización en desarrollo de aplicaciones web y móviles, con interés en tecnologías emergentes y experiencia de usuario.

**Darosh Luco**: Enfoque en gestión de proyectos ágiles y desarrollo de soluciones escalables para empresas.

**Isaac Paz**: Interés en ciberseguridad y desarrollo de sistemas robustos con énfasis en calidad de software.

### Conexión con el Proyecto

1. **Desarrollo Web y Móvil**: DuocPoint utiliza tecnologías modernas como PWA, permitiendo experiencia nativa en dispositivos móviles sin necesidad de aplicaciones adicionales.

2. **Gestión de Proyectos Ágiles**: La implementación de Scrum permite aplicar metodologías ágiles en un proyecto real, con sprints, retrospectivas y entregas continuas.

3. **Ciberseguridad**: El sistema implementa múltiples capas de seguridad, desde autenticación JWT hasta moderación de contenido, preparando al equipo para desafíos de seguridad en el campo laboral.

4. **Calidad de Software**: El proyecto incluye testing sistemático, documentación técnica y mejores prácticas de desarrollo, esenciales para el éxito profesional.

5. **Innovación Tecnológica**: La implementación de Street View personalizado y moderación inteligente demuestra capacidad de innovación y resolución de problemas complejos.

## 4. Factibilidad del Proyecto APT

### Duración del Semestre
- **Período**: 18 semanas de desarrollo
- **Metodología**: Sprints de 2 semanas (9 sprints total)
- **Entregas**: Funcionalidades incrementales cada sprint
- **Factibilidad**: ✅ **ALTA** - Tiempo suficiente para desarrollo completo

### Horas Asignadas a la Asignatura
- **Horas semanales**: 4 horas presenciales + 8 horas de trabajo autónomo
- **Total semestral**: 216 horas por estudiante
- **Trabajo en equipo**: 648 horas totales del equipo
- **Factibilidad**: ✅ **ALTA** - Horas suficientes para desarrollo y testing

### Materiales Requeridos
- **Tecnologías**: Django, PostgreSQL, Redis, Docker (gratuitas)
- **Herramientas**: GitHub, Trello, VS Code (gratuitas)
- **Infraestructura**: Servidor de desarrollo local
- **Factibilidad**: ✅ **ALTA** - Tecnologías accesibles y conocidas

### Factores Externos que Facilitan el Desarrollo
1. **Conocimiento previo** de las tecnologías utilizadas
2. **Herramientas colaborativas** (GitHub, Trello) disponibles
3. **Acceso a documentación** y recursos de aprendizaje
4. **Apoyo de la institución** para el desarrollo del proyecto
5. **Comunidad estudiantil** como usuarios potenciales para testing

### Factores Externos que Dificultan el Desarrollo
1. **Integración backend-frontend** puede presentar desafíos técnicos
2. **Testing con usuarios reales** requiere coordinación con la comunidad
3. **Deployment en producción** puede requerir recursos adicionales
4. **Mantenimiento continuo** después del semestre

### Estrategias de Mitigación
- **Planificación detallada** con tiempo suficiente para integración
- **Testing temprano** con usuarios beta de la comunidad
- **Documentación completa** para facilitar mantenimiento
- **Arquitectura modular** para facilitar actualizaciones

## 5. Objetivos del Proyecto

### Objetivo General
Desarrollar una plataforma digital integral que mejore la experiencia universitaria de la comunidad Duoc UC, facilitando la comunicación, el aprendizaje y el desarrollo profesional de los estudiantes.

### Objetivos Específicos

1. **Comunicación Efectiva**
   - Implementar sistema de foros por carrera con moderación automática
   - Facilitar interacción entre estudiantes, docentes y personal administrativo
   - Reducir barreras de comunicación entre sedes

2. **Orientación y Navegación**
   - Desarrollar mapa interactivo de la sede con recorridos virtuales
   - Proporcionar información detallada de puntos de interés
   - Facilitar orientación de nuevos estudiantes

3. **Desarrollo Profesional**
   - Crear sistema de portafolio automático con generación de PDF
   - Implementar seguimiento de logros y competencias
   - Facilitar transición al mundo laboral

4. **Bienestar Estudiantil**
   - Desarrollar recursos personalizados por carrera
   - Implementar sistema de reportes de infraestructura
   - Facilitar acceso a servicios de bienestar

5. **Comercio Seguro**
   - Crear mercado de compra/venta entre estudiantes
   - Implementar sistema de reportes y moderación
   - Facilitar transacciones seguras

6. **Participación Estudiantil**
   - Desarrollar sistema de encuestas y votaciones
   - Implementar notificaciones push para eventos
   - Facilitar participación en actividades institucionales

## 6. Metodología de Trabajo

### Metodología Ágil - Scrum

#### Roles del Equipo
- **Product Owner**: Pablo Avendaño (definición de requerimientos y prioridades)
- **Scrum Master**: Darosh Luco (facilitación del proceso y eliminación de impedimentos)
- **Desarrolladores**: Isaac Paz (implementación técnica y testing)

#### Sprints de 2 Semanas
- **Sprint 1-2**: Configuración inicial y autenticación
- **Sprint 3-4**: Sistema de foros y moderación
- **Sprint 5-6**: Sistema de compra/venta
- **Sprint 7-8**: Portafolio y Street View
- **Sprint 9**: Testing, documentación y deployment

#### Ceremonias Scrum
- **Daily Standups**: Reuniones diarias de 15 minutos
- **Sprint Planning**: Planificación de 2 horas al inicio de cada sprint
- **Sprint Review**: Demostración de funcionalidades al final de cada sprint
- **Retrospectiva**: Análisis de mejoras al final de cada sprint

#### Herramientas de Gestión
- **GitHub**: Control de versiones y colaboración
- **Trello**: Gestión de tareas y seguimiento de progreso
- **Discord**: Comunicación diaria del equipo
- **Google Drive**: Documentación compartida

### Iteración Continua
- **Desarrollo incremental** con entregas funcionales cada sprint
- **Retroalimentación constante** de usuarios y stakeholders
- **Adaptación continua** basada en feedback recibido
- **Mejora continua** de procesos y funcionalidades

## 7. Plan de Trabajo

### Cronograma General (18 semanas)

#### Fase 1: Inicialización (Semanas 1-2)
- **Semana 1**: Configuración del entorno de desarrollo
- **Semana 2**: Implementación de autenticación y gestión de usuarios

#### Fase 2: Funcionalidades Core (Semanas 3-8)
- **Semanas 3-4**: Sistema de foros con moderación
- **Semanas 5-6**: Sistema de compra/venta
- **Semanas 7-8**: Portafolio y Street View

#### Fase 3: Funcionalidades Avanzadas (Semanas 9-14)
- **Semanas 9-10**: Sistema de encuestas y notificaciones
- **Semanas 11-12**: Bienestar estudiantil y reportes
- **Semanas 13-14**: Optimización y testing

#### Fase 4: Finalización (Semanas 15-18)
- **Semanas 15-16**: Testing integral y corrección de bugs
- **Semanas 17-18**: Documentación final y deployment

### Recursos Necesarios

#### Humanos
- **3 Desarrolladores** (equipo completo)
- **1 Product Owner** (Pablo Avendaño)
- **1 Scrum Master** (Darosh Luco)
- **1 Tester** (Isaac Paz)

#### Técnicos
- **Servidor de desarrollo** (local)
- **Base de datos** (PostgreSQL)
- **Herramientas de desarrollo** (VS Code, Git)
- **Servicios en la nube** (opcional para deployment)

#### Materiales
- **Documentación técnica** (Django, DRF, PWA)
- **Recursos de diseño** (Bootstrap, iconos)
- **Imágenes para Street View** (fotografías de la sede)

### Facilitadores
1. **Conocimiento previo** de las tecnologías
2. **Herramientas gratuitas** disponibles
3. **Apoyo institucional** para el proyecto
4. **Comunidad estudiantil** para testing
5. **Documentación abundante** de las tecnologías

### Obstaculizadores
1. **Complejidad técnica** de algunas funcionalidades
2. **Tiempo limitado** para testing exhaustivo
3. **Coordinación** entre miembros del equipo
4. **Recursos limitados** para deployment en producción
5. **Dependencias externas** (APIs, servicios)

### Estrategias de Mitigación
- **Planificación detallada** con buffers de tiempo
- **Testing temprano** y continuo
- **Comunicación constante** del equipo
- **Documentación completa** para facilitar mantenimiento
- **Arquitectura modular** para reducir dependencias

## 8. Evidencias del Proyecto

### Evidencias Técnicas
1. **Código fuente** completo en GitHub
2. **Documentación técnica** detallada
3. **Base de datos** con datos de ejemplo
4. **Tests automatizados** con cobertura > 80%
5. **Deployment** en ambiente de producción

### Evidencias de Funcionalidad
1. **Demo en vivo** de la plataforma
2. **Videos de funcionalidades** principales
3. **Capturas de pantalla** de la interfaz
4. **Casos de uso** documentados
5. **Feedback de usuarios** beta

### Evidencias de Proceso
1. **Actas de reuniones** de equipo
2. **Sprints completados** con entregables
3. **Retrospectivas** y mejoras implementadas
4. **Métricas de progreso** y productividad
5. **Documentación de decisiones** técnicas

### Evidencias de Calidad
1. **Reportes de testing** y cobertura
2. **Análisis de performance** y optimización
3. **Auditoría de seguridad** y vulnerabilidades
4. **Revisión de código** y mejores prácticas
5. **Documentación de usuario** y manual técnico

### Justificación de Evidencias
Las evidencias seleccionadas permiten demostrar:
- **Competencia técnica** en desarrollo de software
- **Aplicación de metodologías** ágiles de gestión
- **Calidad del producto** entregado
- **Proceso de desarrollo** sistemático y documentado
- **Impacto real** en la comunidad estudiantil

## 9. Cumplimiento con Indicadores de Calidad

### Desarrollo de Software
- ✅ **Implementación robusta** utilizando Django 5.0 + DRF
- ✅ **Arquitectura escalable** con separación de responsabilidades
- ✅ **API RESTful** con documentación Swagger
- ✅ **PWA funcional** con Service Worker y Manifest
- ✅ **Testing sistemático** con cobertura > 80%

### Gestión de Proyectos
- ✅ **Metodología Scrum** implementada correctamente
- ✅ **Sprints de 2 semanas** con entregas incrementales
- ✅ **Herramientas de gestión** (GitHub, Trello) utilizadas
- ✅ **Retrospectivas** y mejora continua
- ✅ **Documentación de proceso** completa

### Modelado de Datos
- ✅ **Diseño relacional** optimizado y normalizado
- ✅ **Base de datos escalable** (PostgreSQL)
- ✅ **Índices apropiados** para performance
- ✅ **Migraciones** documentadas y versionadas
- ✅ **Datos de ejemplo** para testing

### Ciberseguridad
- ✅ **Autenticación JWT** con validación de dominios
- ✅ **Autorización granular** con roles y permisos
- ✅ **Validación de inputs** y sanitización
- ✅ **Sistema de moderación** automático y manual
- ✅ **Protección contra ataques** comunes

### Calidad de Software (QA)
- ✅ **Tests unitarios** para componentes críticos
- ✅ **Tests de integración** para flujos completos
- ✅ **Tests de aceptación** para casos de uso
- ✅ **Cobertura de código** > 80%
- ✅ **Performance** < 2 segundos de respuesta

## 10. Conclusión

DuocPoint representa una solución integral e innovadora para las necesidades de la comunidad estudiantil de Duoc UC. El proyecto demuestra competencias técnicas avanzadas, aplicación de metodologías ágiles y un enfoque en la calidad del software.

### Logros Principales
1. **Plataforma funcional** con todas las funcionalidades implementadas
2. **Arquitectura robusta** y escalable
3. **Metodología Scrum** aplicada exitosamente
4. **Calidad de código** con testing sistemático
5. **Documentación completa** técnica y de usuario

### Impacto Esperado
- **Mejora en la comunicación** entre miembros de la comunidad
- **Facilitación del acceso** a recursos académicos
- **Fomento de la interacción** entre carreras y sedes
- **Desarrollo profesional** de los estudiantes
- **Eficiencia operativa** de la institución

### Futuro del Proyecto
- **Integración** con sistemas existentes de Duoc UC
- **Expansión** a otras sedes de la institución
- **Mejoras continuas** basadas en feedback de usuarios
- **Mantenimiento** y actualizaciones regulares
- **Escalabilidad** para mayor número de usuarios

El proyecto DuocPoint cumple y supera los estándares de calidad establecidos, demostrando competencias profesionales avanzadas y un compromiso con la excelencia técnica y la innovación en el desarrollo de software.

---

**Documento preparado por**:  
Pablo Avendaño, Darosh Luco, Isaac Paz  
**Fecha**: Enero 2024  
**Asignatura**: APT122 - Proyecto de Título  
**Institución**: Duoc UC - Sede Maipú
