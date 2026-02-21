# ¿Qué es un ViewSet?

Ahora pensemos en el siguiente problema.

Ya tienes:

- Modelo (estructura de datos)
- Serializer (traducción)

Pero… ¿quién decide qué pasa cuando alguien hace un GET o un POST? Ahí entra el ViewSet.

🔹 En Django tradicional

Tú tendrías que hacer:

- Una vista para listar
- Una vista para crear
- Otra para actualizar
- Otra para borrar

Mucho código repetido.

🔹 En DRF

ModelViewSet es una clase que ya trae todo eso armado:

- .list() → GET lista
- .retrieve() → GET por id
- .create() → POST
- .update() → PUT
- .partial_update() → PATCH
- .destroy() → DELETE

Es como una central de operaciones CRUD.

## Funcionalidades importantes

```Python
from rest_framework import viewsets
from .models import Paciente
from .serializers import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
```

Cuando PacienteViewSet hereda de ModelViewSet, ya trae los métodos (list, retrieve, create, etc.). Pero esos métodos son genéricos. No saben nada de tu modelo Paciente todavía.

Ahí es donde entran:

```Python
queryset = Paciente.objects.all()
serializer_class = PacienteSerializer
```

Vamos a desarmarlo con lógica.

### ¿Qué hace queryset?

El ModelViewSet necesita saber de dónde saca los datos.

Cuando alguien hace:

```
GET /api/pacientes/
```

El método interno .list() hace algo conceptualmente así:

- queryset = self.get_queryset()
- serializer = self.get_serializer(queryset, many=True)
- return Response(serializer.data)

Entonces queryset es la fuente de datos. Es la consulta base que se usará para:

- listar
- buscar por id
- actualizar
- eliminar

Sin queryset, el ViewSet no sabe qué modelo consultar.

### ¿Qué hace serializer_class?

Ahora imagina que ya tengo los objetos Paciente en memoria.

Pero necesito:

- Convertirlos a JSON
- Validar datos cuando hagan POST
- Validar datos cuando hagan PUT/PATCH

El ViewSet no sabe cómo hacer eso. Entonces necesita que tú le digas: ¿Con qué clase traduzco y valido estos datos?

Por eso existe:

serializer_class = PacienteSerializer

Sin eso, el ViewSet no sabría:

- Qué campos exponer
- Cómo validar
- Cómo crear una instancia nueva
