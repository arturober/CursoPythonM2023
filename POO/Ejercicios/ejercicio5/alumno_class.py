from examen_class import Examen

class Alumno:
    def __init__(self, nombre: str, curso: str) -> None:
        self.__nombre = nombre
        self.curso = curso
        self.__examenes: list[Examen] = []
        
    @property
    def nombre(self):
        return self.__nombre
        
    @property
    def curso(self):
        return self.__curso
    
    @curso.setter
    def curso(self, curso: str):
        if type(curso) != str or curso.strip() == "":
            raise ValueError("El curso no puede estar vacío")
        self.__curso = curso
        
    def add_examenes(self, *examen):
        self.__examenes.extend(examen)
        
    def __repr__(self) -> str:
        cad = f"{self.nombre} - {self.curso}:"
        for e in self.__examenes:
            cad += "\n  - " + str(e)
        return cad
    
    @property
    def media(self):
        notas = [e.nota for e in self.__examenes]
        return sum(notas)/len(notas)
    
    def print_media_asignaturas(self):
        asignaturas = {e.asignatura for e in self.__examenes}
        for a in asignaturas:
            notas = [e.nota for e in self.__examenes if e.asignatura == a]
            print(f"Media {a}: {sum(notas)/len(notas): .2f} {notas}")
            