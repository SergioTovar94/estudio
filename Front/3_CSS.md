# ¿Qué es CSS?

CSS significa: Cascading Style Sheets

Sirve para controlar:

- 🎨 Colores
- 📏 Tamaños
- 📐 Espaciado
- 📦 Distribución
- 🧱 Layout

HTML estructura.
CSS da apariencia.

# Selectores

Existen selectores por

- Etiqueta
- Por clase .
- Por id #
- Descendente

# ¿Qué significa "Cascading"?

CSS tiene reglas de prioridad.

Si hay conflicto:

style inline (más fuerte)

1. id
2. class
3. etiqueta (menos fuerte)

Ejemplo:

```CSS
p { color: blue; }
.texto { color: red; }
```

Si el párrafo tiene clase texto, será rojo.

# Box Model

Todo elemento HTML es una caja. Una caja tiene:

```
┌───────────────────────┐
│         margin        │
│  ┌─────────────────┐  │
│  │      border     │  │
│  │  ┌───────────┐  │  │
│  │  │  padding  │  │  │
│  │  │ ┌───────┐ │  │  │
│  │  │ │content│ │  │  │
│  │  │ └───────┘ │  │  │
│  │  └───────────┘  │  │
│  └─────────────────┘  │
└───────────────────────┘
```

Visualmente:

```
| margin |
  | border |
    | padding |
      | content |
```

Ejemplo:

```CSS
div {
  margin: 20px;
  padding: 10px;
  border: 2px solid black;
}
```

# Unidades importantes

| Unidad | Significado                  |
| ------ | ---------------------------- |
| `px`   | píxeles                      |
| `%`    | porcentaje                   |
| `em`   | relativo al tamaño del padre |
| `rem`  | relativo al tamaño raíz      |
| `vh`   | % del alto de pantalla       |
| `vw`   | % del ancho de pantalla      |

# Display

Controla cómo se comporta el elemento:

| Valor          | Comportamiento          |
| -------------- | ----------------------- |
| `block`        | Ocupa toda la línea     |
| `inline`       | Solo ocupa su contenido |
| `inline-block` | Mezcla de ambos         |
| `flex`         | Activa Flexbox          |
| `grid`         | Activa Grid             |

# Flexbox

Flexbox sirve para organizar elementos horizontal o verticalmente con control total.

Para activar Flexbox

```CSS
.container {
  display: flex;
}
```

Eso convierte al contenedor en flex.

```CSS
flex-direction: row;      /* horizontal */
flex-direction: column;   /* vertical */
```
