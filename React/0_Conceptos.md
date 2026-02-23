# ¿Qué es React

Es una librería para construir interfaces de usuario

Antes de React, el frontend era así:

- HTML estático
- Manipulación manual del DOM
- Mucho código desordenado
- Difícil de mantener

Cuando una app crece (login, dashboard, tablas, filtros, modales), el código se vuelve caótico.

React propone una idea poderosa: “La interfaz es una función del estado.”

Es decir: UI = f(estado)

Si el estado cambia → la UI se actualiza sola.

# ¿Qué es UI?

UI significa User Interface (en español: Interfaz de Usuario). Es todo lo que el usuario:

- 👀 Ve
- 🖱 Puede tocar o clickear
- ⌨️ Puede escribir
- 📱 Puede interactuar

## Ejemplos de UI

En una página web:

- Botones
- Inputs
- Formularios
- Cards
- Menús
- Modales
- Listas
- Textos
- Imágenes

Todo eso es UI.

# Componentes

React divide la interfaz en piezas pequeñas llamadas componentes.

Ejemplo mental:

Una app puede dividirse así:

- App
- Navbar
- Sidebar
- Dashboard
- UserList
- UserCard

Cada bloque es un componente independiente.

Esto permite:

- Reutilizar
- Mantener orden
- Escalar el proyecto

# El siguiente concepto clave: Estado (State)

Ahora viene lo importante. Un componente puede tener información que cambia:

- Usuario logueado
- Lista de productos
- Formulario
- Contador

Eso es el estado.

Si el estado cambia → React vuelve a renderizar ese componente.

Ejemplo simple mental:

Estado = contador = 0
Usuario hace click → contador = 1
React actualiza pantalla automáticamente.

# Entonces… ¿para qué existen los Hooks?

Antes, solo las clases podían tener estado. Ahora React usa componentes funcionales. Pero necesitaban forma de tener estado y lógica.

Ahí nacen los Hooks.

Los hooks permiten:

- Guardar estado → useState
- Ejecutar efectos → useEffect
- Compartir lógica → hooks personalizados

Entonces:

Hook = herramienta para manejar comportamiento dinámico.

# ¿Dónde entra fetch?

Tu frontend no vive solo. Necesita datos del backend (por ejemplo tu API en Django).

Entonces el flujo real es:

Usuario entra →
React carga →
Hace una petición HTTP →
Recibe datos →
Guarda datos en estado →
Renderiza.

# Estructura común de un proyecto

## Components

Componentes reutilizables (botones, cards, modales).

## Pages

Pantallas completas.

## Services

Conexión al backend (axios o fetch).

## Hooks

Son funciones especiales que permiten que un componente funcional tenga:

- Estado
- Efectos secundarios
- Lógica reutilizable

### useState

Sirve para manejar estado.

```JavaScript
const [contador, setContador] = useState(0);
```

Aquí:

- contador → valor actual
- setContador → función para actualizarlo

### useEffect

Sirve para ejecutar algo cuando:

- El componente se monta
- Una variable cambia

Ejemplo típico: hacer una llamada a una API.
