# Comandos básicos de docker

| Comando             | Qué hace                                           | Ejemplo                  |
| ------------------- | -------------------------------------------------- | ------------------------ |
| docker --version    | Ver la versión de Docker                           | docker --version         |
| docker pull         | Descargar una imagen                               | docker pull postgres     |
| docker images       | Ver imágenes descargadas                           | docker images            |
| docker run          | Crear y ejecutar un contenedor                     | docker run nginx         |
| docker ps           | Ver contenedores en ejecución                      | docker ps                |
| docker ps -a        | Ver todos los contenedores                         | docker ps -a             |
| docker stop         | Detener un contenedor                              | docker stop ID           |
| docker start        | Iniciar un contenedor detenido                     | docker start ID          |
| docker restart      | Reiniciar un contenedor                            | docker restart ID        |
| docker rm           | Eliminar un contenedor                             | docker rm ID             |
| docker rmi          | Eliminar una imagen                                | docker rmi imagen        |
| docker build        | Construir una imagen desde un Dockerfile           | docker build -t mi-app . |
| docker logs         | Ver logs de un contenedor                          | docker logs ID           |
| docker exec         | Ejecutar un comando dentro del contenedor          | docker exec -it ID bash  |
| docker compose up   | Levantar servicios definidos en docker-compose.yml | docker compose up        |
| docker compose down | Detener y eliminar servicios                       | docker compose down      |

##

```bash

```
