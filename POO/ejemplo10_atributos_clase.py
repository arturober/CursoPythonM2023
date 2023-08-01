class Empleado:
    sueldo_minimo = 14000 # atributo de clase

    @classmethod
    def crea_becario(cls, nombre): # Crea empleado con sueldo mínimo
        return cls(nombre, cls.sueldo_minimo)  # Llamo al constructor de la clase

    @staticmethod
    def crea_becario_static(nombre):
        return Empleado(nombre, Empleado.sueldo_minimo)
    
    def __init__(self, nombre, sueldo) -> None:
        self.nombre = nombre
        self.sueldo = sueldo
        
    def __repr__(self) -> str:
        return f"{self.nombre} - {self.sueldo: .2f}"
   
e = Empleado("Pepito", 30000)
print(Empleado.sueldo_minimo)
print(e.sueldo_minimo)

# becario = Empleado("Vanessa", Empleado.sueldo_minimo)
becario = Empleado.crea_becario("Vanessa")
print(becario)
becario2 = Empleado.crea_becario_static("Pedro")
print(becario2)

