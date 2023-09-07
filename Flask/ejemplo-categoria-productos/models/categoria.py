from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import List
from db import db

@dataclass
class Categoria(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255))
    productos: Mapped[List["Producto"]] = relationship(back_populates="categoria")
    # No importes Producto (no hace falta) para no generar error import circular