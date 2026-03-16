# ¿Que es un serializer?

Primero pensemos en el problema. El modelo en Django es una clase que vive en Python, pero una API habla JSON. Entonces hay una necesidad de traducción.

- Python → JSON
- JSON → Python

## Analogía simple

Imagina que tu modelo es un objeto complejo en memoria:

```Python
Paciente(
    nombre="Sergio",
    edad=30,
    documento="123"
)
```

Pero cuando haces un GET, el navegador necesita algo así:

```JSON
{
    "nombre": "Sergio",
    "edad": 30,
    "documento": "123"
}
```

El serializer convierte objetos Python en JSON.
Y también hace lo contrario: toma JSON y lo convierte en objetos válidos.

Básicamente se puede ver así:

```
Base de datos
     ↓
Modelo Django (Python)
     ↓
Serializer
     ↓
JSON (API)
```
