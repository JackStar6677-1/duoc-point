# Análisis de Requerimientos - DuocPoint

## 1. Requerimientos Funcionales

### 1.1 Gestión de Usuarios
- **RF001**: El sistema debe permitir registro solo con emails @duocuc.cl y @gmail.com
- **RF002**: El sistema debe validar automáticamente el dominio del email
- **RF003**: El sistema debe soportar roles: estudiante, moderador, director de carrera, administrador
- **RF004**: El sistema debe permitir autenticación JWT
- **RF005**: El sistema debe permitir recuperación de contraseña

### 1.2 Sistema de Foros
- **RF006**: El sistema debe permitir crear foros por carrera
- **RF007**: El sistema debe permitir crear posts con título y contenido
- **RF008**: El sistema debe permitir comentar posts
- **RF009**: El sistema debe permitir votar posts (positivo/negativo)
- **RF010**: El sistema debe permitir reportar contenido inapropiado
- **RF011**: El sistema debe moderar automáticamente contenido con palabras prohibidas
- **RF012**: El sistema debe permitir moderación manual por administradores

### 1.3 Sistema de Compra/Venta
- **RF013**: El sistema debe permitir publicar productos con categorías
- **RF014**: El sistema debe permitir subir imágenes de productos
- **RF015**: El sistema debe permitir marcar productos como favoritos
- **RF016**: El sistema debe permitir reportar productos inapropiados
- **RF017**: El sistema debe mostrar previsualización OpenGraph de enlaces

### 1.4 Sistema de Portafolio
- **RF018**: El sistema debe permitir gestionar logros académicos
- **RF019**: El sistema debe permitir gestionar proyectos realizados
- **RF020**: El sistema debe permitir gestionar experiencia laboral
- **RF021**: El sistema debe permitir gestionar habilidades técnicas
- **RF022**: El sistema debe generar PDF profesional del portafolio
- **RF023**: El sistema debe calcular porcentaje de completitud

### 1.5 Sistema de Encuestas
- **RF024**: El sistema debe permitir crear encuestas con opciones múltiples
- **RF025**: El sistema debe permitir votar en encuestas
- **RF026**: El sistema debe mostrar resultados en tiempo real o al cierre
- **RF027**: El sistema debe permitir encuestas anónimas

### 1.6 Recorridos Virtuales
- **RF028**: El sistema debe mostrar mapa interactivo de la sede
- **RF029**: El sistema debe permitir recorridos virtuales con imágenes 360°
- **RF030**: El sistema debe mostrar información de puntos de interés

### 1.7 Notificaciones
- **RF031**: El sistema debe enviar notificaciones Web Push
- **RF032**: El sistema debe permitir configurar preferencias de notificación
- **RF033**: El sistema debe enviar recordatorios de clases

## 2. Requerimientos No Funcionales

### 2.1 Rendimiento
- **RNF001**: El sistema debe responder en menos de 2 segundos
- **RNF002**: El sistema debe soportar 1000 usuarios concurrentes
- **RNF003**: El sistema debe tener disponibilidad del 99.5%

### 2.2 Seguridad
- **RNF004**: El sistema debe usar HTTPS en producción
- **RNF005**: El sistema debe validar todos los inputs
- **RNF006**: El sistema debe implementar rate limiting
- **RNF007**: El sistema debe encriptar contraseñas

### 2.3 Usabilidad
- **RNF008**: El sistema debe ser responsive (móvil, tablet, desktop)
- **RNF009**: El sistema debe ser PWA instalable
- **RNF010**: El sistema debe tener interfaz intuitiva
- **RNF011**: El sistema debe soportar modo offline básico

### 2.4 Compatibilidad
- **RNF012**: El sistema debe funcionar en Chrome, Firefox, Safari, Edge
- **RNF013**: El sistema debe funcionar en iOS y Android
- **RNF014**: El sistema debe usar estándares web modernos

### 2.5 Escalabilidad
- **RNF015**: El sistema debe usar arquitectura modular
- **RNF016**: El sistema debe soportar horizontal scaling
- **RNF017**: El sistema debe usar base de datos optimizada

## 3. Requerimientos de Integración

### 3.1 APIs Externas
- **RI001**: Integración con Google OAuth (opcional)
- **RI002**: Integración con servicios de notificaciones push
- **RI003**: Integración con OpenGraph para previsualizaciones

