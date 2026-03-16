# Funciones built-in de Python (las globales)

## Generales

| Función  | Descripción                                                                               | Ejemplo                        |
| -------- | ----------------------------------------------------------------------------------------- | ------------------------------ |
| `len()`  | Retorna la longitud (número de elementos) de un objeto como listas, tuplas, strings, etc. | `len([1, 2, 3])` → 3           |
| `type()` | Retorna el tipo de dato de un objeto (int, str, list, dict, etc.).                        | `type("hola")` → <class 'str'> |
| `id()`   | Retorna la identidad única (dirección de memoria) de un objeto.                           | `id([1, 2])` → 140234567890    |
| `help()` | Muestra documentación interactiva sobre un objeto, módulo o función.                      | `help(len)`                    |
| `dir()`  | Retorna una lista de atributos y métodos válidos de un objeto.                            | `dir("hola")`                  |

## Conversión de tipos

| Función   | Descripción                 | Ejemplo                        |
| --------- | --------------------------- | ------------------------------ |
| `int()`   | Convierte a entero          | `int("42")` → 42               |
| `float()` | Convierte a decimal         | `float("3.14")` → 3.14         |
| `str()`   | Convierte a cadena de texto | `str(42)` → "42"               |
| `list()`  | Convierte a lista           | `list((1, 2, 3))` → [1, 2, 3]  |
| `tuple()` | Convierte a tupla           | `tuple([1, 2, 3])` → (1, 2, 3) |
| `set()`   | Convierte a conjunto        | `set([1, 1, 2])` → {1, 2}      |
| `dict()`  | Convierte a diccionario     | `dict([('a', 1)])` → {'a': 1}  |
| `bool()`  | Convierte a booleano        | `bool(1)` → True               |

## Iteración/Colecciones

| Función       | Descripción                                                                 | Ejemplo                                      |
| ------------- | --------------------------------------------------------------------------- | -------------------------------------------- |
| `range()`     | Genera una secuencia de números enteros, útil para bucles for.              | `range(5)` → 0, 1, 2, 3, 4                   |
| `enumerate()` | Retorna pares de índice y valor al iterar sobre una colección.              | `enumerate(['a', 'b'])` → (0, 'a'), (1, 'b') |
| `zip()`       | Combina múltiples iterables en tuplas de elementos correspondientes.        | `zip([1,2], ['a','b'])` → (1, 'a'), (2, 'b') |
| `sorted()`    | Retorna una lista ordenada de los elementos de un iterable.                 | `sorted([3,1,2])` → [1, 2, 3]                |
| `reversed()`  | Retorna un iterador que recorre una secuencia en orden inverso.             | `reversed([1,2,3])` → 3, 2, 1                |
| `iter()`      | Retorna un objeto iterador a partir de un iterable.                         | `iter([1,2,3])` → objeto iterador            |
| `next()`      | Retorna el siguiente elemento de un iterador.                               | `next(iter([1,2]))` → 1                      |
| `slice()`     | Retorna un objeto que especifica cómo extraer una porción de una secuencia. | `[0,1,2,3][slice(1,3)]` → [1, 2]             |

## Matemáticas/Lógica

| Función    | Descripción                                                          | Ejemplo                        |
| ---------- | -------------------------------------------------------------------- | ------------------------------ |
| `all()`    | Retorna True si todos los elementos de un iterable son verdaderos.   | `all([True, True, 1])` → True  |
| `any()`    | Retorna True si al menos un elemento de un iterable es verdadero.    | `any([False, True, 0])` → True |
| `sum()`    | Retorna la suma de todos los elementos de un iterable.               | `sum([1, 2, 3])` → 6           |
| `max()`    | Retorna el elemento máximo de un iterable o entre varios argumentos. | `max([1, 5, 3])` → 5           |
| `min()`    | Retorna el elemento mínimo de un iterable o entre varios argumentos. | `min([1, 5, 3])` → 1           |
| `abs()`    | Retorna el valor absoluto de un número.                              | `abs(-5)` → 5                  |
| `pow()`    | Retorna la potencia de un número elevado a otro.                     | `pow(2, 3)` → 8                |
| `divmod()` | Retorna una tupla con el cociente y el residuo de una división.      | `divmod(17, 5)` → (3, 2)       |
| `round()`  | Redondea un número a una cantidad especificada de decimales.         | `round(3.14159, 2)` → 3.14     |

## Funcional

