# Núcleo de Django

## django.db (Base de datos)

### models

Model es la clase base. Convierte la clase que herede de ella en una tabla de base de datos.

Una clase, por ejemplo, pacientes, hereda de models.Model

Una class Meta permite realizar la metaconfiguración del modelo, por ejemplo como se llama una variable en singular y plural o como se ordena lo que exponga la tabla.

Siempre que se agregue una app, en el settings principal del proyecto debe agregarse dicha app en installed apps
