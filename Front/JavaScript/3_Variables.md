# Variables y tipos modernos (ES6+)

## let: para variables que cambian

```JavaScript
let contador = 0;
contador = 1;
```

## const: para valores fijos (objetos y arrays también, pero su contenido puede cambiar)

```JavaScript
const nombre = 'Juan';
// nombre = 'Pedro'; ❌ error
const usuario = { nombre: 'Juan' };
usuario.nombre = 'Pedro'; // ✅ se puede modificar la propiedad
```

## Tipos

```js
const email = "test@example.com"; // string
const edad = 30; // number
const isLogged = false; // boolean
const lista = [1, 2, 3]; // array
const persona = { nombre: "Ana" }; // objeto
let algo; // undefined
```
