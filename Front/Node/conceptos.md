# Qué es Node

Es un entorno de ejecución para JavaScript fuera del navegador.

Es decir:

- Antes → JavaScript solo vivía en el navegador.
- Con Node.js → puedes usar JavaScript en el servidor.

# Para qué se usa?

Principalmente para:

- Crear APIs REST
- Backend de aplicaciones web
- WebSockets (tiempo real)
- Microservicios
- Herramientas CLI
- Automatización

# ¿Cómo se gestionan dependencias?

## NPM - Node Package Manager

Con npm. Es el gestor de paquetes más grande del mundo.

- Instalar librerías y frameworks (npm install react)
- Manejar dependencias de un proyecto
- Ejecutar scripts (npm run dev)
- Mantener versiones de paquetes
- Instalas librerías así:

```Bash
npm install express
```

## nvm — Node Version Manager

nvm permite tener múltiples versiones de Node en el mismo PC.

Esto es útil porque:

- Un proyecto usa Node 18
- Otro proyecto usa Node 20
- Puedes cambiar entre versiones sin romper nada

## npx — Node Package eXecute

npx permite ejecutar paquetes directamente sin instalarlos globalmente.

Muy útil para:

- Crear proyectos nuevos
- Probar librerías sin instalarlas
- Ejecutar comandos de herramientas CLI

| Herramienta | Para qué sirve                                 |
| ----------- | ---------------------------------------------- |
| **npm**     | Instalar y manejar librerías/proyectos         |
| **npx**     | Ejecutar paquetes sin instalarlos globalmente  |
| **nvm**     | Cambiar entre versiones de Node según proyecto |
