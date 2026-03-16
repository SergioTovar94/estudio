# Django

Entorno de desarrollo web basado en python. Es la primer opción para trabajo en equipos. Django fue desarrollado donde las aplicaciones se creaban con múltiples páginas html Actualmente necesitan mucha interacción y que el cambio sea rápido. Para eso entonces Django ya no entrega templates o no se usa tanto, sino que entrega archivos Json y el front se encarga de mostrarlos.

Se dice que es un framework web completo en tanto que no es solo una librería sino que es un ecosistema integrado que tiene:

## Capa de Base de Datos ORM

Con django.db.models puedes:

- Definir tablas con clases
- Hacer consultas sin escribir SQL
- Manejar migraciones
- Crear relaciones entre tablas

Eso ya reemplaza herramientas como SQLAlchemy.

## Capa de routing (URLs)

Con django.urls puedes:

- Definir rutas
- Capturar parámetros
- Modularizar apps

No necesitas otro router

## Capa de lógica (Views)

Puedes manejar

- Request HTTP
- Respuestas
- Sesiones
- Headers
- Archivos

## Sistema de Templates

Django trae su propio motor de templates

- Renderizado HTML
- Herencia de Layouts
- Filtros
- Seguridad contra XSS

## Sistema de formularios

Con django.forms

- Validación automática
- Limpieza de datos
- Generación de HTML
- Integración de modelos

## Autenticación y autorización

Con django.contrib.auth

- Usuarios
- Permisos
- Grupos
- Login/logout
- Decoradores de protección

## Panel administrativo

Con django.contrib.admin

- CRUD automático
- Filtros
- Búsquedas
- Permisos

## Seguridad incorporada

- CRSF
- XSS
- SQL Injection
- Clickjacking

## Sistema de migraciones

Control de versiones para bases de datos
