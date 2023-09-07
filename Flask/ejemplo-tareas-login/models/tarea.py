from dataclasses import dataclass
from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, Boolean, ForeignKey
from db import db

@dataclass
class Tarea(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descripcion: Mapped[str] = mapped_column(String(255))  
    realizada: Mapped[bool] = mapped_column(Boolean())
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuario.id")) # tabla.columna
    tarea: Mapped["Usuario"] = relationship(back_populates="usuarios")