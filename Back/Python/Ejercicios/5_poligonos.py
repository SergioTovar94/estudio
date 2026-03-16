"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""

class Poligono:
    def area(self):
        raise NotImplementedError("Esta función debe ser implementada por la subclase")


class Triangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


class Cuadrado(Poligono):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


class Rectangulo(Poligono):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


# Función única que calcula el área de cualquier polígono
def calcular_area(poligono: Poligono):
    return poligono.area()


# Ejemplos de uso
triangulo = Triangulo(5, 3)
cuadrado = Cuadrado(4)
rectangulo = Rectangulo(6, 2)

print("Área triángulo:", calcular_area(triangulo))
print("Área cuadrado:", calcular_area(cuadrado))
print("Área rectángulo:", calcular_area(rectangulo))
