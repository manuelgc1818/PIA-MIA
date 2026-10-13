#E4.5 · Clase abstracta Figura con area() y perimetro();
#implementa Circulo, Rectangulo y Cuadrado.

from abc import ABC, abstractmethod

from math import pi

class Figura(ABC):
    @abstractmethod
    def perimetro(self):
        ...

    @abstractmethod
    def area(self):
        ...

class Circulo(Figura):

    def __init__(self, radio):

        self.radio = radio

    def area(self):

        return pi * self.radio ** 2

    def perimetro(self):

        return 2 * pi * self.radio      

class Rectangulo(Figura):

    def __init__(self, lado1, lado2):

        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):

        return self.lado1 * self.lado2

    def perimetro(self):

        return 2 * (self.lado1 + self.lado2)

class Cuadrado(Figura):

    def __init__(self, lado):

        self.lado = lado

    def area(self):

        return self.lado ** 2

    def perimetro(self):

        return 4 * self.lado

cuadrado = Cuadrado(4)
print(cuadrado.area())
print(cuadrado.perimetro())
rectangulo = Rectangulo(4, 5)
print(rectangulo.area())
print(rectangulo.perimetro())
circulo = Circulo(3)
print(circulo.area())
print(circulo.perimetro())