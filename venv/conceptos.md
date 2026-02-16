# Venv

Es el entorno virtual aislado de Python donde:

- Tiene su propia versión de librerías.
- No afecta el Python global del sistema.
- No se mezcla con otros proyectos.

No es un contenedor. No asila

- Sistema operativo.
- Variables del sistema.
- Archivos del proyecto.

Solo aísla paquetes de Python. Es un aislamiento ligero.

- venv es un módulo oficial que viene incluido en Python (desde Python 3.3)
- Parte de la librería estándar

## Creación del entorno virtual

```python
python -m venv venv
```

- -m: orienta a que se ejecute el módulo como un script. Equivale a: busca este módulo y ejecutalo.
- Se repite venv porque el primero hace referencia al módulo que se va a ejecutar y el segundo indica la carpeta que se va a crear.

Python crea:

```
mi_proyecto/
│
├── venv/
│   ├── Scripts/ o bin/
│   ├── Lib/
│   └── pyvenv.cfg
```

Activar entorno virtual

```Python
venv\Scripts\activate
```
