# Diagramas del Sistema - DuocPoint

## Diagrama de Arquitectura General

```mermaid
graph TB
    subgraph "Frontend"
        A[PWA Web App]
        B[Service Worker]
        C[Manifest]
    end
    
    subgraph "Backend"
        D[Django + DRF]
        E[Celery Worker]
        F[Redis]
    end
    
    subgraph "Base de Datos"
        G[PostgreSQL]
    end
    
    subgraph "Servicios Externos"
        H[Google OAuth]
        I[Web Push]
        J[OpenGraph]
    end
    
    A --> D
    D --> G
    D --> E
    E --> F
    D --> H
    D --> I
    D --> J
    B --> A
    C --> A
```

## Diagrama de Base de Datos

```mermaid
erDiagram
    User ||--o{ Post : creates
    User ||--o{ Producto : sells
    User ||--o{ Logro : has
    User ||--o{ Proyecto : creates
    User ||--o{ Habilidad : has
    
    Sede ||--o{ Foro : contains
    Sede ||--o{ Recorrido : has
    Sede ||--o{ User : belongs_to
    
    Foro ||--o{ Post : contains
    Post ||--o{ Comentario : has
    Post ||--o{ PostReporte : reported_by
    Post ||--o{ VotoPost : voted_by
    
    CategoriaProducto ||--o{ Producto : categorizes
    Producto ||--o{ ProductoFavorito : favorited_by
    Producto ||--o{ ProductoReporte : reported_by
    
    Poll ||--o{ PollOpcion : has
    Poll ||--o{ PollVoto : voted_by
    
    User {
        int id PK
        string email UK
        string name
        string role
        int campus_id FK
        string career
        boolean es_estudiante_gmail
    }
    
    Post {
        int id PK
        int foro_id FK
        int usuario_id FK
        string titulo
        text cuerpo
        string estado
        int score
        datetime created_at
    }
    
    Producto {
        int id PK
        int vendedor_id FK
        int categoria_id FK
        string titulo
        text descripcion
        decimal precio
        string estado
    }
```

## Diagrama de Flujo de Moderación

```mermaid
flowchart TD
    A[Usuario crea post] --> B{Contenido verificado}
    B -->|Palabras prohibidas| C[Estado: Revisión]
    B -->|Palabras moderación| D[Estado: Revisión]
    B -->|Contenido limpio| E[Estado: Publicado]
    
    C --> F[Moderador revisa]
    D --> F
    F --> G{Decisión moderador}
    G -->|Aprobar| E
    G -->|Rechazar| H[Estado: Rechazado]
    G -->|Ocultar| I[Estado: Oculto]
    
    J[Usuario reporta post] --> K[Contador reportes +1]
    K --> L{Reportes >= 3?}
    L -->|Sí| C
    L -->|No| M[Post permanece activo]
```

## Diagrama de Componentes Frontend

```mermaid
graph TB
    subgraph "Páginas Principales"
        A[Index.html]
        B[Forum/index.html]
        C[Forum/moderation.html]
        D[Market/index.html]
        E[Portfolio/index.html]
        F[StreetView/index.html]
    end
    
    subgraph "Componentes JS"
        G[forum.js]
        H[moderation.js]
        I[market.js]
        J[streetview.js]
    end
    
    subgraph "Estilos"
        K[forum.css]
        L[market.css]
        M[streetview.css]
    end
    
    A --> G
    B --> G
    C --> H
    D --> I
    E --> J
    F --> J
    
    B --> K
    C --> K
    D --> L
    F --> M
```

## Diagrama de API REST

```mermaid
graph TB
    subgraph "Autenticación"
        A1[POST /api/auth/login/]
        A2[POST /api/auth/refresh/]
        A3[GET /api/accounts/me/]
    end
    
    subgraph "Foros"
        F1[GET /api/forum/foros/]
        F2[GET /api/forum/posts/]
        F3[POST /api/forum/posts/]
        F4[POST /api/forum/posts/{id}/reportar/]
        F5[POST /api/forum/posts/{id}/moderar/]
    end
    
    subgraph "Mercado"
        M1[GET /api/market/productos/]
        M2[POST /api/market/productos/]
        M3[GET /api/market/categorias/]
    end
    
    subgraph "Portafolio"
        P1[GET /api/portfolio/portafolio-completo/]
        P2[POST /api/portfolio/generar-pdf/]
    end
    
    subgraph "Encuestas"
        E1[GET /api/polls/]
        E2[POST /api/polls/{id}/votar/]
    end
```

## Diagrama de Deployment

```mermaid
graph TB
    subgraph "Servidor de Producción"
        A[Nginx]
        B[Gunicorn]
        C[Django App]
        D[Celery Worker]
        E[Redis]
        F[PostgreSQL]
    end
    
    subgraph "Cliente"
        G[Navegador Web]
        H[PWA Mobile]
    end
    
    subgraph "Servicios Externos"
        I[Google OAuth]
        J[Web Push Service]
        K[AWS S3]
    end
    
    G --> A
    H --> A
    A --> B
    B --> C
    C --> D
    C --> E
    C --> F
    C --> I
    C --> J
    C --> K
```

## Diagrama de Flujo de Usuario

```mermaid
journey
    title Flujo de Usuario Típico
    section Login
      Acceder a la plataforma: 5: Usuario
      Iniciar sesión: 4: Usuario
      Verificar dominio email: 5: Sistema
    section Navegación
      Explorar foros: 5: Usuario
      Leer posts: 4: Usuario
      Crear post: 3: Usuario
    section Moderación
      Sistema verifica contenido: 5: Sistema
      Moderador revisa: 4: Moderador
      Aprobar/Rechazar: 5: Moderador
    section Mercado
      Buscar productos: 4: Usuario
      Ver detalles: 5: Usuario
      Contactar vendedor: 3: Usuario
    section Portafolio
      Completar perfil: 4: Usuario
      Agregar proyectos: 5: Usuario
      Generar PDF: 5: Sistema
```
