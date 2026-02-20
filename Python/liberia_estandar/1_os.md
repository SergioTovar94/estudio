# Módulo os

## Propósito

Interactuar con el sistema operativo: manejo de archivos y carpetas, rutas, procesos, variables de entorno, y control de directorios.

## Funciones más usadas

os.getcwd() → devuelve el directorio de trabajo actual.

os.listdir(path) → lista los archivos y carpetas de path.

os.mkdir(path) → crea un directorio nuevo.

os.makedirs(path, exist_ok=True) → crea directorios anidados.

os.remove(path) → elimina un archivo.

os.rename(src, dst) → renombra un archivo o carpeta.

os.path.exists(path) → verifica si un archivo o carpeta existe.

os.environ → acceder a variables de entorno.

## Constantes más usadas

os.sep → separador de rutas (/ en Linux/Mac, \ en Windows).

os.name → tipo de sistema operativo ('nt' para Windows, 'posix' para Linux/Mac).

os.linesep → salto de línea del sistema operativo.

os.pathsep → separador de rutas múltiples (: en Linux/Mac, ; en Windows).

## Clases más usadas

os.DirEntry → representa una entrada en un directorio (usada con os.scandir()).

os.stat_result → resultado de os.stat(), contiene info de archivos.

## Tipos de datos o estructuras importantes

Rutas y nombres de archivos como strings (str).

Listas de archivos: list (os.listdir()).

Objetos especiales como DirEntry o stat_result.

## Errores comunes

FileNotFoundError → archivo o directorio no existe.

PermissionError → no tienes permisos para leer, escribir o eliminar.

OSError → errores generales del sistema operativo (p. ej., disco lleno, ruta inválida).

## Interacción con otros módulos
