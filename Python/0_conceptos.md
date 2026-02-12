# REPL

Es el entorno de programación en python a través de una terminal. Sus siglas hacen referencia a Read, Eval, Print y Loop. Es decir,
es un loop que constantemente está leyendo, evaluando y escribiendo por terminal.

# Hash

Una búsqueda por hash es una forma de encontrar un dato casi instantáneamente, sin recorrer uno por uno los elementos.

En vez de buscar así:

`“¿está este valor aquí?” → revisar elemento por elemento`

Python hace esto:

```
“convierto el valor en un número → voy directo a donde debería estar”
```

Ese número es el hash.

## En Python

Diccionarios

```
edades = {"Ana": 20, "Luis": 30}

print(edades["Ana"])  # acceso por hash

```

Sets

```
usuarios = {"ana", "luis", "carlos"}

print("ana" in usuarios)  # búsqueda por hash
```

Tanto dict como set están implementados como tablas hash.

# GIL

Hace referencia a Global Interpreter Lock o Bloqueo Global del Intérprete. Es un mecanismo de CPython que asegura que un solo hilo ejecutre bytecode de Python, incluso en procesadores multinúcleo. Evita conflictos de acceso a memoria pero limita el rendimiento real en tareas pesadas que usan CPU multithreading.

# **init**

Es el constructor de una clase

# Iterable e iterador

Un iterable puede producir iteradores; un iterador mantiene estado y se agota.

# PEP8

PEP8 (Python Enhancement Proposal 8) es la guía de estilo oficial para escribir código en Python, enfocada en maximizar la legibilidad y consistencia.
