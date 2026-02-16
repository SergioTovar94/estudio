# Django

Entorno de desarrollo web backend basado en python
Es la primer opción para trabajo en equipos
Django fue desarrollado donde las aplicaciones se creaban con múltiples páginas html
Actualmente necesitan mucha interacción y que el cambio sea rápido. Para eso entonces Django ya no entrega templates o no se usa tanto, sino que entrega archivos Json y el front se encarga de mostrarlos
Si no tienen html ni interfaces son rest apis

## Modulos por defecto en Django

Al momento de crear un proyecto en Django aparecen lo siguientes módulos dentro de la carpeta principal.

### Carpeta **pycache**

Guarda código que ya compiló python para que se ejecute más rápido. Está más relacionado con el funcionamiento de python que Django.

### **init.py**

Le indica a python que la carpeta en la que se encuentra este archivo es un módulo de python.

### settings.py

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

### Admin

Permite que se añada un panel administrador al proyecto.

### Apps

Es el equivalente a settings.py para la aplicación en concreto

### Model

Permite crear clases las cuales se van a convertir en tablas de SQL.

### Test

Permiten escribir testing de nuestras vistas y comprobar lógica.

## Patrón Model View Template

### Serializer

### Route

### ORM

Tiene ORM que es un módulo o paquete que maneja por uno las consultas a base de datos.

Ya viene por defecto y es esencial del framework y se encarga de las migraciones.

### Seguridad

Arquitectura de seguridad robusca contra CSRF, SQL injction, xss

### Django Rest Framework

Hay un modulo Djando Rest Framework, pasar datos a Json, crear un crud completo, asegurar api con JWT fácilmente,
Project, global

App, cada parte, routing

La url viaja al view, el consulta base de datos que es el model y este envía html al front que es el template

Headless cms
