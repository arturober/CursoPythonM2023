from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Numeric, create_engine

class BaseModel(DeclarativeBase):
    pass

class Producto(BaseModel):
    __tablename__ = "producto"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255))
    precio: Mapped[float] = mapped_column(Numeric(10, 2))
    
    def __repr__(self) -> str:
        return f"{self.id} - {self.nombre} ({self.precio: .2f})"
    
engine = create_engine("sqlite:///SQLAlchemy/bbdd/datos.db", echo=True) # echo=True activa modo depuración
BaseModel.metadata.create_all(engine)
    

    