# ¿Qué es HTML?

HTML significa:

HyperText Markup Language

No es un lenguaje de programación.
Es un lenguaje de estructura.

Sirve para decirle al navegador:

- “Esto es un título”,
- “Esto es un botón”,
- “Esto es una imagen”,
- “Esto es una lista”.

# 2. Estructura básica de un documento HTML

Un archivo mínimo se ve así:

```HTML
<!DOCTYPE html>
<html>
  <head>
    <title>Mi página</title>
  </head>
  <body>
    <h1>Hola mundo</h1>
  </body>
</html>
```

## Etiquetas con significado

| Etiqueta    | Para qué se usa                |
| ----------- | ------------------------------ |
| `<header>`  | Encabezado de página o sección |
| `<nav>`     | Navegación                     |
| `<main>`    | Contenido principal            |
| `<section>` | Sección temática               |
| `<article>` | Contenido independiente        |
| `<aside>`   | Información secundaria         |
| `<footer>`  | Pie de página                  |

Son atributos que puedes usar prácticamente en cualquier elemento HTML:

## Atributos globales

| Atributo          | Para qué sirve                           | Ejemplo                        |
| ----------------- | ---------------------------------------- | ------------------------------ |
| `id`              | Identificador único del elemento         | `<div id="main">`              |
| `class`           | Agrupa elementos para aplicar estilos    | `<p class="texto">`            |
| `style`           | Estilo inline                            | `<h1 style="color:red;">`      |
| `title`           | Tooltip (texto al pasar el mouse)        | `<span title="Info">`          |
| `hidden`          | Oculta el elemento                       | `<div hidden>`                 |
| `tabindex`        | Controla el orden de enfoque con teclado | `<input tabindex="1">`         |
| `contenteditable` | Permite editar el contenido              | `<div contenteditable="true">` |
| `draggable`       | Permite arrastrar el elemento            | `<div draggable="true">`       |
| `lang`            | Idioma del contenido                     | `<p lang="es">`                |
| `dir`             | Dirección del texto (`ltr` o `rtl`)      | `<p dir="rtl">`                |
| `data-*`          | Datos personalizados                     | `<div data-id="123">`          |

# 3. Etiquetas importantes

## Títulos

```HTML
<h1>Título principal</h1>
<h2>Subtítulo</h2>
<h3>Sección</h3>
```

Van de <h1> a <h6>.

## Párrafos

```HTML
<p>Este es un párrafo.</p>
```

Div (muy importante para React)

```HTML
<div>Contenido</div>
```

div no tiene significado semántico.
Es solo un contenedor.

React usa muchísimo div.

## Botones

```HTML
<button>Haz clic</button>
```

| Atributo   | Tipo       | Para qué sirve                    | Ejemplo                  |
| ---------- | ---------- | --------------------------------- | ------------------------ |
| `type`     | Específico | `"button"`, `"submit"`, `"reset"` | `<button type="submit">` |
| `disabled` | Booleano   | Desactiva el botón                | `<button disabled>`      |
| `name`     | Específico | Identificador en formularios      | `<button name="enviar">` |
| `value`    | Específico | Valor enviado en formulario       | `<button value="ok">`    |
| `id`       | Global     | Identificador único               |                          |
| `class`    | Global     | Estilos                           |                          |

## Inputs

```HTML
<input type="text" />
<input type="password" />
<input type="number" />
```

| Atributo      | Tipo       | Para qué sirve                                        | Ejemplo                           |
| ------------- | ---------- | ----------------------------------------------------- | --------------------------------- |
| `type`        | Específico | `"text"`, `"password"`, `"email"`, `"checkbox"`, etc. | `<input type="text">`             |
| `name`        | Específico | Identifica el campo                                   | `<input name="usuario">`          |
| `value`       | Específico | Valor del campo                                       | `<input value="Sergio">`          |
| `placeholder` | Específico | Texto guía                                            | `<input placeholder="Tu nombre">` |
| `required`    | Booleano   | Campo obligatorio                                     | `<input required>`                |
| `disabled`    | Booleano   | Desactiva el input                                    | `<input disabled>`                |
| `checked`     | Booleano   | Para checkbox/radio                                   | `<input type="checkbox" checked>` |
| `readonly`    | Booleano   | Solo lectura                                          | `<input readonly>`                |
| `min`         | Específico | Valor mínimo (number)                                 | `<input type="number" min="0">`   |
| `max`         | Específico | Valor máximo                                          |                                   |
| `maxlength`   | Específico | Máximo caracteres                                     |                                   |
| `id`          | Global     | Identificador                                         |                                   |
| `class`       | Global     | Estilos                                               |                                   |

## Enlaces

```HTML
<a href="https://google.com">Ir a Google</a>
```

| Atributo   | Tipo       | Para qué sirve         | Ejemplo               |
| ---------- | ---------- | ---------------------- | --------------------- |
| `href`     | Específico | URL destino            | `<a href="/home">`    |
| `target`   | Específico | Dónde abrir (`_blank`) | `<a target="_blank">` |
| `rel`      | Específico | Seguridad (`noopener`) | `<a rel="noopener">`  |
| `download` | Específico | Descarga archivo       | `<a download>`        |
| `id`       | Global     | Identificador          |                       |
| `class`    | Global     | Estilos                |                       |

## Imágenes

```HTML
<img src="imagen.jpg" alt="Descripción" />
```

| Atributo  | Tipo       | Para qué sirve               | Ejemplo                   |
| --------- | ---------- | ---------------------------- | ------------------------- |
| `src`     | Específico | Ruta de la imagen            | `<img src="foto.jpg">`    |
| `alt`     | Específico | Texto alternativo            | `<img alt="Foto perfil">` |
| `width`   | Específico | Ancho                        | `<img width="200">`       |
| `height`  | Específico | Alto                         | `<img height="150">`      |
| `loading` | Específico | `"lazy"` para carga diferida | `<img loading="lazy">`    |
| `id`      | Global     | Identificador                |                           |
| `class`   | Global     | Estilos                      |                           |
