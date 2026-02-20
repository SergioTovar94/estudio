# Pathlib

Proporcionar una forma orientada a objetos de trabajar con rutas de archivos y directorios, reemplazando en muchos casos a os.path. Permite crear, inspeccionar y manipular rutas de manera más legible y segura.

```python
import os
os.path.join("data", "raw", "archivo.csv")
```

Y ahora se hace así:

```python
from pathlib import Path
Path("data") / "raw" / "archivo.csv"
```

## Funciones más usadas

Path.exists() → verifica si la ruta existe.

Path.is_file() → comprueba si es un archivo.

Path.is_dir() → comprueba si es un directorio.

Path.mkdir(parents=True, exist_ok=True) → crear directorios, incluso anidados.

Path.joinpath(\*otros) → unir rutas de manera segura.

Path.rename(destino) → renombrar archivo o directorio.

Path.unlink() → eliminar archivo.

Path.glob(pattern) → buscar archivos por patrón dentro de un directorio.

## Constantes más usadas

Path.cwd() → devuelve el directorio actual de trabajo.

Path.home() → devuelve el directorio del usuario.

## Clases más usadas

Path → la clase principal para rutas de archivos y directorios.

PurePath, PurePosixPath, PureWindowsPath → clases abstractas para manipular rutas sin interactuar con el sistema de archivos (útiles para compatibilidad entre OS).

## Tipos de datos o estructuras importantes

Path → objetos que representan rutas.

str → se puede convertir con str(Path).

Iterables de Path → por ejemplo al usar Path.glob() devuelve un generador de objetos Path.

### Unir rutas

```Python
nueva = Path("data") / "silver" / "ventas.parquet"
```

El operador / une partes de la ruta.
✔ Es multiplataforma
✔ Evita errores con \ y /

### Obtener partes de ruta

```Python
ruta.name        # ventas.parquet
ruta.stem        # ventas
ruta.suffix      # .parquet
ruta.parent      # data/silver
ruta.parts       # ('data', 'silver', 'ventas.parquet')
```

Es un módulo de Python que sirve para manejar rutas de archivos y directorios de manera orientada a objetos, más moderna que usar os.path.

## Creación de rutas

from pathlib import Path

`p = Path("mi_carpeta/archivo.txt")`

Path() → crea un objeto de ruta.

## Propiedades de la ruta

p.exists() → devuelve True si el archivo o carpeta existe.

p.is_file() → True si es un archivo.

p.is_dir() → True si es un directorio.

p.name → nombre del archivo (archivo.txt).

p.stem → nombre sin extensión (archivo).

p.suffix → extensión del archivo (.txt).

p.parent → directorio padre (mi_carpeta).

p.parts → tupla con todos los componentes de la ruta (('mi_carpeta', 'archivo.txt')).

## Navegación y creación

p.joinpath("subcarpeta/otro.txt") → crea una ruta dentro de la ruta actual.

p.mkdir(parents=True, exist_ok=True) → crea directorios; parents=True crea padres si no existen.

p.rename("nuevo_nombre.txt") → renombra el archivo o carpeta.

p.unlink() → elimina el archivo.

p.rmdir() → elimina directorio vacío.

## Lectura y escritura

p.read_text() → lee el contenido de un archivo de texto.

p.write_text("hola") → escribe texto en el archivo.

p.read_bytes() → lee como bytes.

p.write_bytes(b"datos") → escribe bytes.

## Búsqueda y patrones

p.glob("\*.txt") → itera sobre archivos que coinciden con el patrón en ese directorio.

p.rglob("\*.txt") → busca recursivamente en todos los subdirectorios.

Ejemplo:

for archivo in Path("mi_carpeta").glob("\*.txt"):
print(archivo)
Otras utilidades

p.absolute() → ruta absoluta.

p.resolve() → ruta absoluta resolviendo links simbólicos.

p.with_name("nuevo.txt") → cambia el nombre manteniendo la ruta.

p.with_suffix(".md") → cambia la extensión del archivo.
