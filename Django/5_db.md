# ¿Qué base de datos viene por defecto en Django?

La base de datos preconfigurada es:

SQLite

Es un archivo local, algo como:

```
db.sqlite3
```

## ¿Dónde se configura?

En settings.py.

Ahí verás algo como:

```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Eso indica:

- Motor: SQLite
- Archivo físico: db.sqlite3

## Django usa un ORM.

Eso significa que tu modelo:

```Python
class Paciente(models.Model):
```

Es independiente del motor de base de datos.

Puedes cambiar SQLite por PostgreSQL o MySQL sin cambiar tu modelo. Eso es una gran ventaja arquitectónica.
