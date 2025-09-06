# Plan de Pruebas - DuocPoint

## 1. Objetivo del Plan de Pruebas

El objetivo de este plan es validar que el sistema DuocPoint cumple con todos los requerimientos funcionales y no funcionales establecidos, garantizando la calidad, confiabilidad y usabilidad de la plataforma.

## 2. Alcance de las Pruebas

### 2.1 Incluido en el Alcance
- Sistema de autenticación y gestión de usuarios
- Sistema de foros con moderación
- Sistema de compra/venta
- Sistema de portafolio
- Sistema de encuestas
- Recorridos virtuales
- Notificaciones push
- API REST
- Interfaz de usuario (PWA)
- Integración con servicios externos

### 2.2 Excluido del Alcance
- Sistemas externos de Duoc UC
- Integración con Moodle
- Sistemas de pago externos
- Aplicaciones móviles nativas

## 3. Estrategia de Pruebas

### 3.1 Tipos de Pruebas
- **Pruebas Unitarias**: Validación de componentes individuales
- **Pruebas de Integración**: Validación de interacción entre módulos
- **Pruebas de Sistema**: Validación del sistema completo
- **Pruebas de Aceptación**: Validación de requerimientos de usuario
- **Pruebas de Rendimiento**: Validación de performance
- **Pruebas de Seguridad**: Validación de vulnerabilidades
- **Pruebas de Usabilidad**: Validación de experiencia de usuario

### 3.2 Niveles de Pruebas
- **Nivel 1**: Pruebas de humo (smoke tests)
- **Nivel 2**: Pruebas funcionales básicas
- **Nivel 3**: Pruebas funcionales avanzadas
- **Nivel 4**: Pruebas de rendimiento y seguridad

## 4. Casos de Prueba

### 4.1 Autenticación y Gestión de Usuarios

#### CP001: Registro de Usuario Válido
- **Objetivo**: Verificar que un usuario con email válido puede registrarse
- **Precondiciones**: Sistema funcionando, base de datos limpia
- **Pasos**:
  1. Acceder a la página de registro
  2. Ingresar email @duocuc.cl
  3. Ingresar contraseña válida
  4. Confirmar contraseña
  5. Hacer clic en "Registrar"
- **Resultado Esperado**: Usuario registrado exitosamente
- **Prioridad**: Alta

#### CP002: Registro con Email Inválido
- **Objetivo**: Verificar que emails no autorizados son rechazados
- **Precondiciones**: Sistema funcionando
- **Pasos**:
  1. Acceder a la página de registro
  2. Ingresar email @hotmail.com
  3. Ingresar contraseña válida
  4. Hacer clic en "Registrar"
- **Resultado Esperado**: Error de validación mostrado
- **Prioridad**: Alta

#### CP003: Login Exitoso
- **Objetivo**: Verificar que usuarios válidos pueden iniciar sesión
- **Precondiciones**: Usuario registrado en el sistema
- **Pasos**:
  1. Acceder a la página de login
  2. Ingresar email válido
  3. Ingresar contraseña correcta
  4. Hacer clic en "Iniciar Sesión"
- **Resultado Esperado**: Usuario autenticado y redirigido al dashboard
- **Prioridad**: Alta

### 4.2 Sistema de Foros

#### CP004: Crear Post Exitoso
- **Objetivo**: Verificar que usuarios pueden crear posts
- **Precondiciones**: Usuario autenticado
- **Pasos**:
  1. Acceder al foro
  2. Hacer clic en "Nuevo Post"
  3. Seleccionar foro
  4. Escribir título y contenido
  5. Hacer clic en "Publicar"
- **Resultado Esperado**: Post creado y visible en el foro
- **Prioridad**: Alta

#### CP005: Moderación Automática
- **Objetivo**: Verificar que contenido inapropiado es moderado automáticamente
- **Precondiciones**: Usuario autenticado, palabras prohibidas configuradas
- **Pasos**:
  1. Crear post con palabras prohibidas
  2. Intentar publicar
- **Resultado Esperado**: Post enviado a revisión automáticamente
- **Prioridad**: Alta

