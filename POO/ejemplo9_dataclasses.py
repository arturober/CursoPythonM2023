from dataclasses import dataclass

@dataclass
class Direccion:
    calle: str
    numero: int
    cp: str

@dataclass
class Persona:
    nombre: str
    edad: int
    direccion: Direccion
    
    def hola(self): # Se pueden seguir definiendo métodos con normalidad
        print(f"Hola!. Me llamo {self.nombre}")

    
dir = Direccion("Calle perdida", 23, "02434")
p = Persona("Ana", 39, dir)
p2 = Persona("Ana", 39, dir)

print(p)
p.hola()
