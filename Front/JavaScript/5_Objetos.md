# Objetos

## Acceder y modificar propiedades

```js
const user = { name: "Sergio", age: 30 };
user.age = 31; // modificar
user.email = "s@mail.com"; // agregar
delete user.age; // eliminar
```

## Object.keys, values, entries

```js
const user = { a: 1, b: 2 };
Object.keys(user); // ['a','b']
Object.values(user); // [1,2]
Object.entries(user); // [['a',1], ['b',2]]
```

## Optional chaining (?.) – evitar errores de undefined

```js
const user = { profile: { name: "Sergio" } };
console.log(user.profile?.name); // 'Sergio'
console.log(user.contact?.email); // undefined (no error)
// En React, cuando los datos vienen del backend
const nombre = transaccion?.categoria?.nombre ?? "Sin categoría";
```

## Nullish coalescing (??) – valor por defecto solo si es null o undefined

```js
const valor = null ?? "por defecto"; // 'por defecto'
const cero = 0 ?? "por defecto"; // 0 (porque 0 no es null/undefined)
// Ojo: || toma falsey: 0, '' también
```

# Destructuración de objetos

## Forma tradicional

```js
const user = { name: "Sergio", age: 30, email: "s@example.com" };

const name = user.name;
const age = user.age;
```

## Con desestructuración

```js
const { name, age } = user;
console.log(name); // 'Sergio'
```

## En parámetros de función (muy común en React)

```js
function UserProfile({ name, age }) {
  // ← ya tienes name y age
  return (
    <div>
      {name} tiene {age} años
    </div>
  );
}
```
