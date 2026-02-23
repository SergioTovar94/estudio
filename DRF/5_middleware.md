# Middleware

MIDDLEWARE son funciones que Django ejecuta antes y después de cada request/respuesta HTTP.

El middleware intercepta la petición antes de que llegue a tus vistas, y puede modificarla o rechazarla.

| Middleware                                                    | Para qué sirve                                                                                                                          | Ejemplo o detalle práctico                                                                               |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **`django.middleware.security.SecurityMiddleware`**           | Aplica medidas de seguridad en las respuestas y peticiones. Puede forzar HTTPS, HSTS, y prevenir ciertos ataques.                       | Hace que tu sitio siempre use HTTPS y protege contra ataques de tipo clickjacking o “injection” simples. |
| **`django.contrib.sessions.middleware.SessionMiddleware`**    | Habilita el uso de **sesiones** en Django. Permite guardar datos de usuario entre requests.                                             | Guarda si un usuario está logueado, items en un carrito de compras, etc.                                 |
| **`django.middleware.common.CommonMiddleware`**               | Aplica reglas generales de manejo de requests/respuestas: redirecciones de slash al final, manejo de códigos 404, etc.                  | Redirige automáticamente `/about` a `/about/` si falta el slash final.                                   |
| **`django.middleware.csrf.CsrfViewMiddleware`**               | Protege tu app contra ataques CSRF (**Cross-Site Request Forgery**). Verifica que los formularios y requests POST provengan de tu app.  | Evita que un atacante haga que un usuario logueado envíe un formulario a tu app desde otro sitio.        |
| **`django.contrib.auth.middleware.AuthenticationMiddleware`** | Conecta las **sesiones** con el sistema de **usuarios de Django** (`request.user`).                                                     | Permite saber quién está logueado y usar `request.user` en tus vistas o templates.                       |
| **`django.contrib.messages.middleware.MessageMiddleware`**    | Permite enviar mensajes temporales entre requests (por ejemplo, alertas de éxito o error).                                              | Después de un login fallido, puedes mostrar “Usuario o contraseña incorrecta” en la siguiente página.    |
| **`django.middleware.clickjacking.XFrameOptionsMiddleware`**  | Protege tu app contra ataques de clickjacking. Agrega cabeceras HTTP que impiden que tu página sea embebida en un iframe de otro sitio. | Evita que alguien haga un “botón invisible” sobre tu web dentro de otra página para engañar al usuario.  |

CorsMiddleware revisa cada petición del frontend y agrega los headers de CORS necesarios para que el navegador deje pasar la respuesta.