| Función    | Descripción                                              | Ejemplo                                    |
| ---------- | -------------------------------------------------------- | ------------------------------------------ |
| `map()`    | Aplica una función a todos los elementos de un iterable. | `map(str, [1, 2, 3])` → ['1', '2', '3']    |
| `filter()` | Filtra elementos que cumplen una condición.              | `filter(lambda x: x > 2, [1, 2, 3])` → [3] |
| `reduce()` | Reduce un iterable a un único valor (en functools).      | `reduce(lambda x, y: x+y, [1, 2, 3])` → 6  |

# Operadores

## Operadores aritméticos

| Operador | Descripción      |
| -------- | ---------------- |
| `+`      | Suma             |
| `-`      | Resta            |
| `*`      | Multiplicación   |
| `/`      | División         |
| `//`     | División entera  |
| `%`      | Módulo (residuo) |
| `**`     | Potencia         |
| `==`     | Igualdad         |

## Operadores de comparación

| Operador | Descripción       |
| -------- | ----------------- |
| `!=`     | Desigualdad       |
| `<`      | Menor que         |
| `>`      | Mayor que         |
| `<=`     | Menor o igual que |
| `>=`     | Mayor o igual que |

## Operadores lógicos

| Operador | Descripción                                      |
| -------- | ------------------------------------------------ |
| `and`    | Verdadero si ambas condiciones son verdaderas    |
| `or`     | Verdadero si al menos una condición es verdadera |
| `not`    | Invierte el valor booleano                       |

## Operadores de pertenencia

| Operador | Descripción                                      |
| -------- | ------------------------------------------------ |
| `in`     | Verifica si un elemento está en una colección    |
| `not in` | Verifica si un elemento no está en una colección |

## Operadores de identidad

| Operador | Descripción                                           |
| -------- | ----------------------------------------------------- |
| `is`     | Verifica si dos variables refieren al mismo objeto    |
| `is not` | Verifica si dos variables no refieren al mismo objeto |

## Operadores bit a bit

| Operador | Descripción                   |
| -------- | ----------------------------- |
| `&`      | AND bit a bit                 |
| `\|`     | OR bit a bit                  |
| `^`      | XOR bit a bit                 |
| `~`      | NOT bit a bit                 |
| `<<`     | Desplazamiento a la izquierda |
| `>>`     | Desplazamiento a la derecha   |

## Operadores de asignación

| Operador | Descripción                                                           |
| -------- | --------------------------------------------------------------------- |
| `=`      | Asignación simple                                                     |
| `+=`     | Suma y asigna (crea nuevo objeto si es inmutable)                     |
| `-=`     | Resta y asigna (crea nuevo objeto si es inmutable)                    |
| `*=`     | Multiplica y asigna (crea nuevo objeto si es inmutable)               |
| `/=`     | Divide y asigna (crea nuevo objeto si es inmutable)                   |
| `//=`    | División entera y asigna (crea nuevo objeto si es inmutable)          |
| `%=`     | Módulo y asigna (crea nuevo objeto si es inmutable)                   |
| `**=`    | Potencia y asigna (crea nuevo objeto si es inmutable)                 |
| `&=`     | AND bit a bit y asigna (crea nuevo objeto si es inmutable)            |
| `\|=`    | OR bit a bit y asigna (crea nuevo objeto si es inmutable)             |
| `^=`     | XOR bit a bit y asigna (crea nuevo objeto si es inmutable)            |
| `<<=`    | Desplazamiento izquierda y asigna (crea nuevo objeto si es inmutable) |
| `>>=`    | Desplazamiento derecha y asigna (crea nuevo objeto si es inmutable)   |

## Tipos de datos

| Criterio        | Lista              | Tupla       | Set      | Diccionario              |
| --------------- | ------------------ | ----------- | -------- | ------------------------ |
| Modificable     | Sí                 | No          | Sí       | Sí                       |
| Repetidos       | Sí                 | Sí          | No       | Claves: No / Valores: Sí |
| Clave–valor     | No                 | No          | No       | Sí                       |
| Índice          | Sí                 | Sí          | No       | No                       |
| Mantiene orden  | Sí                 | Sí          | No       | Sí (Python 3.7+)         |
| Búsqueda rápida | No                 | No          | Sí       | Sí                       |
| Uso típico      | Colección dinámica | Datos fijos | Unicidad | Mapeo datos              |
| Sintaxis        | []                 | ()          | {}       | {k: v}                   |

# Raise

Sirve para lanzar de forma intencional excepciones en Python

```python
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad < 18:
        raise ValueError("Debes tener al menos 18 años")
    return "Acceso permitido"

try:
    print(validar_edad(-5))
except ValueError as e:
    print(f"Error: {e}")  # Error: La edad no puede ser negativa

try:
    print(validar_edad(15))
except ValueError as e:
    print(f"Error: {e}")  # Error: Debes tener al menos 18 años

print(validar_edad(25))  # Acceso permitido
```
