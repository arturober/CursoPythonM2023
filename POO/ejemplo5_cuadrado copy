'''
Getters y setters estilo Python/C#/JavaScript (propiedades)
__lado -> '__' indica que es un atributo privado y
solo puede ser accedido mediante las propiedades definidas para ello
'''

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
        
    @property # Indica que 'lado' es una propiedad de acceso público (llama a esta función implícitamente)
    def lado(self): # Getter
        return self.__lado
    
    @lado.setter
    def lado(self, lado): # Setter
        if lado <= 0:
            raise ValueError("El cuadrado no puede tener lado negativo")
        self.__lado = lado
       
    @property # Puedo acceder sin los paréntesis 
    def area(self):
        return self.lado ** 2
        
c = Cuadrado(4)
print(f"lado: {c.lado}, área: {c.area}")
c.lado = 25
print(f"lado: {c.lado}, área: {c.area}")


