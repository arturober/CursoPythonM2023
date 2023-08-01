from dataclasses import dataclass

@dataclass
class Examen:
    asignatura: str
    nota: float
    
    aprobado = 5 # Atributo de clase
    