class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

c = Cuadrado(8) 

print(type(c)) # <class '__main__.Cuadrado'>
print(c.lado)

c2 = Cuadrado(14)
print(c2.lado)
