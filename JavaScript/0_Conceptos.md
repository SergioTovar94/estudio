# ¿Qué es realmente JavaScript?

Un lenguaje de programación interpretado, dinámico y orientado a objetos basado en prototipos.

## Es un lenguaje interpretado

No se compila como C o Java.

El navegador (o Node.js) lo interpreta y lo ejecuta directamente.

El motor más famoso es:

V8 (usado en Chrome y Node.js)

# Es dinámicamente tipado

No declaras tipos.

let x = 10;
x = "Hola";

Eso es válido.

El tipo puede cambiar en tiempo de ejecución.

# Todo gira alrededor del motor de ejecución

Cuando el navegador ejecuta JS:

Lee el código

Crea un entorno de ejecución

Maneja memoria

Ejecuta línea por línea

# Es single-threaded

JavaScript tiene un solo hilo principal.

Eso significa:

Solo puede ejecutar una cosa a la vez.

Pero entonces…

¿Cómo maneja cosas asíncronas?

Con:

Event Loop

Callbacks

Promesas

async/await

# Es orientado a objetos (pero basado en prototipos)

No usa clases tradicionales como Java o C# originalmente.

Usa prototipos.

Aunque ahora existe class, por debajo sigue siendo prototípico.
