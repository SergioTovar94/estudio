# Diccionarios

Un diccionario es una estructura clave → valor, mutable y sin duplicados de clave. Ideal para datos estructurados (JSON, APIs).

Acceso por clave, no por índice.

```
dic = {
    "nombre": "Ana",
    "edad": 30
}

```

Por clave:

`dic["nombre"]   # "Ana"`

Con .get() (más seguro):

```
dic.get("edad")        # 30
dic.get("altura")     # None
dic.get("altura", 0)  # 0
```
Claves, valores e items:

```
dic.keys()    # dict_keys(['nombre', 'edad'])
dic.values()  # dict_values(['Ana', 30])
dic.items()   # dict_items([('nombre', 'Ana'), ('edad', 30)])
```

## Métodos de diccionarios

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `keys()` | Retorna las claves del diccionario | `dic.keys()` → `dict_keys(['nombre', 'edad'])` |
| `values()` | Retorna los valores del diccionario | `dic.values()` → `dict_values(['Ana', 30])` |
| `items()` | Retorna pares clave-valor | `dic.items()` → `dict_items([('nombre', 'Ana'), ('edad', 30)])` |
| `get(clave, default)` | Obtiene valor de forma segura | `dic.get("edad")` → `30` |
| `pop(clave)` | Extrae y elimina una clave | `dic.pop("edad")` → `30` |
| `update(otro_dic)` | Actualiza con otro diccionario | `dic.update({"ciudad": "Madrid"})` |
| `clear()` | Elimina todos los elementos | `dic.clear()` |
| `copy()` | Crea una copia superficial | `dic2 = dic.copy()` |
| `setdefault(clave, valor)` | Obtiene o establece valor por defecto | `dic.setdefault("edad", 25)` |
| `popitem()` | Elimina el último par | `dic.popitem()` |


### Conteo básico


```
texto = "gato perro gato ave perro gato"
```

Construye un diccionario donde:
- La clave sea la palabra
- El valor sea cuántas veces aparece

```
texto = "gato perro gato ave perro gato"

conteo = {}
for palabra in texto.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(conteo)
```

### Filtrado estructural

Dado

```
registros = [
    {"id": 1, "score": 0.8},
    {"id": 2, "score": 0.4},
    {"id": 3, "score": 0.9},
]
```

Crea un diccionario nuevo que:

- Tenga como clave el id
- Tenga como valor el score
- Solo si score >= 0.7

```
print({x["id"]:x["score"] for x in registros if x.get("score")>0.7})
```

### Validación de integridad

Dado:
```
datos = {
    "usuario1": {"python", "ml", "sql"},
    "usuario2": {"java", "sql"},
    "usuario3": {"python", "sql"},
}
```

- Imprime True solo si: todos los usuarios tienen "sql"
- False si alguno no lo tiene

```
print(all("sql" in skills for skills in datos.values()))
```