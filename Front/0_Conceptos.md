# DOM

Document Object Model. Es la representación en forma de árbol que el navegador crea cuando lee tu HTML.

El DOM no es el HTML. Es lo que el navegador construye a partir del HTML.

Ejemplo simple. Si tienes este HTML:

```HTML
<body>
  <h1>Hola</h1>
  <p>Texto</p>
</body>
```

El navegador lo convierte en algo así:

```
body
 ├── h1
 │    └── "Hola"
 └── p
      └── "Texto"
```

Eso es el DOM: un árbol de nodos.

## ¿Qué es un nodo?

Todo en el DOM es un objeto:

- Elementos (div, p, button)
- Texto
- Atributos

Por eso se llama Document Object Model:
porque cada cosa se convierte en un objeto manipulable con JavaScript.

## ¿Por qué existe?

Para que JavaScript pueda hacer cosas como:

- document.getElementById("titulo")
- document.querySelector("p")

Sin DOM, JavaScript no podría modificar la página.
