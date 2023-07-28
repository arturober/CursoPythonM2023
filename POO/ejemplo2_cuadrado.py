class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def get_area(self):
        return self.lado ** 2
    
    def __repr__(self) -> str: # Representación string cuadrado
        return f"Cuadrado (lado = {self.lado})" # Llama a __str__
    
    def __add__(self, other): # Sumar 2 cuadrados
        return Cuadrado(self.lado + other.lado)
    
    def __lt__(self, other) -> bool: # Operador <
        return self.lado < other.lado
    
    def __eq__(self, other) -> bool: # Operador ==
        return self.lado == other.lado

c = Cuadrado(12) 
print(type(c)) # <class '__main__.Cuadrado'>
print(f"lado = {c.lado}, area = {c.get_area()}")
print(c)


c2 = Cuadrado(14)
c3 = c + c2

print(c3) # Cuadrado (lado = 22)
print(c > c2)

lista = [c3, c2, c]
lista.sort()
print(lista)


