from examen_class import Examen
from alumno_class import Alumno
    
a = Alumno("Juan", "1BACH")
a.add_examenes(
    Examen("Lengua", 5.75), 
    Examen("Mates", 6.5),
    Examen("Lengua", 8), 
    Examen("Historia", 2.6),
    Examen("Lengua", 7.4), 
    Examen("Historia", 6.5),
    Examen("Historia", 4.75), 
    Examen("Mates", 8)
)
print(a)
a.print_media_asignaturas()
print(f"Nota media: {a.media: .2f}")
a.print_eficiencia()

novato = Alumno.crea_novato("Evaristo")
print(novato)

