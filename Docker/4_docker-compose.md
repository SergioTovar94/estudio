# Partes

# version:

Indica la versión del docker compose. Si no se usa, docker la deecta automáticamente.

# services: (la más importante)

```YAML
services:

  nombre_del_servicio:
    configuración
```

Ejemplo

```YAML
services:

  postgres:
    image: postgres:16
```

## Image

Define qué imagen usar

```YAML
image: postgres:16
```

## build

Se usa cuando quieres construir una imagen desde un Dockerfile.

```YAML
build: .
```

construir la imagen usando el Dockerfile en esta carpeta.

También puede ser:

```YAML
build:
  context: .
  dockerfile: Dockerfile.dev
```

## ports

Define qué puerto del contenedor se expone.

```YAML
ports:
  - "8080:8080"
```

Significa:

puerto_local : puerto_contenedor

Ejemplo real:

```YAML
ports:
  - "5432:5432"
```

## environment

Define variables de entorno. Muy usado en:

- bases de datos
- APIs
- configuraciones

Ejemplo:

```YAML
environment:
  POSTGRES_DB: app
  POSTGRES_USER: admin
  POSTGRES_PASSWORD: secret
```

## volumes:

Define almacenamiento persistente.

Ejemplo:

```YAML
volumes:
  - datos:/var/lib/postgresql/data
```

## depends_on

Define qué servicio debe iniciar primero.

Ejemplo:

```YAML
depends_on:
  - db
```

## command

Define el comando que ejecutará el contenedor.

Ejemplo:

```YAML
command: python app.py
```

## restart

Define cuándo reiniciar el contenedor.

Ejemplo:

```YAML
restart: always
```

Opciones:

- no
- always
- on-failure
- unless-stopped

## container_name

Define el nombre del contenedor.

Ejemplo:

```YAML
container_name: mi-postgres
```

# volumes (sección global)

Esto define volúmenes reutilizables.

Ejemplo:

```YAML
volumes:
  datos:
```

Esto crea un volumen llamado "datos".

Luego se usa en un servicio:

```YAML
volumes:
  - datos:/var/lib/postgresql/data
```

# networks

Define redes entre contenedores.

Ejemplo:

```YAML
networks:
  backend-network:
```

Y luego:

```YAML
services:
    db:
        networks:
            - backend-network
```

Pero importante:

Docker crea una red automáticamente.

Por eso:

muchas veces no necesitas definirla.

```YAML

```
