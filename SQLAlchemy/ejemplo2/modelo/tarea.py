from modelo.basemodel import BaseModel
from sqlalchemy.orm import  Mapped, mapped_column
from sqlalchemy import Boolean, String

class Tarea(BaseModel):
    __tablename__ = "tarea"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descripcion: Mapped[str] = mapped_column(String(255))
    realizada: Mapped[bool] = mapped_column(Boolean(False))
    
    def __repr__(self) -> str:
        return f"{self.id} - {self.descripcion} (Realizada: {'Sí' if self.realizada else 'No'})"
    