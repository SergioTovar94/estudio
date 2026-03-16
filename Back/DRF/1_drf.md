# Django Rest Framework

Django REST Framework es una librería que se instala encima de Django para convertirlo en un framework especializado en crear APIs REST. No reemplaza a Django, lo extiende.

## Lo que DRF agrega

### Serialirzers

Django normal no sabe convertir modelos a JSON de forma elegante.

DRF agrega:

- Serializers (como los forms, pero para APIs)
- Validación automática
- Conversión modelo ↔ JSON
- Control de qué campos se exponen

### ViewSets

En Django normal haces:

- create()
- list()
- retrieve()
- update()
- delete()

A mano.
DRF te permite hacer todo eso con una sola clase:

```Python
class PacienteViewSet(ModelViewSet):
```

Y listo. CRUD completo automático.

### Routers automáticos

En Django debes declarar cada ruta. En DRF haces:

```Python
router.register('pacientes', PacienteViewSet)
```

Y genera automáticamente:

- GET /pacientes/
- POST /pacientes/
- GET /pacientes/1/
- PUT /pacientes/1/
- DELETE /pacientes/1/

### Respuestas inteligentes

DRF tiene:

```Python
from rest_framework.response import Response
```

Y maneja:

- JSON automático
- Status codes
- Content negotiation

### Autenticación para APIs

DRF trae:

- Token Authentication
- Session Authentication
- JWT (con librerías externas)
- Permisos personalizados

Django tiene auth, pero no pensado específicamente para APIs REST.

### 6. Navegador interactivo

DRF tiene una vista web automática donde puedes:

- Probar endpoints
- Ver formularios
- Hacer POST desde el navegador
- Ver documentación básica

Es como un mini-Postman integrado.

## Lo que DRF NO QUITA

Importante: DRF no elimina nada de Django.

Sigues teniendo:

- Models
- ORM
- Migraciones
- Auth
- Admin
- Seguridad
- Settings

DRF solo trabaja en la capa de vistas/respuestas.

# Diferencias entre Django y Django REST Framework (DRF)

| Aspecto                | Django                                          | Django REST Framework (DRF)                             |
| ---------------------- | ----------------------------------------------- | ------------------------------------------------------- |
| Tipo de herramienta    | Framework web completo                          | Framework especializado para construir APIs REST        |
| Enfoque principal      | Aplicaciones web tradicionales (HTML + backend) | APIs RESTful (JSON)                                     |
| Devuelve por defecto   | HTML (Templates)                                | JSON (y otros formatos como XML si se configura)        |
| Serialización          | No tiene sistema formal de serializers          | Tiene `Serializer` y `ModelSerializer`                  |
| Validación para APIs   | Manual                                          | Automática mediante Serializers                         |
| CRUD automático API    | No                                              | Sí, con `ModelViewSet`                                  |
| Sistema de rutas API   | Manual con `path()`                             | Automático con `Router`                                 |
| Manejo de métodos HTTP | Manual (`if request.method == ...`)             | Automático (GET, POST, PUT, PATCH, DELETE)              |
| Autenticación          | Basada en sesión (web)                          | Token, Session, Basic, JWT (extensión)                  |
| Permisos API           | Manual                                          | Sistema de permisos integrado (`IsAuthenticated`, etc.) |
| Paginación             | Manual                                          | Automática configurable                                 |
| Filtros y búsqueda     | Manual                                          | Integrado y configurable                                |
| Manejo de errores      | Manual                                          | Respuestas estructuradas estándar JSON                  |
| Interfaz de prueba     | No                                              | Browsable API incluida                                  |
| Nivel de abstracción   | Más bajo para APIs                              | Más alto y estructurado para APIs                       |
| Curva de aprendizaje   | Más simple al inicio                            | Un poco más avanzada                                    |
| Uso típico             | Apps web tradicionales                          | Backend para frontend (React, Vue, etc.)                |

---

## Resumen conceptual

- **Django** → Framework web general.
- **DRF** → Extensión que convierte Django en un framework profesional para APIs REST.
