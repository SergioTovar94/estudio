¿Qué es un Manager?

Muy buena pregunta 👌

Un Manager es el objeto que permite consultar la base de datos.

Cuando haces:

Paciente.objects.all()

👉 objects es un Manager.

¿Qué hace un Manager?

Es el punto de entrada al ORM.

Devuelve QuerySets:

Paciente.objects.filter(nombre="Juan")
Paciente.objects.get(id=1)
Paciente.objects.create(nombre="Carlos")
Manager personalizado

Puedes crear uno propio:

class PacienteManager(models.Manager):
def activos(self):
return self.filter(activo=True)
