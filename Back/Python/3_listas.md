# Listas

Una lista es una colección ordenada y mutable. Permite duplicados y acceso por índice.

Dada la siguiente lista: 

`lista = ["a", "b", "c"]`

Para acceder a sus elementos

```lista[0]   # "a"
lista[1]   # "b"
```

Índice negativo

`lista[-1]  # "c"`

|Método|Qué hace|Uso|
|------|--------|---|
|append(x)|Agrega elemento al final|`lista.append(5)`|
|extend(iterable)|Agrega múltiples elementos|`lista.extend([1, 2, 3])`|
|insert(i, x)|Inserta en posición|`lista.insert(0, "x")`|
|remove(x)|Elimina por valor|`lista.remove(5)`|
|pop(i)|Elimina y retorna por índice|`lista.pop(0)`|
|clear()|Vacía la lista|`lista.clear()`|
|index(x)|Devuelve índice|`lista.index(5)`|
|count(x)|Cuenta ocurrencias|`lista.count(5)`|
|sort()|Ordena la lista|`lista.sort()`|
|reverse()|Invierte el orden|`lista.reverse()`|
|copy()|Copia superficial|`nueva = lista.copy()`|

### Validación compuesta (nivel ML)

Dada una lista de tokens:

`tokens = ["modelo", "GPT", "aprende", "123", "rapido"]`

Imprime True solo si:

- Todos los elementos son strings
- Al menos uno está en mayúsculas
- Ninguno es numérico puro ("123" debería invalidar)


Solución:

```
tokens = ["modelo", "GPT", "aprende", "123", "rapido"]

print(
    all(isinstance(x, str) for x in tokens)
    and any(x.isupper() for x in tokens)
    and not any(x.isdigit() for x in tokens)
)
```


### Transformación con reglas (pipeline real)

`numeros = [3, -1, 4, -2, 0, 5]`

Crea una nueva lista que:

- Elimine los negativos
- Eleve al cuadrado los positivos
- Ignore el cero

```
numeros = [3, -1, 4, -2, 0, 5]
print([x*x for x in numeros if x>0])
```


### Análisis estructural (clave en ML)

```
datos = [
    {"valor": 10, "valido": True},
    {"valor": 5, "valido": False},
    {"valor": 8, "valido": True},
]
```

Solución

```
print(sum(
    x.get("valor")
    for x in datos
    if x.get("valor") > 6 and x.get("valido") == True
))
```

### Ranking con criterio

Dada una lista de puntajes

`scores = [88, 92, 70, 100, 85]`

Crea una nueva lista con los 3 puntajes más altos, ordenados de mayor a menor.

Resultado esperado

`[100, 92, 88]`

```
scores = [88, 92, 70, 100, 85]
top3 = sorted(scores, reverse=True)[:3]
print(top3)
```

### Limpieza + estructura (NLP real)

Dada una lista de frases:

```
frases = [
    "  Python es PODEROSO  ",
    "python  es   rapido",
    "  PYTHON es popular "
]
```

Crea una nueva lista que:

- Quite espacios extra
- Pase todo a minúsculas
- Reemplace múltiples espacios por uno solo

```
nueva = [" ".join(x.lower().split()) for x in frases]
print(nueva)
```

### Ventana deslizante (nivel ML)

Dada:

`numeros = [10, 20, 30, 40, 50]`

Genera una lista de pares consecutivos:

```
numeros = [10, 20, 30, 40, 50]
pares = list(zip(numeros[:-1], numeros[1:]))
print(pares)
```

Alternativa solo con comprensión

```
numeros = [10, 20, 30, 40, 50]
[(numeros[i], numeros[i+1]) for i in range(len(numeros)-1)]
print(pares)
```