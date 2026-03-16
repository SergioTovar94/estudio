# Tupla

Igual que una lista, pero inmutable.


```
tupla = ("x", "y", "z")

tupla[0]    # "x"
tupla[-1]   # "z"
```

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `count()` | Cuenta cuántas veces aparece un elemento | `tupla.count("x")` → `1` |
| `index()` | Retorna el índice del primer elemento coincidente | `tupla.index("y")` → `1` |
| `len()` | Retorna la cantidad total de elementos | `len(tupla)` → `3` |
| `in` | Verifica si un elemento existe en la tupla | `"x" in tupla` → `True` |

### Creación y acceso (base)

Dada la tupla:

`persona = ("Juan", 30, "Colombia")`

Imprimir nombre y edad

```
print(persona[0], persona[1])
```

### Desempaquetado (clave en Python)

Dada:

`punto = (3, 4)`

```
x = 3
y = 4
```
Solución

x,y=punto
print(x,y)

### Tuplas dentro de listas

Dada:

```
datos = [
    ("gato", 2),
    ("perro", 5),
    ("ave", 1)
]
```

Crea una lista con solo los nombres cuya cantidad sea mayor que 1

```
print([nombre for nombre, cantidad in datos if cantidad > 1])
```

### Tuplas como claves

Tuplas como claves (importante)

`puntos = [(1, 2), (3, 4), (1, 2), (5, 6)]`

Crea una estructura que permita:

- Eliminar duplicados
- Mantener cada punto como una entidad inmutable
```
puntos = [(1, 2), (3, 4), (1, 2), (5, 6)]
print(set(puntos))
```


### Ordenar por múltiples criterios

Dada:
```
datos = [
    ("Juan", 30, 1.75),
    ("Ana", 25, 1.65),
    ("Luis", 30, 1.80)
]
```

👉 Ordena los datos:

- Por edad (ascendente)
- Si la edad es igual, por altura (descendente)

Solución
```
datos = [
    ("Juan", 30, 1.75),
    ("Ana", 25, 1.65),
    ("Luis", 30, 1.80)
]
ordenados = sorted(datos, key=lambda tupla: (tupla[1], -tupla[2]))
print(ordenados)
```

### Retornos múltiples

Crea una función que reciba una lista de números y devuelva:
- El mínimo
- El máximo
- El promedio

```
def analizar(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return min(lista), max(lista), sum(lista)/len(lista)
print(analizar([1, 2, 3, 4]))

```

