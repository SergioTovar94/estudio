# Clases

Las clases permiten realizar una abstracción. Una clase puede tener variables que hacen referencias a características
de esta, también puede tener métodos que harían referencia a funcionalidades de la clase.

## Ejemplo de Clase y Constructor

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

# Crear una instancia de la clase
persona1 = Persona("Juan", 30)
persona1.saludar()  # Salida: Hola, me llamo Juan y tengo 30 años
```

Tienen un método constructor que es definido mediante **init**

En parámetro self es una palabra reserevada en python y hace las veces de this en java. Permite indicar que se hace referencia a
este objeto.

## Encapsulamiento

### Encapsulamiento de variables

Cuando se usan dos guiones al piso antes del nombre de una variable esta queda encapsulada y no puede ser accedida desde el exterior.
Así, la forma para acceder a estos datos encapsulados será mediante métodos definidos para la clase.

### Ejemplo de Encapsulamiento de variables

```python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Variable encapsulada

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def obtener_saldo(self):
        return self.__saldo

# Uso
cuenta = CuentaBancaria("Juan", 1000)
print(cuenta.obtener_saldo())  # Salida: 1000
cuenta.depositar(500)
print(cuenta.obtener_saldo())  # Salida: 1500
# print(cuenta.__saldo)  # Error: AttributeError
```

### Encapsulamiento de funciones

En este caso, los métodos encapsulados también son definidos con dos guiones al piso antes del nombre de esta y solo podrán ser accesibles
por otros métodos dentro de la clase.

### Ejemplo de Encapsulamiento de métodos

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __aplicar_descuento(self):  # Método encapsulado
        return self.precio * 0.9

    def obtener_precio_final(self, aplicar_desc):
        if aplicar_desc:
            return self.__aplicar_descuento()
        return self.precio

# Uso
producto = Producto("Laptop", 1000)
print(producto.obtener_precio_final(False))  # Salida: 1000
print(producto.obtener_precio_final(True))   # Salida: 900.0
# producto.__aplicar_descuento()  # Error: AttributeError
```

## str

Cuando se imprime un objeto por consola en python, lo que queda impreso no es totalmente entendible. La forma para devolver
algo que sea más entendible es a través del uso de la función **str** dentro de la clase. Allí va a poderse defir lo que se debería
devolver cuando se llame al objeto y no a una de sus variables o métodos.

### Ejemplo de **str**

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}, {self.edad} años"

# Uso
persona = Persona("María", 25)
print(persona)  # Salida: Persona: María, 25 años
```

Otro ejemplo más complejo:

```python
class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __str__(self):
        return f"Coche {self.marca} {self.modelo} ({self.año})"

# Uso
coche = Coche("Toyota", "Corolla", 2020)
print(coche)  # Salida: Coche Toyota Corolla (2020)
```

## Herencia

Para que una clase herede de otra debemos pasar dentro de los paréntesis de su definición la clase padre.
En caso dado de que se haya sobreescrito el constructor o un método de la clase padre en la clase hija será necesario
hacer uso de super() para acceder a dicho método.

### Ejemplo de Herencia con Constructor

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)  # Llamar al constructor de la clase padre
        self.matricula = matricula

    def estudiar(self):
        print(f"{self.nombre} está estudiando con matrícula {self.matricula}")

# Uso
estudiante = Estudiante("Carlos", 20, "2024001")
estudiante.saludar()  # Salida: Hola, me llamo Carlos y tengo 20 años
estudiante.estudiar()  # Salida: Carlos está estudiando con matrícula 2024001
```

En este ejemplo, la clase `Estudiante` hereda de `Persona`. El constructor de `Estudiante` utiliza `super().__init__()`
para llamar al constructor de la clase padre y inicializar los atributos `nombre` y `edad`, además de agregar el atributo
específico `matricula`. La clase hija también hereda el método `saludar()` de la clase padre.

### Sobreescritura de métodos

Una clase hija puede redefinir un método de la clase padre nombrandola de la misma forma. Por principio de especificación, al acceder al método siempre llamará al método de la clase más específica, esto es la hija. Si se desea acceder al método de la clase padre es necesario usar la palabra reservada super()

### Ejemplo de Sobreescritura de métodos

```python
class Animal:
    def hacer_sonido(self):
        print("Sonido genérico de animal")

class Perro(Animal):
    def hacer_sonido(self):  # Sobreescritura del método
        print("Guau guau")

class Gato(Animal):
    def hacer_sonido(self):  # Sobreescritura del método
        print("Miau miau")

# Uso
animal = Animal()
animal.hacer_sonido()  # Salida: Sonido genérico de animal

perro = Perro()
perro.hacer_sonido()  # Salida: Guau guau

gato = Gato()
gato.hacer_sonido()  # Salida: Miau miau
```

Ejemplo con super() para acceder al método de la clase padre:

```python
class Vehiculo:
    def info(self):
        print("Este es un vehículo")

class Coche(Vehiculo):
    def info(self):  # Sobreescritura del método
        super().info()  # Llamar al método de la clase padre
        print("Este es un coche")

# Uso
coche = Coche()
coche.info()
# Salida:
# Este es un vehículo
# Este es un coche
```

### Herencia múltiple

Una clase puede heredar de más de una clase agregandolas en los paréntesis de la definición de esta. En el momendo de instanciar un objeto de dicha clase, python pedirá que sean ingresados los valores que pide el constructor de la primer clase padre referenciada.

### Polimorfismo

Poli hace referencia a muchas y morfos a formas. Es decir, polimorismo puede entenderse como muchas formas.

### Ejemplo de Polimorfismo

```python
class Forma:
    def area(self):
        pass

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Uso
formas = [Cuadrado(5), Circulo(3), Rectangulo(4, 6)]

for forma in formas:
    print(f"Área: {forma.area()}")
# Salida:
# Área: 25
# Área: 28.27435
# Área: 24
```

En este ejemplo, cada clase hija (`Cuadrado`, `Circulo`, `Rectangulo`) hereda de `Forma` e implementa su propio método `area()`.
Aunque cada clase tiene una implementación diferente del método, se puede llamar al mismo método sobre objetos de diferentes tipos
y cada uno realiza su propia versión. Esto es polimorfismo: la capacidad de usar un mismo nombre de método de diferentes formas.
