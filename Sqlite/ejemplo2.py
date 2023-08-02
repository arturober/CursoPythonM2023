import sqlite3
import os

db = sqlite3.connect(os.path.dirname(__file__) + "/bbdd/tareas.db")


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


def mostrar_tareas(db: sqlite3.Connection):
    cursor = db.cursor()
    tareas = cursor.execute("SELECT * FROM tarea").fetchall()
    for t in tareas:
        print(f"{t[0]}. {t[1]} ({'realizada' if t[2] else 'no realizada'})")


def add_tarea(db: sqlite3.Connection):
    cursor = db.cursor()
    desc = input("Descripción nueva tarea: ")
    cursor.execute("INSERT INTO tarea(descripcion, realizada) VALUES(?, 0)", (desc,))
    db.commit()


def realiza_tarea(db: sqlite3.Connection):
    mostrar_tareas(db)
    id = int(input("Id de tarea realizada: "))
    cursor = db.cursor()
    cursor.execute("UPDATE tarea SET realizada = 1 WHERE id = ?", (id,))
    db.commit()


def borra_tarea(db: sqlite3.Connection):
    mostrar_tareas(db)
    id = int(input("Id de tarea a borrar: "))
    cursor = db.cursor()
    cursor.execute("DELETE FROM tarea WHERE id = ?", (id,))
    db.commit()


# crear_tablas(db)

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
           mostrar_tareas(db) 
        case 2:
            add_tarea(db)
        case 3:
            realiza_tarea(db)
        case 4:
            borra_tarea(db)

    input("Pulsa enter para continuar...")
    
db.close()
