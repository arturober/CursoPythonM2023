
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        
    def get_area(self):
        return self.ancho * self.alto
    
    def __repr__(self) -> str:
        return f"Rectángulo -> ancho = {self.ancho}, alto = {self.alto}"
    
    def __lt__(self, other):
        return self.get_area() < other.get_area()

r = Rectangulo(4, 6)
print(r)

lista = [r, Rectangulo(7, 2), Rectangulo(12, 9), Rectangulo(2, 2)]
# lista.sort(key = lambda r: r.get_area())
lista.sort() # No hace falta indicar cómo ordenar al estar implementado __lt__
print("Lista ordenada")
for rec in lista:
    print(f"{rec}, área: {rec.get_area()}")