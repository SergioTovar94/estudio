# Importando módulos o librerías

## Módulo

Generalmente es un archivo .py (o un archivo compilado en C, como .so o .pyd) que contiene definiciones y declaraciones de Python. Por ejemplo, el módulo math está implementado en C pero se comporta como un módulo.

## Paquete

Es una colección de módulos organizados en una carpeta. Para que Python reconozca una carpeta como paquete, tradicionalmente debe contener un archivo **init**.py (que puede estar vacío o contener código de inicialización). Así, cuando haces import paquete.submodulo, Python sabe dónde buscar.

## Librería

Uuna librería en Python es un concepto más amplio: puede ser un único módulo (un solo archivo .py), un paquete (una carpeta con varios módulos y init.py), o incluso una colección de varios paquetes y módulos relacionados que se distribuyen juntos.

Para ser más precisos:

Módulo: Archivo .py (o archivo compilado .pyc, o extensión en C) que contiene código Python.

Paquete: Carpeta que contiene un archivo init.py y otros módulos o subpaquetes. Sirve para organizar módulos relacionados.

Librería: Término general que se refiere a una colección de código reutilizable. Puede ser:

Un solo módulo (ej: requests originalmente era un solo archivo, pero ahora es un paquete).

Un solo paquete (ej: numpy es un paquete grande).

Varios paquetes y módulos independientes pero relacionados que se distribuyen juntos (ej: matplotlib incluye varios paquetes como matplotlib.pyplot, matplotlib.axes, etc.).

La librería estándar de Python es un ejemplo de una colección enorme que contiene tanto módulos individuales como paquetes enteros, todos distribuidos juntos con el intérprete.

## Formas de importar en Python

### Importar módulo completo

```Python
import math
print(math.pi)
```

- Uso: cuando necesitas varias funciones/variables del módulo y quieres mantener claro de dónde vienen (namespace explícito).
- Ventaja: evita conflictos de nombres, es muy legible.
- Desventaja: puede ser verboso si usas muchas veces el mismo nombre.

### Importar objetos específicos de un módulo

```Python
from math import pi, sin
print(pi)
print(sin(0))
```

- Uso: cuando solo necesitas unos pocos elementos del módulo y quieres acceder directamente sin el prefijo.
- Ventaja: código más conciso.
- Desventaja: puede causar conflictos si ya tienes una variable con el mismo nombre.

### Importar con alias

```Python
import numpy as np
from pandas import DataFrame as DF
```

### Importar todo con \* (asterisco)

```Python
from math import *
print(pi)
print(sin(0))
```

- Uso: muy desaconsejado, salvo en sesiones interactivas o scripts muy pequeños y personales.
- Problema: contamina el espacio de nombres, puede sobrescribir funciones sin previo aviso y dificulta la lectura (no sabes de dónde viene cada cosa).

Recomendación: evitarlo en código de producción.

### Importaciones relativas (dentro de paquetes)

```Python
# Dentro de un paquete, en un submódulo
from . import modulo_vecino
from ..subpaquete import otro_modulo
```

## Agrupa las importaciones

1. Primero los módulos de la librería estándar
2. Módulos de terceros
3. Módulos locales

Uso: para importar módulos dentro del mismo paquete (organización interna).
Ventaja: facilita la reestructuración del paquete sin cambiar nombres absolutos.

Desventaja: solo funciona dentro de paquetes, no en scripts principales.
