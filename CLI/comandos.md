# Conceptos

CLI hace referencia a Command Line Interface, es decir, interfaz de línea de comandos. Un programa que recibe texto como entrada, lo interpreta y ejecuta algo.

Es una forma de interactuar con un programa o con el sistema operativo escribiendo comandos en texto, en lugar de usar botones o menús gráficos.

**Ejemplo sencillo**

En lugar de:

- Abrir el explorador
- Hacer clic en una carpeta
- Arrastrar un archivo

En un CLI escribirías algo como:

```bash
cd documentos
mv archivo.txt respaldo/
```

## Donde existe un CLI

- En la terminal Linux o Mac.
- En CMD o PowerShell
- Herramientas como
- - git
- - python
- - docker
- - django-admin
- - npm

Siempre hay tres argumentos partes:

- Comando
- Argumentos
- Opciones/flags

Ejemplo

```bash
python manage.py runserver 8000 --settings=prod
```

- python: comando principal
- manage.py: script
- runserver: argumento
- 8000: argumento
- --settings: flag

## Uso de la terminal

```bash
pwd        # dónde estoy
ls         # qué hay aquí
cd carpeta # moverme
mkdir      # crear carpeta
rm         # borrar
cp         # copiar
mv         # mover
```

### Rutas

Se pueden usar

- rutas relativas y absolutas
- . (carpeta actual)
- .. (carpeta anterior)

## Opciones

- -m: utilizado en los commits, permite luego de él escribir un mensaje entre comillas. Sin él, se abriría un editor para que se escriba el mensaje.
- -u: utilizado en los push, crea un vínculo entre la rama local e indica cuál es la rama remota a la que debe apuntar. Solo es necesario usarlo la primer vez, apartir de ello ya con solo `git push` funciona.
- -M: utilizado en branch, se utiliza para forzar el renombrado de una rama, incluso si ya hay otra con este nombre.

```

```
