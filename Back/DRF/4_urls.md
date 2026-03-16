# URLs

DRF no reemplaza las urls Django, las utiliza. La base sigue siendo el archivo urls.py del proyecto.

🧱 Flujo real cuando haces una petición

Cuando visitas:

http://127.0.0.1:3000/api/pacientes/

Pasa esto internamente:

```
Request HTTP
    ↓
urls.py del proyecto
    ↓
include(...)
    ↓
urls.py de la app
    ↓
Router de DRF
    ↓
ViewSet
    ↓
Serializer
    ↓
Respuesta JSON
```

## ¿Qué hace el Router?

En DRF tú haces algo así:

```Python
router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)

urlpatterns = router.urls
```

Ese router es el que hace la magia.

Cuando registras un ViewSet, DRF automáticamente crea rutas como:

```
GET /pacientes/
POST /pacientes/
GET /pacientes/{id}/
PUT /pacientes/{id}/
PATCH /pacientes/{id}/
DELETE /pacientes/{id}/
```

Tú no escribiste esas rutas manualmente.

El router las construye a partir del ViewSet.
