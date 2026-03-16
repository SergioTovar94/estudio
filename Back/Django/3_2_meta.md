# Meta

Dentro del modelo:

class Meta:

Se usa para configuración interna.

Las más importantes:
📌 ordering
ordering = ['-fecha_creacion']

Orden por defecto.

📌 verbose_name
verbose_name = "Paciente"
verbose_name_plural = "Pacientes"
📌 db_table
db_table = "tabla_pacientes"

Nombre personalizado en la base de datos.

📌 constraints
constraints = [
models.UniqueConstraint(
fields=['email'],
name='unique_email'
)
]
📌 indexes
indexes = [
models.Index(fields=['apellido']),
]
📌 abstract = True

Convierte el modelo en base para herencia (no crea tabla).
