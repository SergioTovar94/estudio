# Definición

Axios es una librería de JavaScript para hacer peticiones HTTP a una API.

En otras palabras, sirve para que tu frontend (React) pueda hablar con tu backend (Django + DRF)

# Qué tipos de peticiones puedes hacer

Método Para qué sirve
GET obtener datos
POST crear datos
PUT actualizar datos
PATCH actualizar parcialmente
DELETE eliminar datos

## Relación entre fetch y axios

| Característica    | fetch                    | axios                       |
| ----------------- | ------------------------ | --------------------------- |
| Qué es            | API nativa de JavaScript | Librería externa            |
| Instalación       | No                       | Sí (`npm install axios`)    |
| Devuelve          | Response                 | Data directamente           |
| JSON automático   | No                       | Sí                          |
| Manejo de errores | Manual                   | Automático                  |
| Interceptors      | No                       | Sí                          |
| Popular en        | Web estándar             | Apps grandes / React / APIs |
