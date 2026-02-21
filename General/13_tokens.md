# ¿Qué es un token?

Es un string firmado digitalmente que contiene:

- user id
- expiración
- permisos

El servidor

- Firma el token con una clave secreta
- Luego puede verificar esa firma

Con token el flujo es:

1. Usuario hace login
2. Servidor genera un token firmado
3. Cliente guarda el token

Cada request incluye:

```
Authorization: Bearer <token>
```

El servidor:

- No guarda nada
- Solo verifica que el token sea válido

Entonces:

- Request 1 puede ir a servidor A
- Request 2 a servidor B
- Request 3 a servidor C

Todos pueden verificar el token sin depender de memoria compartida. Eso permite:

- Escalar horizontalmente
- Balancear tráfico fácilmente
- No necesitar sticky sessions

# Hay varios tipos de token

## Session token

El servidor guarda sesión en base de datos o memoria.

El cliente guarda solo un ID de sesión (cookie).

No es completamente stateless

## JWL (JSON Web Token)

Muy popular en APIs modernas.

Es un string firmado que contiene:

- user_id
- expiración
- claims (roles, permisos)

Ventajas:

- No requiere consultar DB siempre
- Stateless real
