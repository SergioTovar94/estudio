# Spring Boot

Hace referencia al nivel de automatización de la configuración. Spring Boot es una herramienta que simplifica muchísimo Spring. Un framework que simplifica la creación de aplicaciones Spring mediante configuración automática, servidor embebido y gestión de dependencias.

Antes de Spring Boot, crear una app Spring implicaba:

- Mucha configuración XML
- Configurar servidor
- Configurar dependencias
- Configurar beans manualmente
- Podía tomar horas o días iniciar un proyecto.

## Las 3 características más importantes de Spring Boot

### 1. Configuración automática (Auto Configuration)

Spring detecta lo que necesitas y lo configura solo.

Ejemplo:

Si agregas: spring-boot-starter-web, Spring automáticamente configura:

- servidor web
- controlador REST
- JSON
- rutas HTTP

Sin que tú escribas configuración manual.

### 2. Servidor embebido

No necesitas instalar un servidor externo.

Spring Boot incluye:

- Tomcat
- Jetty
- Undertow

La aplicación se ejecuta sola.

### 3. Starter dependencies

Son paquetes que traen todo lo necesario.

Ejemplo:

spring-boot-starter-web

Incluye:

- Spring MVC
- Jackson
- servidor web
- validación

## Qué hace internamente Spring Boot al iniciar

- Escanea clases
- Detecta anotaciones
- Crea objetos (beans)
- Inyecta dependencias
- Configura servidor
- Inicia aplicación

## Estrutura de un proyecto Spring Boot

```
project

src
 └── main
      └── java
           └── controller
           └── service
           └── repository
           └── model

resources
 └── application.properties
```

## Aplicaión Properties

Aquí se configura la aplicación.

```
server.port=8080
spring.datasource.url=jdbc:postgresql://localhost:5432/db
spring.datasource.username=user
spring.datasource.password=password
```

Si no se configuran algunos valores, se asumen por defecto.
