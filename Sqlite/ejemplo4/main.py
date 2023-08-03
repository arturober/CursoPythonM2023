import sqlite3
import os
from modelo.tarea import Tarea
from dao.tarea_dao import TareaDAO

db = sqlite3.connect(os.path.dirname(__file__) + "/../bbdd/tareas.db")

def crear_tablas(db: sqlite3.Connection):
    cursor = db.cursor()
    create_table_query = """
    DROP TABLE IF EXISTS tarea;

    CREATE TABLE tarea (
        id INTEGER PRIMARY KEY,
        descripcion TEXT,
        realizada INT
    );
    """
    cursor.executescript(
        create_table_query
    )  # Ejecuta 1 o más instrucciones SQL seguidas


def mostrar_tareas(tareaDao: TareaDAO):
    tareas = tareaDao.get_all()
    for t in tareas:
        print(f"{t.id}. {t.descripcion} ({'realizada' if t.realizada else 'no realizada'})")

# crear_tablas(db)

tareaDao = TareaDAO(db)

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
            mostrar_tareas(tareaDao) 
        case 2:
            desc = input("Descripción nueva tarea: ")
            tarea = Tarea(descripcion=desc)
            tareaDao.insert(tarea)
        case 3:
            mostrar_tareas(tareaDao)
            id = int(input("Id de tarea realizada: "))
            tarea = tareaDao.get(id)
            tarea.realizada = True
            tareaDao.update(tarea)
        case 4:
            mostrar_tareas(tareaDao)
            id = int(input("Id de tarea a borrar: "))
            tareaDao.delete(id)

    input("Pulsa enter para continuar...")
    
db.close()
