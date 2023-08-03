from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, Numeric, create_engine, select

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

def add_productos():
    silla = Producto(nombre = "Silla", precio = 25)
    mesa = Producto(nombre = "Mesa", precio = 99.95)
    estanteria = Producto(nombre = "Estantería", precio = 60.5) 

    # expire_on_commit=False -> Permite acceder a los objetos fuera de la sesión
    with Session(engine, expire_on_commit=False) as session:
        session.add(silla)
        session.add_all([mesa, estanteria])
        session.commit()
        
    print(silla, mesa, estanteria)
    
def mostrar_productos():
    with Session(engine) as session:
        st = select(Producto) # Select * from producto
        productos = session.execute(st).scalars().all()
        print(productos)
        
        st2 = select(Producto).where(Producto.precio > 50)
        productos2 = session.execute(st2).scalars().all()
        print(productos2)
        
        st3 = select(Producto).where(Producto.id == 1)
        producto = session.execute(st3).scalars().one()
        print(producto)
        
        producto2 = session.get(Producto, 2) # Producto con id 2 (Clave Primaria)
        print(producto2)
        
def modificar_productos():
    with Session(engine) as session:
        producto = session.get(Producto, 3)
        producto.nombre = "Modificado 2"
        producto.precio = 11
        session.commit()
        
def borrar_producto():
    with Session(engine) as session:
        producto = session.get(Producto, 3)
        session.delete(producto)
        session.commit()
    
# add_productos()
# mostrar_productos()
# modificar_productos()
borrar_producto()

    