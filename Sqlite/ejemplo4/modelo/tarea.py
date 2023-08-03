from dataclasses import dataclass

@dataclass
class Tarea:
    id: int = 0
    descripcion: str = None
    realizada: bool = False
    