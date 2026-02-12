# Generadores

Permiten extraer valores de una función y almacenarlos de uno en uno en objetos iterables (que
se pueden recorrer). Sin la necesidad de almacenarlos todos a la vez en la memoria ram.

## Ejemplo básico: Sin generador

```python
def numeros_sin_generador(n):
    resultado = []
    for i in range(n):
        resultado.append(i)
    return resultado

nums = numeros_sin_generador(5)
for num in nums:
    print(num)
```

**Problema:** La función crea una lista completa en memoria con todos los números antes de devolverla. Si `n` es muy grande (ej: 1 millón), consume mucha RAM.

## Ejemplo básico: Con generador

```python
def numeros_con_generador(n):
    for i in range(n):
        yield i

nums = numeros_con_generador(5)
for num in nums:
    print(num)
```

**Ventaja:** El generador produce los números uno a uno bajo demanda usando `yield`. No almacena toda la lista en memoria.

## Diferencia en memoria

- **Sin generador:** Almacena `[0, 1, 2, 3, 4]` completamente en RAM antes de usarla.
- **Con generador:** Produce cada número cuando se solicita (lazy evaluation). Solo ocupa una pequeña cantidad de memoria constante.

Para números grandes:

```python
# Sin generador: crea lista de 1 millón de elementos
lista = numeros_sin_generador(1000000)  # Alto uso de memoria

# Con generador: no crea lista, genera bajo demanda
gen = numeros_con_generador(1000000)  # Mínimo uso de memoria
```

- Los generadores son más eficientes que las funciones tradicionales.
- Muy útiles con listas de valores infinitos.
- Entre llamada y llamada, el objeto iterable entra en estado de pausa (suspensión).

## Métodos de generadores

| Método    | Descripción                                                                                              | Ejemplo                                                |
| --------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| `next()`  | Obtiene el siguiente valor del generador. Lanza `StopIteration` cuando no hay más valores.               | `next(gen)` devuelve el próximo valor                  |
| `send()`  | Envía un valor al generador y reanuda su ejecución desde el `yield`. Permite comunicación bidireccional. | `gen.send(valor)` retorna el resultado de `yield`      |
| `throw()` | Lanza una excepción en el punto donde el generador está pausado.                                         | `gen.throw(TypeError, "mensaje")` genera una excepción |
| `close()` | Cierra el generador de forma limpia, lanzando `GeneratorExit` en su interior.                            | `gen.close()` detiene la ejecución                     |

### Ejemplo con `next()`

```python
def contador():
    n = 0
    while True:
        yield n
        n += 1

gen = contador()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
```

### Ejemplo con `send()`

```python
def dialogar():
    x = yield "¿Cuál es tu nombre?"
    yield f"Hola, {x}!"

gen = dialogar()
print(next(gen))           # ¿Cuál es tu nombre?
print(gen.send("Juan"))    # Hola, Juan!
```

### Ejemplo con `throw()`

```python
def procesar():
    try:
        yield "Procesando..."
        yield "Completado"
    except ValueError as e:
        yield f"Error capturado: {e}"

gen = procesar()
print(next(gen))              # Procesando...
print(gen.throw(ValueError, "Datos inválidos"))  # Error capturado: Datos inválidos
```

### Ejemplo con `close()`

```python
def limpiar():
    try:
        yield "Inicio"
        yield "Proceso"
    finally:
        print("Generador cerrado")

gen = limpiar()
print(next(gen))  # Inicio
gen.close()       # Imprime: Generador cerrado
```