#### CP006: Reportar Post
- **Objetivo**: Verificar que usuarios pueden reportar contenido inapropiado
- **Precondiciones**: Usuario autenticado, post existente
- **Pasos**:
  1. Ver post en el foro
  2. Hacer clic en "Reportar"
  3. Seleccionar tipo de reporte
  4. Agregar descripción
  5. Enviar reporte
- **Resultado Esperado**: Reporte registrado y contador incrementado
- **Prioridad**: Media

### 4.3 Sistema de Compra/Venta

#### CP007: Publicar Producto
- **Objetivo**: Verificar que usuarios pueden publicar productos
- **Precondiciones**: Usuario autenticado
- **Pasos**:
  1. Acceder al mercado
  2. Hacer clic en "Vender"
  3. Seleccionar categoría
  4. Completar información del producto
  5. Subir imágenes
  6. Publicar
- **Resultado Esperado**: Producto publicado y visible en el mercado
- **Prioridad**: Media

#### CP008: Buscar Productos
- **Objetivo**: Verificar funcionalidad de búsqueda
- **Precondiciones**: Productos publicados en el sistema
- **Pasos**:
  1. Acceder al mercado
  2. Usar filtros de búsqueda
  3. Ver resultados
- **Resultado Esperado**: Productos filtrados correctamente
- **Prioridad**: Media

### 4.4 Sistema de Portafolio

#### CP009: Completar Perfil
- **Objetivo**: Verificar que usuarios pueden completar su perfil
- **Precondiciones**: Usuario autenticado
- **Pasos**:
  1. Acceder al portafolio
  2. Completar información personal
  3. Agregar logros
  4. Agregar proyectos
  5. Agregar habilidades
- **Resultado Esperado**: Perfil completado y porcentaje actualizado
- **Prioridad**: Media

#### CP010: Generar PDF
- **Objetivo**: Verificar generación de PDF del portafolio
- **Precondiciones**: Portafolio completado al 70%
- **Pasos**:
  1. Acceder al portafolio
  2. Hacer clic en "Generar PDF"
  3. Esperar procesamiento
  4. Descargar archivo
- **Resultado Esperado**: PDF generado y descargado exitosamente
- **Prioridad**: Media

### 4.5 Sistema de Encuestas

#### CP011: Crear Encuesta
- **Objetivo**: Verificar que moderadores pueden crear encuestas
- **Precondiciones**: Usuario con rol de moderador
- **Pasos**:
  1. Acceder a panel de administración
  2. Crear nueva encuesta
  3. Agregar opciones
  4. Configurar visibilidad
  5. Publicar
- **Resultado Esperado**: Encuesta creada y visible para usuarios
- **Prioridad**: Baja

#### CP012: Votar en Encuesta
- **Objetivo**: Verificar que usuarios pueden votar
- **Precondiciones**: Encuesta activa, usuario autenticado
- **Pasos**:
  1. Ver encuesta en el foro
  2. Seleccionar opción
  3. Enviar voto
- **Resultado Esperado**: Voto registrado y resultados actualizados
- **Prioridad**: Baja

## 5. Pruebas de Rendimiento

### 5.1 Carga de Usuarios
- **Objetivo**: Verificar que el sistema soporta 1000 usuarios concurrentes
- **Método**: Herramientas de carga (JMeter, Locust)
- **Métricas**: Tiempo de respuesta, throughput, errores
- **Criterios**: Tiempo de respuesta < 2 segundos, errores < 1%

### 5.2 Base de Datos
- **Objetivo**: Verificar performance de consultas
- **Método**: Análisis de queries lentas
- **Métricas**: Tiempo de ejecución, uso de recursos
- **Criterios**: Queries < 100ms, uso de CPU < 80%

## 6. Pruebas de Seguridad

### 6.1 Autenticación
- **Objetivo**: Verificar seguridad de autenticación
- **Método**: Pruebas de penetración
- **Aspectos**: JWT tokens, rate limiting, validación de inputs
- **Criterios**: No vulnerabilidades críticas