### 3.2 Sistemas Internos
- **RI004**: Integración con sistema de horarios de Duoc UC
- **RI005**: Integración con directorio de estudiantes
- **RI006**: Integración con sistema de calificaciones (futuro)

## 4. Requerimientos de Datos

### 4.1 Almacenamiento
- **RD001**: El sistema debe almacenar datos de usuarios de forma segura
- **RD002**: El sistema debe respaldar datos diariamente
- **RD003**: El sistema debe retener logs por 1 año
- **RD004**: El sistema debe permitir exportar datos de usuario

### 4.2 Privacidad
- **RD005**: El sistema debe cumplir con LGPD
- **RD006**: El sistema debe permitir eliminar datos personales
- **RD007**: El sistema debe notificar sobre uso de cookies

## 5. Requerimientos de Deployment

### 5.1 Infraestructura
- **RDP001**: El sistema debe usar Docker para deployment
- **RDP002**: El sistema debe usar PostgreSQL en producción
- **RDP003**: El sistema debe usar Redis para cache
- **RDP004**: El sistema debe usar Nginx como proxy reverso

### 5.2 Monitoreo
- **RDP005**: El sistema debe registrar logs de aplicación
- **RDP006**: El sistema debe monitorear performance
- **RDP007**: El sistema debe alertar sobre errores críticos

## 6. Requerimientos de Mantenimiento

### 6.1 Actualizaciones
- **RM001**: El sistema debe permitir actualizaciones sin downtime
- **RM002**: El sistema debe mantener compatibilidad con versiones anteriores
- **RM003**: El sistema debe documentar cambios en API

### 6.2 Soporte
- **RM004**: El sistema debe incluir documentación técnica
- **RM005**: El sistema debe incluir manual de usuario
- **RM006**: El sistema debe incluir guías de troubleshooting

## 7. Matriz de Trazabilidad

| Requerimiento | Módulo | Estado | Prioridad |
|---------------|--------|--------|-----------|
| RF001-RF005 | accounts | ✅ Completo | Alta |
| RF006-RF012 | forum | ✅ Completo | Alta |
| RF013-RF017 | market | ✅ Completo | Media |
| RF018-RF023 | portfolio | ✅ Completo | Media |
| RF024-RF027 | polls | ✅ Completo | Baja |
| RF028-RF030 | campuses | ✅ Completo | Media |
| RF031-RF033 | notifications | ✅ Completo | Baja |
| RNF001-RNF017 | Sistema | ✅ Completo | Alta |
| RI001-RI003 | Integraciones | ✅ Completo | Baja |
| RD001-RD007 | Datos | ✅ Completo | Alta |
| RDP001-RDP007 | Deployment | ✅ Completo | Media |
| RM001-RM006 | Mantenimiento | ✅ Completo | Baja |

## 8. Criterios de Aceptación

### 8.1 Funcionalidad
- [ ] Todos los requerimientos funcionales implementados
- [ ] Tests unitarios con cobertura > 80%
- [ ] Tests de integración pasando
- [ ] Manual de usuario completo

### 8.2 Calidad
- [ ] Código revisado y documentado
- [ ] Performance dentro de límites establecidos
- [ ] Seguridad validada
- [ ] Accesibilidad básica implementada

### 8.3 Deployment
- [ ] Sistema desplegado en ambiente de producción
- [ ] Monitoreo configurado
- [ ] Backup automatizado
- [ ] Documentación de deployment actualizada

## 9. Riesgos y Mitigaciones

### 9.1 Riesgos Técnicos
- **Riesgo**: Dependencias externas no disponibles
- **Mitigación**: Implementar fallbacks y servicios alternativos

- **Riesgo**: Performance degradada con muchos usuarios
- **Mitigación**: Implementar cache y optimizaciones de base de datos

### 9.2 Riesgos de Negocio
- **Riesgo**: Baja adopción por parte de estudiantes
- **Mitigación**: Campaña de marketing y capacitación

- **Riesgo**: Contenido inapropiado en foros
- **Mitigación**: Sistema de moderación robusto y políticas claras

## 10. Métricas de Éxito

### 10.1 Métricas Técnicas
- Tiempo de respuesta < 2 segundos
- Disponibilidad > 99.5%
- Cobertura de tests > 80%
- Errores críticos < 0.1%

### 10.2 Métricas de Negocio
- Usuarios activos mensuales > 1000
- Posts creados por día > 50
- Productos publicados por semana > 20
- Satisfacción de usuarios > 4.0/5.0
