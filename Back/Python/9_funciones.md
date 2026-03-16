# Funciones anidadas

En Python se pueden definir funciones dentro de funciones para encapsular lógica y aprovechar el scope enclosing; cuando la función interna mantiene acceso a variables externas, se crea una closure.

```
def outer():
    def inner():
        print("Hola desde inner")
    inner()

outer()
```

inner solo existe dentro de outer
Fuera de outer, inner no es visible (scope local).
