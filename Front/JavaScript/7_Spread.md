# Spread (...) para expandir elementos

## Copiar arrays

```js
const original = [1, 2, 3];
const copia = [...original]; // [1,2,3]
```

## Combinar arrays

```js
const mas = [4, 5];
const todos = [...original, ...mas]; // [1,2,3,4,5]
```

## Copiar objetos

```js
const usuario = { nombre: "Ana", edad: 25 };
const copiaUsuario = { ...usuario };
```

## Sobrescribir propiedades

```js
const usuarioConEmail = { ...usuario, email: "ana@mail.com" };
// resultado: { nombre: 'Ana', edad: 25, email: 'ana@mail.com' }
```
