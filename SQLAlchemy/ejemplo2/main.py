from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, Numeric, create_engine, select
from modelo.basemodel import BaseModel
from modelo.tarea import Tarea

engine = create_engine("sqlite:///SQLAlchemy/bbdd/tareas.db") # echo=True activa modo depuración
BaseModel.metadata.create_all(engine)


def mostrar_tareas():
    with Session(engine) as session:
        tareas = session.execute(select(Tarea)).scalars().all()
        for t in tareas:
            print(t)
            
opcion = -1
while opcion != 0:
    print("""MENU
1) Ver tareas
2) Añadir tarea
3) Marcar tarea como realizada
4) Borrar tarea
0) Salir
""")
    opcion = int(input("Elige una opción: "))
    match opcion:
        case 1:
            mostrar_tareas() 
        case 2:
            desc = input("Descripción nueva tarea: ")
            tarea = Tarea(descripcion=desc, realizada=False)
            with Session(engine) as session:
                session.add(tarea)
                session.commit()
        case 3:
            mostrar_tareas()
            id = int(input("Id de tarea realizada: "))
            with Session(engine) as session:
                tarea = session.get(Tarea, id)
                tarea.realizada = True
                session.commit()
        case 4:
            mostrar_tareas()
            id = int(input("Id de tarea a borrar: "))
            with Session(engine) as session:
                tarea = session.get(Tarea, id)
                session.delete(tarea)
                session.commit()

    input("Pulsa enter para continuar...")
    
