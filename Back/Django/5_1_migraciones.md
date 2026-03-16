# Migraciones

## Makemigrations

Cuando se hace

```Python
python manage.py makemigrations
```

Django analiza los modelos y genera un archivo en:

```
pacientes/migrations/0001_initial.py
```

Ese archivo contiene instrucciones como:

```Python
migrations.CreateModel(
    name='Paciente',
    fields=[
        ...
    ],
)
```

A eso le llamé “blueprint” (plano de construcción). 📄 Un documento que describe cómo debe verse la tabla en la base de datos.

## Migrate

Construye la tabla

Este formato de separar planos de la ejecución hace que pueda haber un versionado sobre los archivos.
