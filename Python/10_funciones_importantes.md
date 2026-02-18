# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

Abre el archivo y devuelve el objeto de archivo correspondiente . Si no se puede abrir el archivo, OSErrorse lanza una instrucción.

```Python
f = open("datos.txt", "r")
```

Eso significa:

- "datos.txt" → qué archivo
- "r" → cómo lo quieres abrir

Los modos de apertura más importantes son:

| Modo   | Significa                           |
| ------ | ----------------------------------- |
| `"r"`  | read (leer)                         |
| `"w"`  | write (escribir, borra lo anterior) |
| `"a"`  | append (agregar al final)           |
| `"rb"` | read binary                         |
| `"wb"` | write binary                        |

# map

map() es una función de Python que sirve para:

Aplicar una función a cada elemento de un iterable.

Y devuelve los resultados transformados.

## Sintaxis

`map(funcion, iterable)`

🔹 Ejemplo simple

Supongamos que tienes:

`numeros = [1, 2, 3, 4]`

Y quieres elevar cada número al cuadrado.

Sin map:

```Python
resultado = []
for n in numeros:
    resultado.append(n * n)
```

Con map:

```Pyton
resultado = map(lambda n: n * n, numeros)
```

Pero ojo 👀

map no devuelve una lista directamente.

Devuelve un objeto especial iterable.

Para verlo como lista:

`list(resultado)`

Resultado:

`[1, 4, 9, 16]`

# with

Se usa para manejar recursos automáticamente

Recurso = algo que debe abrirse y luego cerrarse.

Ejemplos típicos:

- Archivos
- Conexiones a bases de datos
- Locks
- Sockets
