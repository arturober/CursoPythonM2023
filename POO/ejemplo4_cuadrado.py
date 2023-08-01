'''
Getters y setters estilo Java
__lado -> '__' indica que es un atributo privado y
solo puede ser accedido mediante los métodos get y set
'''

class Cuadrado:
    def __init__(self, lado):
        self.set_lado(lado)
        
    def get_lado(self): # Getter
        return self.__lado
    
    def set_lado(self, lado): # Setter
        if lado <= 0:
            raise ValueError("El cuadrado no puede tener lado negativo")
        self.__lado = lado
        
c = Cuadrado(4)
c.set_lado(c.get_lado() - 20) # ValueError: El cuadrado no puede tener lado negativo
print(c.get_lado())
