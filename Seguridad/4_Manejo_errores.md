Hay un manejador global de errores.

# 1. Principios teóricos que aplican al manejo de errores

## Responsabilidad Única (SRP)

Cada @ExceptionHandler maneja una familia de excepciones. Tu handler de validación no debe saber de autenticación.

## Abierto/Cerrado (OCP)

Puedes añadir nuevos manejadores sin modificar los existentes. Simplemente creas un nuevo método con @ExceptionHandler(MiExcepcion.class).

## Segregación de interfaces

No fuerces a los controladores a manejar errores. Usa @RestControllerAdvice para separar la lógica de error de la lógica de negocio.

## DRY (Don't Repeat Yourself)

Centralizas la construcción de respuestas de error. Si cambia el formato de ErrorResponse, tocas un solo lugar.

## Fail Fast

Detecta y lanza excepciones tan pronto como los datos son inválidos. Mejor un 400 temprano que un 500 más tarde.

## Principio de menor asombro

Usa códigos HTTP estándar (400 = error de cliente, 404 = no encontrado, 409 = conflicto, etc.). No inventes códigos.

# Qué hacer y qué no hacer (checklist práctico)

## SÍ debes hacer

Usar @RestControllerAdvice para manejo global.

Definir excepciones propias de negocio (ej. ResourceNotFoundException, BusinessRuleException).

Loggear el error con nivel apropiado (warn para errores de cliente, error para imprevistos).

Devolver siempre una estructura consistente de error (timestamp, código, mensaje, ruta).

Usar @Valid + BindingResult o lanzar MethodArgumentNotValidException.

En entornos de desarrollo, puedes incluir el stack trace en la respuesta, pero no en producción.

Mapear IllegalArgumentException a 400 Bad Request (es un error del cliente).

## No debes hacer..

No exponer detalles internos (stack traces, queries SQL, rutas de archivos) al cliente.

No usar Exception como comodín para lógica de negocio. Captura Exception.class solo como último recurso.

No imprimir ex.printStackTrace() en producción → usa un logger (log.error("mensaje", ex)).

No devolver 500 Internal Server Error para errores que son claramente culpa del cliente (datos faltantes, IDs inválidos).

No lanzar RuntimeException genérica cuando puedes crear una excepción semántica.

## @RestControllerAdvice

Es una anotación de Spring que se usa para manejar errores de forma global en todos los controllers de tu aplicación, sin tener que escribir try-catch en cada endpoint.
