# Pasos para crear el proyecto

## Se crea el entorno virtual y se activa

`python -m venv venv`

`.\venv\Scripts\activate`

## Se instalan las dependencias necesarias

`pip install django`
Habilita models, ORM, vistas.

`pip install djangorestframework`
Habilita mejor manejo de URL, serializers, autenticación, permisos avanzados

`pip install django-cors-headers`
CORS significa Cross-Origin Resource Sharing.
Esta librería le dice al navegador:

"Está permitido que este frontend haga peticiones a este backend".

## Se crea el requirements

`pip freeze > requirements.txt`

Esto genera un archivo con:

```
Django==5.0.1
asgiref==3.7.2
```

## Creación del proyecto

`django-admin startproject nombre-proyecto .`
El . al final permite que se cree todo el proyecto en la carpeta en la que nos encontramos y no
se cree una nueva.

Registrar 'rest_framework' y 'corsheaders', en installed apps y cors en middleware

```Python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'corsheaders',
    'rest_framework',
]
```

```Python
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # debe ir al inicio
    ...,
]
```

```Python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
```

CORS_ALLOWED_ORIGINS le dice a Django qué orígenes (dominios + puertos) pueden hacer peticiones a tu API.

## Crear app

Crea una app dentro del proyecto llamada mi-app
`python manage.py startapp mi-app`

Registrar la app en settings.py

```Python
INSTALLED_APPS = [...
'pacientes',
```

## Modelo

```Python
from django.db import models

# Create your models here.
class Paciente(models.Model):
    """Modelo para pacientes
    """
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

```

Se crea la clase que hereda de models
Se le crean sus atributos

## Serializer

```Python
from rest_framework import serializers
from .models import Paciente

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
```

La clase, al heredar de ModelSerializer, va a poder hacer traducción de sus datos a JSON.
Se le indica a la meta descripción que el modelo es paciente y que puede entregar todos los objetos.

## Viewsets

```Python
from rest_framework import viewsets
from .models import Paciente
from .serializers import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all() # pylint: disable=no-member
    serializer_class = PacienteSerializer
```

Cuando PacienteViewSet hereda de ModelViewSet, ya trae los métodos (list, retrieve, create, etc.). Pero esos métodos son genéricos. No saben nada de tu modelo Paciente todavía.

El query set sabe de donde sacar los datos con el modelo. Y como traducirlos con el serializer.

## Configuración de urls

### Dentro de la app se crea el arcivos urls.py

```Python
from rest_framework.routers import DefaultRouter
from .views import PacienteViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)

urlpatterns = router.urls
```

Aquí el router hace la magia. Cuando se hace el register se crean todas las rutas.

### En urls del config

En Django, el urls.py de una app siempre espera:

El router de DRF tiene un atributo mágico urls que es una lista de objetos de URL ya construidos.
Así que en vez de escribir cada path manualmente, haces:

urlpatterns = router.urls

Eso le dice a Django:

“Aquí están todas las rutas generadas por el router. Solo inclúyelas en el proyecto.”

```Python
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
]
```

Todo lo que empiece con /api/ lo manejan las rutas definidas en pacientes/urls.py

`python manage.py makemigrations`
`python manage.py migrate`

Si es la primer vez que se ejecutan los comandos y no se han creado modelos aparecerán las tablas
y los índices definidos por defecto par django.
