# Operador ternario (? :)

Es una forma corta de escribir un if-else.

```js
condicion ? valorSiTrue : valorSiFalse;
```

Ejemplo simple

```js
const edad = 18;

const mensaje = edad >= 18 ? "Es mayor de edad" : "Es menor de edad";
```

Esto es equivalente a:

```js
let mensaje;

if (edad >= 18) {
  mensaje = "Es mayor de edad";
} else {
  mensaje = "Es menor de edad";
}
```

# Cortocircuito (Short-circuit)

Es cuando JavaScript deja de evaluar una expresión lógica tan pronto ya sabe el resultado.
Se usa principalmente con:

```
&&
||
```

## Cortocircuito con && (AND)

Regla:

```
Si el primero es false → devuelve el primero
Si el primero es true → evalúa el segundo
```

Ejemplo

```js
isLoggedIn && console.log("Bienvenido");
```

Esto significa:

```js
if (isLoggedIn) {
  console.log("Bienvenido");
}
```

Muy usado para ejecutar algo solo si una condición es verdadera.

## Cortocircuito con || (OR)

Regla:

Si el primero es true → devuelve el primero
Si el primero es false → devuelve el segundo
Ejemplo

```js
const nombre = inputNombre || "Invitado";
```

Significa:

```js
let nombre;

if (inputNombre) {
  nombre = inputNombre;
} else {
  nombre = "Invitado";
}
```

Esto se usa muchísimo para:

- valores por defecto
- evitar null o undefined
- simplificar validaciones
