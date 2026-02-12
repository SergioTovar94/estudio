# Desempaquetado

## Desempaquetado en tupla

El número de variables tiene que ser igual al de elementos. En caso contrario se producirá un error.

```
datos = ('Elemento 1', 'Elemento 2', 'Elemento 3')

(var1, var2, var3) = datos

print(var1)
print(var2)
print(var3)
```

## Uso de *

Sirve para desempaquetar todo o una parte en caso que se desconozca el número de elementos dentro de la tupla.
Cuando aparece * significa “Toma este iterable y pásalo elemento por elemento"

```
(var1, *var2) = datos

print(var1)
print(var2)
```

# Variable descartable o variable comodin (dummy variable)

- No es una palabra reservada especial
- Es una convención, no una regla del lenguaje.
- Sí queda guardado en memoria, solo expresa que el valor no es importante

# Slicing

> En **Python**, slicing es una forma simple y muy poderosa de extraer partes (subsecciones) de una secuencia, como:

## Sintaxis básica

`secuencia[inicio : fin : paso]`

inicio → índice donde empieza (incluido)

fin → índice donde termina (NO incluido)

paso → cada cuántos elementos avanzar (opcional)

## Ejemplos con strings

`texto = "Python"`

```texto[0:4]    # 'Pyth'
texto[1:5]    # 'ytho'
texto[:3]     # 'Pyt'
texto[2:]     # 'thon'
```

## Ejemplos con listas

`numeros = [0, 1, 2, 3, 4, 5]`

``` numeros[1:4]      # [1, 2, 3]
numeros[:3]       # [0, 1, 2]
numeros[3:]       # [3, 4, 5]
numeros[::2]      # [0, 2, 4]
```

## Paso y slicing inverso

```numeros[::2]      # toma uno sí, uno no → [0, 2, 4]
numeros[::-1]     # invierte la lista → [5, 4, 3, 2, 1, 0]
```

También con strings:

`"hola"[::-1]      # 'aloh'`
