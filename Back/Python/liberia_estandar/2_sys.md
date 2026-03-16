## Módulo Sys

Proporciona acceso a funciones y variables relacionadas con el intérprete de Python y el entorno de ejecución. Se usa para interactuar con argumentos de línea de comando, rutas de búsqueda de módulos, salida estándar, errores y el cierre del programa.

## Funciones más usadas

sys.exit([codigo]) → termina la ejecución del programa.

sys.argv → lista de argumentos de línea de comando pasados al script.

sys.path → lista de rutas donde Python busca módulos.

sys.platform → nombre del sistema operativo ('win32', 'linux', 'darwin').

sys.version → información de la versión de Python.

sys.modules → diccionario de módulos cargados actualmente.

sys.stdin, sys.stdout, sys.stderr → flujos de entrada/salida estándar.

## Constantes más usadas

sys.maxsize → el entero máximo que puede manejar Python en la plataforma.

sys.float_info → información sobre precisión y límites de float.

sys.byteorder → indica el orden de bytes de la plataforma ('little' o 'big').

## Clases más usadas

sys.flags → contiene información de flags del intérprete (por ejemplo, optimizaciones).

sys.exc_info() → devuelve información sobre la excepción actual (tipo, valor y traceback).

## Tipos de datos o estructuras importantes

Strings (str) → información de versión y plataforma.

Listas (list) → sys.argv, sys.path.

Diccionarios (dict) → sys.modules.

Objetos especiales → sys.flags, sys.float_info.

## Errores comunes

SystemExit → generado al usar sys.exit().

AttributeError → si accedes a un atributo inexistente, como sys.foobar.

IndexError → al usar sys.argv[i] si no hay suficientes argumentos.

## Interacción con otros módulos

os → sys.platform y rutas (sys.path) se pueden usar con os para manejo de archivos.

pathlib → se puede usar junto con sys.path para agregar rutas de búsqueda.

subprocess → sys.stdin/stdout/stderr pueden redirigirse a procesos externos.
