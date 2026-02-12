# API

Una API es una interfaz que permite la comunicación entre sistemas, definiendo cómo solicitar y recibir información sin exponer la implementación interna. Puede ser web, de librería o de sistema.

## API Rest

REST = Representational State Transfer

Es un estilo de arquitectura para diseñar APIs web.

No es una librería ni un protocolo, sino un conjunto de principios.

## Clasificación de códigos HTTP

### 2xx — Éxito

La petición fue correcta.

- 200 OK → Todo salió bien
- 201 Created → Se creó un recurso (muy común en POST)
- 204 No Content → Éxito, pero sin respuesta

“Lo que pediste funcionó”

### 3xx — Redirección

El recurso está en otro lugar.

- 301 Moved Permanently
- 302 Found

Más común en navegación web que en APIs REST.

### 4xx — Error del cliente

El cliente hizo algo mal.

- 400 Bad Request → Datos inválidos
- 401 Unauthorized → No autenticado
- 403 Forbidden → No tienes permisos
- 404 Not Found → Recurso no existe

“El problema está en la petición”

### 5xx — Error del servidor

El cliente pidió bien, pero el servidor falló.

- 500 Internal Server Error → Error genérico
- 502 Bad Gateway
- 503 Service Unavailable

“La culpa es del servidor”
