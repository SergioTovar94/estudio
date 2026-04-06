# Tailwind CSS

npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

CSS tradicional

```CSS
.button {
  background-color: blue;
  padding: 10px;
  border-radius: 8px;
}
```

Luego:

```HTML
<button class="button">Login</button>
```

Con Tailwind

No creas CSS.

```HTML
<button class="bg-blue-500 p-2 rounded">
  Login
</button>
```

Las clases ya existen.

```
bg-blue-500 → color azul
p-2 → padding
rounded → bordes redondeados
```

```bash
npm install -D tailwindcss postcss autoprefixer
```

-D significa que es para desarrollo

**tailwindcss:** Es el framework. Genera las clases CSS

Ejemplo:

```
bg-blue-500
text-center
flex
p-4
```

**postcss:** Es un procesador de CSS. Transforma CSS automáticamente

Tailwind funciona sobre PostCSS.

**autoprefixer:** Agrega compatibilidad con navegadores.

Ejemplo:

display: flex;

Se convierte en:

display: -webkit-flex;
display: flex;

**npx tailwindcss init -p:** Este comando crea archivos de configuración.

```
npx tailwindcss init -p
```

Significa: Inicializar Tailwind

Crea:

tailwind.config.js
postcss.config.js

## Explicación de las mejoras visuales con Tailwind CSS

| Clase                                          | Efecto visual                                                      |
| ---------------------------------------------- | ------------------------------------------------------------------ |
| `min-h-screen`                                 | Ocupa toda la altura de la ventana (viewport)                      |
| `flex items-center justify-center`             | Centra el contenido horizontal y verticalmente                     |
| `bg-gradient-to-br from-blue-50 to-indigo-100` | Fondo con degradado suave de azul claro a índigo claro             |
| `bg-white p-8 rounded-2xl shadow-xl`           | Tarjeta blanca con padding, bordes muy redondeados y sombra grande |
| `w-full max-w-md`                              | Ancho completo hasta 28rem (aprox. 448px) – responsive             |
| `text-3xl font-bold`                           | Título grande y en negrita                                         |
| `space-y-5`                                    | Espaciado vertical uniforme entre los elementos del formulario     |
| `focus:ring-2 focus:ring-blue-500`             | Anillo azul al enfocar los inputs (feedback visual)                |
| `transition`                                   | Suaviza los cambios de color, sombra, etc.                         |
| `hover:scale-[1.02]`                           | El botón se agranda ligeramente al pasar el ratón                  |
| `hover:underline`                              | El enlace se subraya al pasar el ratón                             |
