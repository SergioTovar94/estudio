# Pasos para crear el proyecto

`python -m venv venv`

`.\venv\Scripts\activate`

`pip install django`

`pip freeze > requirements.txt`

Esto genera un archivo con:

```
Django==5.0.1
asgiref==3.7.2
```

`django-admin startproject nombre-proyecto .`
El . al final permite que se cree todo el proyecto en la carpeta en la que nos encontramos y no
se cree una nueva.

`python manage.py runserver 3000`
Pone a correr el servidor en el puerto 3000

`python manage.py startapp mi-app`
Crea una app dentro del proyecto llamada mi-app

`python manage.py makemigrations`

`python manage.py migrate`

Si es la primer vez que se ejecutan los comandos y no se han creado modelos aparecerán las tablas
y los índices definidos por defecto par django.
