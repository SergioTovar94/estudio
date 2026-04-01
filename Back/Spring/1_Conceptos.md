# Spring Framework

Framework de desarrollo para Java que facilita crear aplicaciones, especialmente aplicaciones web, APIs y microservicios.
Sin Spring, en Java tienes que programar muchas cosas desde cero (configuración, manejo de objetos, conexiones, seguridad, etc.).

| Función                   | Qué hace                               |
| ------------------------- | -------------------------------------- |
| Inyección de dependencias | Administra los objetos automáticamente |
| Desarrollo web            | Crear APIs REST y aplicaciones web     |
| Acceso a bases de datos   | Conectar y manejar datos fácilmente    |
| Seguridad                 | Autenticación y autorización           |
| Transacciones             | Control seguro de operaciones en BD    |

## Ecosistema de Spring

El framework tiene varios módulos importantes:

Spring Boot → la forma moderna y rápida de crear aplicaciones Spring

Spring MVC → para aplicaciones web

Spring Security → autenticación y permisos

Spring JPA → acceso a bases de datos

Spring Cloud → microservicios y arquitectura distribuida

## Flujo completo en Spring

```
Cliente
   ↓
Filtro de seguridad (Spring Security)
   ↓
Controller (Spring MVC)
   ↓
Validación
   ↓
Service (lógica de negocio)
   ↓
Repository (Spring Data JPA)
   ↓
Base de datos
   ↓
Respuesta
```

## Qué es Spring MVC

Es un módulo dentro de Spring para crear aplicaciones web.

MVC significa:

| Parte      | Qué hace              |
| ---------- | --------------------- |
| Model      | Maneja los datos      |
| View       | Lo que ve el usuario  |
| Controller | Recibe las peticiones |
