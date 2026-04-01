# JWT

JWT (JSON Web Token) es un formato de token que se usa para transmitir información segura entre partes, normalmente después de que un usuario se autentica.

Principalmente para:

- Autenticación
- Autorización
- Manejo de sesiones
- APIs
- Microservicios

Un JWT tiene tres partes

HEADER.PAYLOAD.SIGNATURE

## Header

Contiene información sobre el token:

```JSON
{
  "alg": "HS256",
  "typ": "JWT"
}
```

alg: algoritmo de firma.
typ: "JWT"

## Payload

Contiene los datos del usuario

```JSON
{
  "userId": 123,
  "role": "ADMIN",
  "exp": 1710000000
}
```

Cada uno se llama claims

### Tipos de Claims

_Registered claims_
exp → expiración
sub → sujeto
iss → emisor
aud → audiencia
_Public claims_
Definidos por la aplicación

- Role
- Permissions
  _Private claims_

  Información interna.

Ejemplo:

userId
email

## Signature

Es lo que hace seguro al token.

Sirve para:

verificar integridad
evitar manipulación

Se genera con:

clave secreta
algoritmo criptográfico

# Como funciona

## Paso 1

El usuario escribe sus credenciales en el frontend:

```
usuario: sergio
password: 123456
```

El frontend envía una petición al backend.
Request al servidor

```
POST /login
Content-Type: application/json
```

```JSON
{
  "username": "sergio",
  "password": "123456"
}
```

## Paso 2: Servidor valida las credenciales

Aquí ocurre la autenticación. El servidor:

1. Busca el usuario en la base de datos
2. Obtiene el salt del hash almacenado.

Ese hash fue generado con bcrypt, argon2, scrypt.

Un hash típico tiene algoritmo + salt + hash.

3. Convierte el password en hash
4. Compara los hashes.
5. Si coincide: Usuario autenticado. Si no, Error 404 Unauthorized

## Paso 3: Servidor genera el JWT

Con el usuario autenticado el servidor crea el token. Primero los claims

```JSON
{
  "sub": "123",
  "username": "sergio",
  "role": "USER",
  "iat": 1710000000,
  "exp": 1710003600
}
```

| Claim    | Significado         |
| -------- | ------------------- |
| sub      | ID del usuario      |
| username | nombre              |
| role     | rol                 |
| iat      | momento de creación |
| exp      | expiración          |

## Paso 4: El servidor firma el token

1. Toma header y payload
2. Usa una clave secreta
3. Aplica el algoritmo
4. Genera la firma

## Paso 5: Servidor envía el token al cliente

El backend responde:

```http
200 OK
```

```JSON
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

## Paso 6: cliente guarda el token

Queda guardado el JWT en memoria, localstorage o cookie

## Paso 7: El cliente hace una petición a la API

Ahora el usuario quiere acceder a un recurso.

Por ejemplo:

## Paso 8: El servidor interpreta la petición.

Ocurre antes de que se ejecute el endpoint. Aquí entra un middleware.

1. Revisa si el token antes de ejecutar el endpoint.
2. Lee el header.
3. Extrae el token
4. Valida el token. Paso 9

## Paso 9: validación token.

### Verificación 1: Firma

El servidor recalcula la firma y la compara.

Recalcula

```
firma_calculada = HASH(header + payload + SECRET_KEY)
```

Compara

```
firma_calculada == firma_del_token
```

Si coincide, token válido. Si no coincide, token no válido.

### Verificación 2: Expiración

El servidor revisa exp. Si el momento actual es menor, se define como expirado.

### Verificación 3: Estructura

Formato correcto
Claims requeridos
Algoritmo permitido

### Verificación 4: Issuer (Iss) - Audience (aud)

Quién emite el token y para quién fue emitido.
