# Ejemplo clases abstractas
from abc import ABC, abstractclassmethod
import math

class Figura(ABC): # Clase abstracta
    @abstractclassmethod
    def get_area(self): # Método abstracto
        pass
    
    @abstractclassmethod 
    def get_perimetro(self): # Método abstracto
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto) -> None:
        self.ancho = ancho
        self.alto = alto
        
    def get_area(self):
        return self.ancho * self.alto
    
    def get_perimetro(self): # Método abstracto
        return self.ancho * 2 + self.alto * 2

class Circulo(Figura):
    def __init__(self, radio) -> None:
        self.radio = radio
        
    def get_area(self):
        return math.pi * self.radio ** 2
    
    def get_perimetro(self): # Método abstracto
        return math.pi * self.radio * 2
        
#figura = Figura() # TypeError: Can't instantiate abstract class Figura with abstract methods get_area, get_perimetro

rect = Rectangulo(4, 6)
print(rect.get_area()) # 24
print(rect.get_perimetro()) # 20

circulo = Circulo(4)
print(circulo.get_area()) # 50.26
print(circulo.get_perimetro()) # 25.13

