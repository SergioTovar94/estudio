# For clasico

```JavaScript
for (inicialización; condición; actualización) {
  // código a ejecutar
}
```

## for...of (para recorrer valores)

```JavaScript
const numeros = [10, 20, 30];

for (const numero of numeros) {
  console.log(numero);
}
```

# for...in (para recorrer propiedades)

```JavaScript
const persona = {
  nombre: "Sergio",
  edad: 25
};

for (const clave in persona) {
  console.log(clave, persona[clave]);
}
```

# forEach (método de array)

No es un for como tal, pero cumple función similar:forEach (método de array)

```JavaScript
const numeros = [1, 2, 3];

numeros.forEach(function(numero) {
  console.log(numero);
});
```

O versión moderna:

```JavaScript
numeros.forEach(numero => console.log(numero));
```

```JavaScript

```
