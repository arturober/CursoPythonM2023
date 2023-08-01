# Clase base
class Empleado:  # No usaremos propiedades (@property) para simplificar
    def __init__(self, nombre, sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo

    def sube_sueldo(self, porcentaje):
        self.sueldo *= 1 + porcentaje / 100
        
    def __repr__(self) -> str:
        return f"{self.nombre}. Sueldo: {self.sueldo: .2f}"


# Clase derivada
class Programador(Empleado):
    def __init__(self, nombre, sueldo, lenguaje) -> None:
        super().__init__(nombre, sueldo) # Llamamos constructor de Empleado
        self.lenguaje = lenguaje
    
    # Método sobrescrito
    def sube_sueldo(self, porcentaje: float):
        super().sube_sueldo(porcentaje) # Llamamos al método heredado original
        if self.lenguaje == "Python":
            print("El programador de Python sube un 5% extra")
            self.sueldo *= 1.05

    def __repr__(self) -> str:
        return super().__repr__() + ". Lenguaje: " + self.lenguaje

p = Programador("Paco", 20000, "Python")
p.sube_sueldo(5)
print(p.sueldo)  # 21000.0
print(p)

e = Empleado("Pepe", 20000)
e.sube_sueldo(5)
print(e)