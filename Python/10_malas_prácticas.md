# Malas prácticas

Es mala práctica porque el valor por defecto es un objeto mutable que se comparte entre llamadas, lo que puede producir efectos secundarios difíciles de detectar y bugs inesperados.

```
def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())
```
