# Principios SOLID

SOLID hace referencia a 5 principios base de la programación orientada a objetos. Cada letra hace referencia a un principio.

| Principio | Nombre Completo                                                   | Descripción                                                                                                                                                                  |
| --------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **S**     | Single Responsibility Principle (SRP - Responsabilidad Única)     | Una clase debe tener una sola razón para cambiar, es decir, debe realizar una sola tarea o tener una única responsabilidad.                                                  |
| **O**     | Open/Closed Principle (OCP - Abierto/Cerrado)                     | Las entidades de software (clases, módulos, funciones) deben estar abiertas para su extensión, pero cerradas para su modificación.                                           |
| **L**     | Liskov Substitution Principle (LSP - Sustitución de Liskov)       | Los objetos de una subclase deben poder reemplazar a los objetos de la clase base sin alterar el correcto funcionamiento del sistema.                                        |
| **I**     | Interface Segregation Principle (ISP - Segregación de Interfaces) | Es mejor tener muchas interfaces específicas que una sola interfaz de propósito general. Los clientes no deben depender de interfaces que no utilizan.                       |
| **D**     | Dependency Inversion Principle (DIP - Inversión de Dependencias)  | Se debe depender de abstracciones (interfaces o clases abstractas) en lugar de implementaciones concretas. Los módulos de alto nivel no deben depender de los de bajo nivel. |

## Ejemplos en Python

### S - Single Responsibility Principle

```python
# ❌ Mal: La clase tiene múltiples responsabilidades
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def guardar_en_bd(self):
        # Responsabilidad 1: Persistencia
        pass

    def enviar_email(self):
        # Responsabilidad 2: Envío de emails
        pass

# ✅ Bien: Cada clase tiene una única responsabilidad
class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class RepositorioUsuario:
    def guardar(self, usuario):
        # Solo responsable de persistencia
        pass

class ServicioEmail:
    def enviar(self, usuario):
        # Solo responsable de envío de emails
        pass
```

### O - Open/Closed Principle

```python
# ❌ Mal: Cerrado a extensión, debe modificar la clase
class Descuento:
    def calcular(self, tipo_cliente, monto):
        if tipo_cliente == "regular":
            return monto * 0.05
        elif tipo_cliente == "vip":
            return monto * 0.10
        elif tipo_cliente == "super_vip":
            return monto * 0.15

# ✅ Bien: Abierto a extensión, cerrado a modificación
from abc import ABC, abstractmethod

class Descuento(ABC):
    @abstractmethod
    def calcular(self, monto):
        pass

class DescuentoRegular(Descuento):
    def calcular(self, monto):
        return monto * 0.05

class DescuentoVIP(Descuento):
    def calcular(self, monto):
        return monto * 0.10

class DescuentoSuperVIP(Descuento):
    def calcular(self, monto):
        return monto * 0.15
```

### L - Liskov Substitution Principle

```python
# ❌ Mal: La subclase viola el contrato de la clase base
class Ave:
    def volar(self):
        return "Volando..."

class Aguila(Ave):
    def volar(self):
        return "Aguila volando alto..."

class Pinguino(Ave):
    def volar(self):
        raise Exception("Los pingüinos no pueden volar")

# ✅ Bien: Las subclases respetan el contrato
class Ave(ABC):
    @abstractmethod
    def moverse(self):
        pass

class AveVoladora(Ave):
    def moverse(self):
        return "Volando..."

class Aguila(AveVoladora):
    def moverse(self):
        return "Aguila volando alto..."

class Pinguino(Ave):
    def moverse(self):
        return "Nadando..."
```

### I - Interface Segregation Principle

```python
# ❌ Mal: Interfaz muy general con métodos que no todos usan
class Dispositivo:
    def encender(self):
        pass

    def apagar(self):
        pass

    def imprimir(self):
        pass

class Impresora(Dispositivo):
    def encender(self):
        pass

    def apagar(self):
        pass

    def imprimir(self):
        print("Imprimiendo...")

class Ventilador(Dispositivo):
    def encender(self):
        pass

    def apagar(self):
        pass

    def imprimir(self):
        # No debería implementar esto
        pass

# ✅ Bien: Interfaces específicas
class Encendible(ABC):
    @abstractmethod
    def encender(self):
        pass

class Apagable(ABC):
    @abstractmethod
    def apagar(self):
        pass

class Imprimible(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Impresora(Encendible, Apagable, Imprimible):
    def encender(self):
        pass

    def apagar(self):
        pass

    def imprimir(self):
        print("Imprimiendo...")

class Ventilador(Encendible, Apagable):
    def encender(self):
        pass

    def apagar(self):
        pass
```

### D - Dependency Inversion Principle

```python
# ❌ Mal: La clase depende de implementaciones concretas
class ServicioPago:
    def __init__(self):
        self.servicio_tarjeta = ServicioTarjetaCredito()

    def procesar_pago(self, monto):
        return self.servicio_tarjeta.pagar(monto)

class ServicioTarjetaCredito:
    def pagar(self, monto):
        print(f"Pagando {monto} con tarjeta")

# ✅ Bien: La clase depende de abstracciones
from abc import ABC, abstractmethod

class ProcesadorPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass

class ServicioTarjetaCredito(ProcesadorPago):
    def pagar(self, monto):
        print(f"Pagando {monto} con tarjeta")

class ServicioPayPal(ProcesadorPago):
    def pagar(self, monto):
        print(f"Pagando {monto} con PayPal")

class ServicioPago:
    def __init__(self, procesador_pago: ProcesadorPago):
        self.procesador_pago = procesador_pago

    def procesar_pago(self, monto):
        return self.procesador_pago.pagar(monto)
```
