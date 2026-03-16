# API

Una API es una interfaz que permite la comunicación entre sistemas, definiendo cómo solicitar y recibir información sin exponer la implementación interna. Puede ser web, de librería o de sistema.

## API Rest

REST = Representational State Transfer

Es un estilo de arquitectura para diseñar APIs web.

No es una librería ni un protocolo, sino un conjunto de principios.

Principios:

- Cliente servidor
- Stateless
- Recursos identificados por URL
- Uso correcto de métodos HTTP

Estos principios fueron definidos por Roy Fielding en sus tesis doctoral en el año 2000.

### Cliente - Servidor

El frontend y el backend están separados. El cliente hace request y el servidor responde.

Ejemplo: React app (cliente), API Django (Servidor).

Esto permite que cada uno evolucione por separado.

### Stateless (Sin Estado)

Cada request debe contener toda la información necesaria. El servidor no debe recordar nada de peticiones.

❌ Incorrecto:
El servidor guarda en memoria quién eres.

✅ Correcto:
Cada request envía un token de autenticación.

Esto hace que las APIs sean escalables y fáciles de balancear.

### Cacheable

Las respuestas deben indicar si pueden ser cacheables. Esto parte de la idea de que si los datos no cambian cada cierto tiempo, puede guardarse temporalmente una respuesta para reutirlizarla.

Si esa lista no cambia cada segundo, puedes guardarla 60 segundos.

Entonces:

- Usuario 1 hace request
- Servidor responde y guarda copia
- Usuario 2 hace request
- Se devuelve la copia
- No se ejecuta lógica ni consulta DB

Eso es cache. Por eso normalmente get puede ser cacheable y post no, porque post crea o modifica recursos.

### Interfaz uniforme

- Recursos identificados por URL.
- Uso correcto de métodos HTTP.
- Representaciones estándar (JSON)

Ejemplo:

```
GET     /pacientes/
POST    /pacientes/
GET     /pacientes/1/
PUT     /pacientes/1/
DELETE  /pacientes/1/
```

No haces:

```
POST /crearPaciente
POST /eliminarPaciente
```

### Layared System (Sistema por capas)

El cliente no sabe si habla

- Directamente con el servidor
- Con un proxy
- Con un gateway
- Con un balanceador

###

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
