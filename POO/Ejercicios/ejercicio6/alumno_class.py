from examen_class import Examen
from dataclasses import dataclass, field

@dataclass
class Alumno:
    nombre: str
    curso: str
    examenes: list[Examen] = field(default_factory=list)
        
    def add_examenes(self, *examen):
        self.examenes.extend(examen)
    
    @property
    def media(self):
        notas = [e.nota for e in self.examenes]
        return sum(notas)/len(notas)
    
    def print_media_asignaturas(self):
        asignaturas = {e.asignatura for e in self.examenes}
        for a in asignaturas:
            notas = [e.nota for e in self.examenes if e.asignatura == a]
            print(f"Media {a}: {sum(notas)/len(notas): .2f} {notas}")
            