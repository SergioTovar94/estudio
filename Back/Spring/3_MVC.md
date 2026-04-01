# ¿Qué es Spring MVC?

Spring MVC es el módulo de Spring que maneja las solicitudes HTTP y construye APIs o aplicaciones web.

- Model
- View
- Controller

Recibe una solicitud HTTP y decide:

- qué controlador ejecutar
- qué lógica correr
- qué respuesta devolver

Automáticamente

- mapea URLs
- convierte JSON a objetos
- valida datos
- maneja errores
- genera respuestas

## Controller

## Service

## Repository

## Model

# Anotaciones

| Anotación       | Función                 |
| --------------- | ----------------------- |
| @RestController | Define controlador REST |
| @RequestMapping | Define ruta base        |
| @GetMapping     | Maneja GET              |
| @PostMapping    | Maneja POST             |
| @PathVariable   | Lee parámetro de URL    |
| @RequestBody    | Lee JSON                |
