class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = nombre
        
    @property
    def edad(self):
        return self.__edad
        
    @edad.setter
    def edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self.__edad = edad
        
    def __repr__(self) -> str:
        return f"{self.nombre} - {self.edad}"
        
lista = [
    Persona("Pedro", 24),
    Persona("Ana", 6),
    Persona("Marco", 4),
]

for p in lista: p.edad -= 1
    
print(lista)
    
p.nombre = ""
