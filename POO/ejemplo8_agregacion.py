class Direccion:
    def __init__(self, calle: str, numero: int, cp: str) -> None:
        self.calle = calle
        self.numero = numero
        self.cp = cp
        
    def __repr__(self) -> str:
        return f"{self.calle}, Núm: {self.numero}, CP: {self.cp}"

class Persona:
    def __init__(self, nombre: str, edad: int, direccion: Direccion) -> None:
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        
    def __repr__(self) -> str:
        return f"{self.nombre} ({self.edad}). Dirección: {self.direccion}"
    
dir = Direccion("Calle perdida", 23, "02434")
p = Persona("Ana", 39, dir)

print(p)