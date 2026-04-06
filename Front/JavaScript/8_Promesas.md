# Promesas

## Promesa tradicional

```js
fetch("/api/users")
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
```

## async/await (mucho más limpio)

```js
async function obtenerUsuarios() {
  try {
    const response = await fetch("/api/users");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}
```

## En react

```js
useEffect(() => {
  async function cargarDatos() {
    try {
      const data = await api.get("/transacciones");
      setTransacciones(data);
    } catch (err) {
      setError(err.message);
    }
  }
  cargarDatos();
}, []);
```
