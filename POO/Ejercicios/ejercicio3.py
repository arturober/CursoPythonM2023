class Examen:
    def __init__(self, asignatura: str, nota: float) -> None:
        self.__asignatura = asignatura
        self.nota = nota
        
    @property
    def asignatura(self):
        return self.__asignatura
    
    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, nota):
        if(nota < 0 or nota > 10):
            raise ValueError("La nota tiene que estar entre 0 y 10")
        self.__nota = nota
    
    def __repr__(self) -> str:
        return f"{self.asignatura} ({self.nota})"
    
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
    
a = Alumno("Juan", "1BACH")
a.add_examenes(Examen("Lengua", 5.75), Examen("Mates", 6.5))
a.curso = "" # ValueError: El curso no puede estar vacío
