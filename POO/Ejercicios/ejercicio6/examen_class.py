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