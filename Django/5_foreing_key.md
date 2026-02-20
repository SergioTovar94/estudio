# ¿Cómo se usa la llave foránea?

La ForeignKey representa:

“Muchos registros apuntan a uno”.

Ejemplo real hospital:

class Doctor(models.Model):
nombre = models.CharField(max_length=100)

class Paciente(models.Model):
nombre = models.CharField(max_length=100)
doctor = models.ForeignKey(
Doctor,
on_delete=models.CASCADE,
related_name='pacientes'
)

## ¿Qué significa on_delete?

Define qué pasa si el Doctor se elimina.

Opciones comunes:

CASCADE → elimina también los pacientes

PROTECT → no deja eliminar

SET_NULL → pone NULL

SET_DEFAULT
