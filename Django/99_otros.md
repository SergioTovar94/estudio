## Relaciones entre tablas (MUY importante)

Aquí está la potencia real del ORM.

## ForeignKey

Relación muchos-a-uno.

doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

## OneToOneField

Relación uno-a-uno.

## ManyToManyField

Muchos-a-muchos.

#### ⚙️ 3️⃣ Opciones de campos (Field options)

Todos los campos aceptan parámetros como:

null=True

blank=True

default=

unique=True

db_index=True

choices=

### 🧬 4️⃣ Meta class

Sirve para configurar el modelo.

class Paciente(models.Model):

```Python
    class Meta:
        ordering = ['-fecha_registro']
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
```

### 5️⃣ Managers

Cada modelo tiene un manager por defecto:

Paciente.objects.all()

objects es un Manager.

Puedes crear managers personalizados:

class PacienteManager(models.Manager):
def activos(self):
return self.filter(activo=True)

### 🔍 6️⃣ QuerySet

Cuando haces:

Paciente.objects.all()

Devuelve un QuerySet.

Un QuerySet permite:

.filter()

.exclude()

.get()

.order_by()

.count()

.exists()

.first()

.last()

Es lazy (no ejecuta SQL hasta que lo necesitas).

## django.shortcuts

## django.urls

## django.forms

## django.contrib.auth

## django.contrib.admin

##
