# Modulos por defecto en Django

Al momento de crear un proyecto en Django aparecen lo siguientes módulos dentro de la carpeta principal.

## Carpeta **pycache**

Guarda código que ya compiló python para que se ejecute más rápido. Está más relacionado con el funcionamiento de python que Django.

## **init.py**

Le indica a python que la carpeta en la que se encuentra este archivo es un módulo de python.

## settings.py

Es el archivo de configuración de todo el proyecto. Por defecto ya tiene varias variables definidas.

ALLOWED_HOST = []

Le permite al servidor web decirle qué direcciones tiene permitido consultar al consultar

DEBUG = True

Es para decirle a la aplicación si estamos en modo desarrollo o en producción.

SECRET_KEY

Sirve para django lo utilice como una forma de poder mejorar un poco la encriptación de los usuarios o generar datos que puede compartir entre el navegador y el servidor.

BASE_DIR

Sirve para indicar donde están los directorios que contiene el proyecto.

INSTALLED_APPS

Django permite dividir un proyecto en múltiples apps o partes.

MIDDLEWARE

Es para indicarle a Django si va a procesar determinado tipo de datos de alguna forma.

TEMPLATES

WSGI_APLICATION

DATABASES
Indica a qué base de datos estamos conectados. Por defecto aparece SQLite3. También indica donde está la base de datos

### urls.py

Se ecriben las urls que los usuarios pueden visitar

## Apps

### view.py

Se considera el archivo principal. Es el que indica qué vamos a querer ejecutar o enviar al navegador para que lo pueda mostrar en pantalla.

### migrations: carpeta

Se va a ir llenando cuando se modifique la base de datos. En Django no se requiere la realización de consultas SQL ya que viene con
un modulo llamado ORM el cuál permitirá interactuar con la base datos a través de python. Sin embargo, de ser requerido, también es permitido usar SQL.
