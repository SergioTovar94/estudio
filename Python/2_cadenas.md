# Cadenas de Caracteres

Acceder a valores en la cadena.

```
texto = "Python"
texto[0]    # "P"
texto[-1]   # "n"
texto[0:3]  # "Pyt"
```

| Método          | Qué hace                                   | Uso                                                                                  |
| --------------- | ------------------------------------------ | ------------------------------------------------------------------------------------ |
| lower()         | Convierte a minúsculas                     | `cadena.lower()`                                                                     |
| upper()         | Convierte a mayúsculas                     | `cadena.upper()`                                                                     |
| strip()         | Elimina espacios al inicio y final         | `cadena.strip()`                                                                     |
| lstrip()        | Elimina espacios a la izquierda            | `cadena.lstrip()`                                                                    |
| rstrip()        | Elimina espacios a la derecha              | `cadena.rstrip()`                                                                    |
| split(sep)      | Divide la cadena en una lista              | `cadena.split()` separa por espacios y `cadena.split(" ")`separa por solo un espacio |
| join(iterable)  | Une elementos en una cadena                | `cadena.join(["a", "b", "c"])`                                                       |
| replace(a, b)   | Reemplaza texto                            | `cadena.replace("Python","Java")`                                                    |
| find(sub)       | Devuelve índice o -1                       | `cadena.find()`                                                                      |
| startswith(sub) | Verifica inicio                            | `cadena.startswith()`                                                                |
| endswith(sub)   | Verifica final                             | `cadena.endswith()`                                                                  |
| isdigit()       | Verifica si son dígitos                    | `cadena.isdigit()`                                                                   |
| isalpha()       | Verifica si son letras                     | `cadena.isalpha()`                                                                   |
| isalnum()       | Letras o números                           | `cadena.isalnum()`                                                                   |
| count(sub)      | Cuenta ocurrencias                         | `cadena.count()`                                                                     |
| capitalize()    | Primera letra en mayúscula                 | `cadena.capitalize()`                                                                |
| title()         | Primera letra de cada palabra en mayúscula | `cadena.title()`                                                                     |
| Islower()       | Si toda está en minúscula                  | `cadena.Islower()`                                                                   |
| Isupper         | Si toda está en mayúscula                  | `cadena.Isupper()`                                                                   |

## Ejecicios

### Longitud

Escribe código que:

- Guarde una cadena "Hola Mundo"
- Imprima su longitud

```
cadena = "Hola Mundo
print(len(cadena))
```

### Mayúsculas y minúsculas

Dada la cadena:

`texto = "Python es Genial"`

- Todo en mayúsculas
- Todo en minúsculas

```
print(texto.upper())
print(texto.lower())
```

### Eliminar espacios

Dada la cadena:

`texto = "   hola   "`

Imprime la cadena sin espacios al inicio y al final

`print(texto.strip())`

### Contar caracteres

Dada la cadena:

`texto = "banana"`

Imprime cuántas veces aparece la letra "a".

```
print(texto.count("a"))
```

### Reemplazo

Dada la cadena

`texto =  "Me gusta Java"`

Imprime

`texto =  "Me gusta Python"`

````
print(texto.replace("Java", "Python"))
```

````
