# Docker

Docker es una herramienta que permite empaquetar una aplicación con todo lo que necesita para ejecutarse y correrla en cualquier lugar de forma consistente.

El paquete se llama **imagen** y cuando se ejecuta se llama **contenedor**.

# Imagen

Un paquete que contiene tu aplicación y todo lo necesario para ejecutarla.

Incluye:

- Sistema operativo
- Runtime (Java, Python, Node, etc.)
- Librerías
- Código
- Configuración

| Lenguaje   | Runtime                    |
| ---------- | -------------------------- |
| Python     | Python                     |
| Java       | JVM (Java Virtual Machine) |
| JavaScript | Node.js                    |
| C#         | .NET Runtime               |
| Go         | Go Runtime                 |

# Contenedor

Es una instancia de ejecución de la imagen.

# Dockerfile

Archivo que define como construir una imagen.

```Dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Eso significa:

- Usa Python
- Crea carpeta /app
- Copia dependencias
- Instala dependencias
- Copia el código
- Ejecuta la aplicación

# Docker hub

Es un repositorio de imágenes. Como Gihub pero para imágenes.

Ejemplos de imágenes disponibles:

- postgres
- mysql
- nginx
- redis
- node
- python
- openjdk

**Ejemplo**

```Bash
docker pull postgres
```

Descarga la imagen de postgres

# Docker vs Máquina Virtual

| Característica    | Docker          | Máquina Virtual |
| ----------------- | --------------- | --------------- |
| Arranque          | segundos        | minutos         |
| Peso              | ligero          | pesado          |
| Uso de RAM        | bajo            | alto            |
| Sistema operativo | comparte kernel | propio kernel   |
| Velocidad         | rápida          | más lenta       |

## ¿Para qué sirve Docker?

1. Ejecutar aplicaciones

Por ejemplo:

Spring Boot
Django
React
PostgreSQL

2. Crear entornos reproducibles

Todos los desarrolladores usan:

misma versión
mismas librerías
misma configuración

3. Microservicios

Cada servicio:

su contenedor
su base de datos
su configuración

4. Despliegue en la nube

Por ejemplo:

AWS
Azure
GCP

5. CI/CD

Automatización:

Build
Test
Deploy

# Volumen

# Red

# Docker Compose
