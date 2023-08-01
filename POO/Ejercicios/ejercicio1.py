class Examen:
    def __init__(self, asignatura: str, nota: float) -> None:
        self.asignatura = asignatura
        self.nota = nota
    
    def __repr__(self) -> str:
        return f"{self.asignatura} ({self.nota})"
    
ex1 = Examen("Lengua", 5.75)
ex2 = Examen("Mates", 7.6)
ex3 = Examen("Historia", 4)
ex4 = Examen("Biología", 9.25)

print(ex1, ex2, ex3, ex4)