### 6.2 Autorización
- **Objetivo**: Verificar control de acceso
- **Método**: Pruebas de roles y permisos
- **Aspectos**: Acceso a recursos, escalación de privilegios
- **Criterios**: Usuarios solo acceden a recursos autorizados

## 7. Pruebas de Usabilidad

### 7.1 Navegación
- **Objetivo**: Verificar facilidad de navegación
- **Método**: Pruebas con usuarios reales
- **Aspectos**: Menús, enlaces, flujo de trabajo
- **Criterios**: Usuarios completan tareas sin ayuda

### 7.2 Responsive Design
- **Objetivo**: Verificar funcionamiento en diferentes dispositivos
- **Método**: Pruebas en múltiples dispositivos
- **Aspectos**: Layout, funcionalidad, performance
- **Criterios**: Funciona correctamente en móvil, tablet, desktop

## 8. Criterios de Aceptación

### 8.1 Funcionalidad
- [ ] 100% de casos de prueba críticos pasando
- [ ] 95% de casos de prueba importantes pasando
- [ ] 90% de casos de prueba opcionales pasando

### 8.2 Rendimiento
- [ ] Tiempo de respuesta < 2 segundos
- [ ] Soporte para 1000 usuarios concurrentes
- [ ] Disponibilidad > 99.5%

### 8.3 Seguridad
- [ ] No vulnerabilidades críticas
- [ ] Validación de inputs implementada
- [ ] Autenticación y autorización funcionando

### 8.4 Usabilidad
- [ ] Navegación intuitiva
- [ ] Funciona en todos los dispositivos
- [ ] PWA instalable y funcional

## 9. Entorno de Pruebas

### 9.1 Ambiente de Desarrollo
- **Propósito**: Pruebas unitarias y de integración
- **Configuración**: SQLite, modo debug activado
- **Acceso**: Solo desarrolladores

### 9.2 Ambiente de Staging
- **Propósito**: Pruebas de sistema y aceptación
- **Configuración**: PostgreSQL, configuración de producción
- **Acceso**: Equipo de QA y stakeholders

### 9.3 Ambiente de Producción
- **Propósito**: Pruebas de humo post-deployment
- **Configuración**: Configuración real de producción
- **Acceso**: Equipo de operaciones

## 10. Cronograma de Pruebas

### Fase 1: Preparación (Semana 1)
- Configuración de entornos de prueba
- Preparación de datos de prueba
- Configuración de herramientas

### Fase 2: Pruebas Unitarias (Semana 2)
- Ejecución de pruebas unitarias
- Corrección de defectos críticos
- Documentación de resultados

### Fase 3: Pruebas de Integración (Semana 3)
- Pruebas de integración entre módulos
- Pruebas de API
- Pruebas de base de datos

### Fase 4: Pruebas de Sistema (Semana 4)
- Pruebas end-to-end
- Pruebas de rendimiento
- Pruebas de seguridad

### Fase 5: Pruebas de Aceptación (Semana 5)
- Pruebas con usuarios finales
- Pruebas de usabilidad
- Validación de requerimientos

## 11. Reportes y Métricas

### 11.1 Reportes Diarios
- Casos de prueba ejecutados
- Defectos encontrados
- Estado de correcciones

### 11.2 Reportes Semanales
- Progreso del plan de pruebas
- Métricas de calidad
- Riesgos identificados

### 11.3 Reporte Final
- Resumen de resultados
- Métricas de cobertura
- Recomendaciones

## 12. Gestión de Defectos

### 12.1 Clasificación de Defectos
- **Crítico**: Bloquea funcionalidad principal
- **Alto**: Afecta funcionalidad importante
- **Medio**: Afecta funcionalidad secundaria
- **Bajo**: Mejora o optimización

### 12.2 Flujo de Defectos
1. Identificación y reporte
2. Clasificación y asignación
3. Corrección por desarrolladores
4. Verificación por QA
5. Cierre del defecto

### 12.3 Criterios de Cierre
- Defecto corregido y verificado
- Pruebas de regresión ejecutadas
- Documentación actualizada
- Aprobación del stakeholder
