# tipos de campos

Son los que definen las columnas de la tabla.

## Parámetros comunes (casi todos los campos)

Estos los puedes usar en prácticamente cualquier tipo de campo:

```Python
null=True          # Permite NULL en base de datos
blank=True         # Permite vacío en formularios
default=valor      # Valor por defecto
unique=True        # Valor único
db_index=True      # Crea índice en BD
verbose_name="..."
help_text="..."
editable=False     # No aparece en admin
```

## Campos de texto

### CharField(max_length=...)

Obligatoriamente necesita:

max_length=100

Eso define el tamaño máximo en la base de datos.

### TextField()

### EmailField()

### SlugField()

### URLField()

## Campos numéricos

### IntegerField()

### FloatField()

### DecimalField(max_digits=, decimal_places=)

Necesita:

max_digits=10
decimal_places=2

### PositiveIntegerField()

## Campos de fecha y tiempo

### DateField()

### DateTimeField()

Puede usar:

auto_now=True
auto_now_add=True

### TimeField()

## Campos booleanos

### BooleanField()
