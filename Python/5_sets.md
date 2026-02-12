# Set

No tiene orden ni índices.

`conjunto = {"a", "b", "c"}`

🚫 Esto NO funciona:

`conjunto = {"a", "b", "c"}`

✅ Formas correctas:

```
for elemento in conjunto:
    print(elemento)
```

Convertir a lista (si necesitas acceder por índice):

```
lista_set = list(conjunto)
lista_set[0]
```

Verificar existencia:

`"a" in conjunto   # True o False`

| Función | Descripción | Ejemplo |
|---------|-------------|---------|
| `add()` | Añade un elemento al conjunto | `conjunto.add("d")` |
| `remove()` | Elimina un elemento (error si no existe) | `conjunto.remove("a")` |
| `discard()` | Elimina un elemento (sin error si no existe) | `conjunto.discard("a")` |
| `pop()` | Elimina y retorna un elemento aleatorio | `conjunto.pop()` |
| `clear()` | Elimina todos los elementos | `conjunto.clear()` |
| `union()` | Combina dos conjuntos | `conjunto.union({"d", "e"})` |
| `intersection()` | Elementos comunes | `conjunto.intersection({"a", "d"})` |
| `difference()` | Elementos que no están en otro | `conjunto.difference({"a"})` |
| `len()` | Cantidad de elementos | `len(conjunto)` |


### Limpieza de duplicados con criterio

Dada una lista con valores repetidos:

`ids = [101, 203, 101, 405, 203, 506, 101]`

Crea un set que contenga solo los IDs únicos

```
ids = [101, 203, 101, 405, 203, 506, 101]
print(set(ids))
```

### Comparación de conjuntos

Dos usuarios visitaron páginas distintas:
```
usuario_a = {"home", "perfil", "productos", "contacto"}
usuario_b = {"home", "login", "productos", "checkout"}
```

Calcula:

- Las páginas que ambos visitaron
- Las páginas que solo visitó A
- Las páginas que visitó al menos uno

```
usuario_a = {"home", "perfil", "productos", "contacto"}
usuario_b = {"home", "login", "productos", "checkout"}

print("Las páginas que ambos visitaron")
print(usuario_a.intersection(usuario_b))
print(usuario_a & usuario_b)

print("\nLas páginas que solo visitó A")
print(usuario_a.difference(usuario_b))
print(usuario_a - usuario_b)

print("\nLas páginas que visitó al menos uno")
print(usuario_a.union(usuario_b))
print(usuario_a | usuario_b)
```

### Detección rápida de duplicados

Dada una lista:
```
numeros = [3, 5, 1, 3, 7, 5, 9]
```

### Consistencia de vocabulario

Dado un corpus tokenizado por documentos:
```
docs = [
    {"python", "ia", "modelo", "datos"},
    {"python", "datos", "aprendizaje"},
    {"datos", "modelo", "prediccion"},
]
```
Imprime el vocabulario común a TODOS los documentos

Solución
```
docs = [
    {"python", "ia", "modelo", "datos"},
    {"python", "datos", "aprendizaje"},
    {"datos", "modelo", "prediccion"},
]
print(set.intersection(*docs))
```

### Detección de anomalías

```
esperados = {"A", "B", "C", "D"}
observados = {"A", "C", "E"}
```

Imprime dos sets:
- Elementos faltantes
- Elementos inesperados

```
esperados = {"A", "B", "C", "D"}
observados = {"A", "C", "E"}
print("Faltantes: ", esperados-observados)
print("Inesperados: ", observados-esperados)
```
### Unicidad global

Dada una lista de listas:
```
lotes = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7],
]
```
- Imprime True solo si ningún número se repite entre lotes
- False si alguno aparece en más de un lote


```
lotes = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7],
]

total_elementos = sum(len(lote) for lote in lotes)
elementos_unicos = len(set.union(*(set(lote) for lote in lotes)))

print(total_elementos == elementos_unicos)
```

