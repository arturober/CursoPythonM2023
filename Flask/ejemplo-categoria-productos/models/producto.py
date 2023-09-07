from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Numeric
from db import db

@dataclass
class Producto(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255))
    precio: Mapped[float] = mapped_column(Numeric(10, 2))
    imagen: Mapped[str] = mapped_column(String(255))
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categoria.id"))
    categoria: Mapped["Categoria"] = relationship(back_populates="productos")
    # No importes Categoria (no hace falta) para no generar error import circular