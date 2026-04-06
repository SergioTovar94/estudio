# ¿Qué es Spring Security?

Imagina que tu aplicación Spring Boot es un edificio. Cualquier persona puede llegar a la puerta, pero no cualquiera puede entrar a todas las oficinas. Spring Security es el sistema de seguridad de ese edificio — controla quién entra, a dónde puede ir y qué puede hacer.

Spring Security es el módulo que maneja la seguridad de la aplicación.

Sin Spring Security, cualquier persona que conozca la URL de tu endpoint puede consumirlo. Por ejemplo:

```
GET http://localhost:8081/api/core/accounts
```

Se encarga de:

- autenticación
- autorización
- control de acceso
- protección contra ataques

## ¿Como funciona la cadena de filtros?

Cuando llega un request HTTP a Spring Boot, no llega directamente al Controller. Primero pasa por una cadena de filtros — como puestos de seguridad en fila:

```
Request HTTP
     │
     ▼
┌─────────────────────────────────┐
│         Filtro 1                │  ¿Tiene token? ¿Es válido?
├─────────────────────────────────┤
│         Filtro 2                │  ¿Tiene permisos para esta URL?
├─────────────────────────────────┤
│         Filtro 3                │  ¿Otros checks?
└─────────────────────────────────┘
     │
     ▼
  Controller
```

Si el request no pasa alguno de esos filtros, Spring Security lo rechaza con un 401 Unauthorized o 403 Forbidden — nunca llega al Controller.

**Los tres conceptos clave**
**Autenticación** — ¿Quién eres?: Verificar que el usuario es quien dice ser. Ejemplo: validar el token JWT o el usuario y contraseña.
**Autorización** — ¿Qué puedes hacer?: Una vez que sé quién eres, verificar si tienes permiso para acceder a ese recurso. Ejemplo: solo el dueño de una cuenta puede ver sus movimientos.
**SecurityContext** — La memoria de la sesión: Una vez que el usuario está autenticado, Spring Security guarda su identidad en un objeto llamado SecurityContext. Así cualquier parte de la aplicación puede preguntar "¿quién está haciendo este request?" sin volver a validar el token.

## Spring Security protege contra:

- CSRF
- XSS
- Session fixation
- Brute force

## Filtros

Spring Security maneja la seguridad mediante una cadena de filtros. Cada petición HTTP pasa por varios filtros antes de llegar a tu controlador. Algunos filtros son nativos de Spring Security (como el que maneja la autenticación básica), otros puedes crearlos para lógica personalizada.

### OncePerRequestFilter

Es una clase base que garantiza que el filtro se ejecute una sola vez por cada petición, incluso si el filtro está en varias cadenas. Es el estándar para filtros personalizados en Spring.

Este filtro se encarga de convertir las cabeceras HTTP que vienen del gateway en un objeto Authentication dentro del contexto de seguridad de Spring.

No valida tokens, no consulta una base de datos; solo confía en lo que el gateway le dice a través de cabeceras. Es como si el gateway le pasara una credencial ya verificada.

## SecurityFilterChain

## UserDetailsService

## PasswordEncoder
