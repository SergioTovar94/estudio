# Vite

Vite es un “build tool” o herramienta de construcción para proyectos frontend modernos.

## Qué hace Vite:

Prepara tu proyecto para desarrollo y producción

Compila JSX, TypeScript, SCSS, etc. a JavaScript que el navegador entiende

Levanta un servidor de desarrollo ultra rápido

Optimiza tu código para producción (minificación, tree-shaking)

## Frameworks que puedes usar con Vite

Cuando creas un proyecto con Vite te pregunta el framework. Los más comunes:

| Framework  | Qué es                                                                                                         |
| ---------- | -------------------------------------------------------------------------------------------------------------- |
| **React**  | Librería de UI más popular para crear interfaces dinámicas. Usas JSX para definir componentes.                 |
| **Vue**    | Framework de JavaScript para UI, muy fácil de aprender y reactivo, similar a React pero con sintaxis distinta. |
| **Svelte** | Framework más moderno que compila tu código a JS puro. Muy rápido, menos librerías, sintaxis simple.           |
| **Lit**    | Librería para Web Components, menos usada pero muy ligera y moderna.                                           |

## Qué incluye Vite dentro de un proyecto

Cuando haces npm create vite@latest frontend, Vite crea:

- package.json → Lista de dependencias y scripts
- node_modules/ → Librerías instaladas
- vite.config.js → Configuración de Vite (puedes personalizar builds, alias, plugins)
- index.html → Entrada del proyecto
- src/ → Carpeta principal donde vivirán tus componentes y páginas
