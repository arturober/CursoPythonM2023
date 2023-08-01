from examen_class import Examen
from alumno_class import Alumno
    
a = Alumno("Juan", "1BACH")
a.add_examenes(Examen("Lengua", 5.75), Examen("Mates", 6.5))
print(a)
print(f"Nota media: {a.media: .2f}")