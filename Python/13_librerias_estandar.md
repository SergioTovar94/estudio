# Liberías estandar

Python trae algo llamado Standard Library. No es una o dos librerías. Son cientos de módulos incluidos con Python.

No necesitas hacer pip install para usarlas.

## pathlib

Sirve para trabajar con rutas de archivos de forma elegante y segura.

Antes se hacía así:

```python
import os
os.path.join("data", "raw", "archivo.csv")
```

Y ahora se hace así:

```python
from pathlib import Path
Path("data") / "raw" / "archivo.csv"
```
