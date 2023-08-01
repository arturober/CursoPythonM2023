from examen_class import Examen
from dataclasses import dataclass, field

@dataclass
class Alumno:
    nombre: str
    curso: str
    examenes: list[Examen] = field(default_factory=list)
    
    @staticmethod
    def crea_novato(nombre: str):
        return Alumno(nombre, '1ESO')
        
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
            
    def print_eficiencia(self):
        num_aprobados = len([e for e in self.examenes if e.nota >= Examen.aprobado])
        print(f"Exámenes aprobados: {num_aprobados}")
        print(f"Exámenes suspensos: {len(self.examenes) - num_aprobados}")
        print(f"Porcentaje aprobado: {num_aprobados*100/len(self.examenes): .2f}%")
            