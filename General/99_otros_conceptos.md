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

## Colisión

Una colisión ocurre cuando dos valores distintos producen el mismo hash. Es decir: Dos cosas diferentes quieren ir al mismo casillero.

### ¿Por qué las colisiones son inevitables?

Porque:

- Hay infinitos valores posibles
- Pero un número finito de posiciones

Por muy buena que sea la función hash: alguna vez dos valores chocarán. Lo importante no es evitarlas, sino resolverlas bien.

# Script vs Aplicación

Un script es:

- Un programa pequeño o puntual.
- Se ejecuta de principio a fin.
- Normalmente automatiza una tarea concreta.
- Tiene poca estructura.

Una aplicación es:

- Un sistema más grande y estructurado.
- Con múltiples módulos.
- Pensada para uso contínuo.
- Con lógica, estado y a veces interfaz

# Migraciones

Son una forma de poder actualizar la base de datos a partir de código, en este caso python.
