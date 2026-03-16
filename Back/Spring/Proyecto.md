# PASO 1 — Abrir la carpeta donde estará el proyecto

Abre VS Cod y crea la carpeta del proyecto.

# PASO 2 — Abrir el comando de Spring Initializr

Ahora presiona:

Ctrl + Shift + P - Se abrirá la Command Palette. Escribe:

Spring Initializr

Selecciona: Spring Initializr: Create a Maven Project

# PASO 3 — Elegir versión de Spring Boot

VS Code te mostrará varias versiones. Elige la más reciente estable (algo como): 3.3.x

Spring Boot 3 funciona perfecto con Java moderno.

# PASO 4 — Elegir lenguaje

Selecciona: Java 21

# PASO 5 — Group (organización)

Esto representa el dominio del proyecto. Puedes usar: com.sergio o com.polizas

# PASO 6 — Artifact (nombre del proyecto)

Es el nombre del servicio.

Por ejemplo: polizas-api

Esto creará una carpeta: polizas-api

# PASO 7 — Packaging

Selecciona: Jar

Esto permite que la aplicación se ejecute como: java -jar

# PASO 8 — Versión de Java

Selecciona: 21. Aunque tengas Java 25, Spring Boot recomienda 21. No te preocupes, funcionará igual.

# PASO 9 — Elegir dependencias

Aquí debes agregar: Obligatorias

Busca y selecciona:

| Dependencia         | Qué aporta al proyecto                                                                                                         | Para qué se usa en la API de seguros                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| **Spring Web**      | Permite crear APIs REST y manejar peticiones HTTP. Incluye servidor Tomcat embebido y conversión automática de JSON.           | Exponer endpoints como `GET /polizas`, `POST /polizas`, `GET /polizas/{id}` para consultar o crear pólizas.        |
| **Spring Data JPA** | Facilita el acceso a bases de datos usando objetos Java. Implementa ORM para mapear entidades a tablas sin escribir mucho SQL. | Guardar, consultar y actualizar pólizas y riesgos en la base de datos usando repositorios como `PolizaRepository`. |
| **H2 Database**     | Base de datos en memoria que se crea automáticamente al iniciar la aplicación. No requiere instalación.                        | Permite probar la API rápidamente sin instalar MySQL o PostgreSQL, ideal para pruebas técnicas o desarrollo local. |
| **Lombok**          | Reduce código repetitivo en Java generando automáticamente getters, setters, constructores y métodos comunes.                  | Simplifica las entidades como `Poliza` o `Riesgo`, evitando escribir manualmente métodos repetitivos.              |

Puedes escribir el nombre en el buscador.

# PASO 10 — Seleccionar carpeta de destino

VS Code preguntará dónde guardar el proyecto. Elige la carpeta que abriste antes:

dev/spring

VS Code creará automáticamente: polizas-api

Verás que descarga dependencias y crea la estructura.

📁 Así quedará tu proyecto
polizas-api

```
├─ src
│ ├─ main
│ │ ├─ java
│ │ │ └─ com/sergio/polizasapi
│ │ │ └─ PolizasApiApplication.java
│ │ └─ resources
│ │ └─ application.properties
│ └─ test
├─ pom.xml
├─ mvnw
└─ mvnw.cmd
```

# PASO 11 — Ejecutar el proyecto

Abre el archivo: PolizasApiApplication.java

Encima de la clase aparecerá: Run | Debug

Haz clic en Run.

📊 Si todo funciona verás en la terminal

Algo como:

Started PolizasApiApplication
Tomcat started on port 8080

Ese Tomcat es el servidor embebido de Spring Boot.
