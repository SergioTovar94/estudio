# Variables especiales relacionadas con módulos

Cuando ejecutas un archivo, Python crea automáticamente algunas variables internas:

```python
__name__
```

Esta es la más famosa.

```python
print(__name__)
```

Si ejecutas el archivo directamente:

```python
python mi_script.py
```

`__name__` vale:

```python
"__main__"
```

Pero si ese archivo es importado desde otro:

```python
import mi_script
```

Entonces `__name__` vale:

"mi_script"

Por eso existe este patrón clásico:

```python
if __name__ == "__main__":
    main()
```

Existen otras como:

```python
__file__
```

Contiene la ruta del archivo actual que se está ejecutando:

```python
print(__file__)  # /home/user/proyecto/mi_script.py
```

```python
__package__
```

Indica el nombre del paquete (para módulos dentro de un paquete):

```python
print(__package__)  # "mi_paquete.submodulo" o None si no está en un paquete
```

```python
__loader__
```

Contiene información sobre cómo fue cargado el módulo:

```python
print(__loader__)  # <class '_frozen_importlib.SourceFileLoader'>
```

También existen:

```python
__cached__
```

Ruta del archivo compilado `.pyc`:

```python
print(__cached__)  # __pycache__/mi_script.cpython-39.pyc
```

```python
__spec__
```

Información completa sobre la especificación del módulo:

```python
print(__spec__)  # ModuleSpec(...)
```

# Variables especiales en objetos y clases

Los objetos y clases en Python tienen atributos especiales marcados con doble guion bajo. Veamos los más importantes:

## `__class__`

Indica la clase a la que pertenece un objeto.

```python
x = "hola"
print(x.__class__)
```

Resultado:

```python
<class 'str'>
```

## `__dict__`

Muestra los atributos internos del objeto en forma de diccionario.

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

p = Persona("Sergio")
print(p.__dict__)
```

Resultado:

```python
{'nombre': 'Sergio'}
```

## Métodos especiales (los famosos “dunder methods”)

Dunder = Double UNDERscore.

Son los que hacen que Python funcione como funciona.

Ejemplos:

```python
__init__
```

Constructor de una clase.

```python
__str__
```

Define qué se imprime cuando haces print(obj).

```python
__len__
```

Permite usar len(obj).

```python
__add__
```

Define qué pasa cuando haces obj1 + obj2.

```python
__truediv__
```

Define qué pasa cuando haces obj1 / obj2.

👆 Aquí está el secreto de Path / "data".

El operador / funciona porque la clase Path implementa:

```python
__truediv__()
```

Eso es lo que llamamos sobrecarga de operadores.
