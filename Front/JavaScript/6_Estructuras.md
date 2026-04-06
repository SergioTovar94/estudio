# Arrays

## Map

Transformar cada elemento (lo más usado en React)

```js
const numeros = [1, 2, 3];
const dobles = numeros.map((n) => n * 2); // [2,4,6]
```

### En React para renderizar listas

```js
const usuarios = [
  { id: 1, nombre: "Juan" },
  { id: 2, nombre: "Ana" },
];
return (
  <ul>
    {usuarios.map((user) => (
      <li key={user.id}>{user.nombre}</li>
    ))}
  </ul>
);
```

## Filter

```js
const numeros = [1, 2, 3, 4, 5];
const pares = numeros.filter((n) => n % 2 === 0); // [2,4]
```

### Ejemplo real: filtrar transacciones por tipo

```js
const fijos = transacciones.filter((tx) => tx.tipo === "Fijos Hogar");
```

## some() y every() – comprobar condiciones

```js
const numeros = [1, 2, 3];
const hayMayorQue2 = numeros.some((n) => n > 2); // true
const todosMayoresQue0 = numeros.every((n) => n > 0); // true
```

## reduce() – acumular valores

```js
array.reduce((acumulador, elementoActual) => {
  return nuevoValor;
}, valorInicial);
```

Parámetros:

- acumulador → donde se guarda el resultado
- elementoActual → el valor actual del arreglo
- valorInicial → desde dónde empieza el acumulador

```js
const gastos = [100, 200, 50];
const total = gastos.reduce((acum, actual) => acum + actual, 0); // 350
```

## Destructuración de arrays

```js
const colores = ["rojo", "verde", "azul"];
const [primero, segundo] = colores;
console.log(primero); // 'rojo'
```

### Para ignorar elementos

```js
const [, , tercero] = colores;
console.log(tercero); // 'azul'
```
