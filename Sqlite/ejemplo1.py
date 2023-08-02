import sqlite3
import os

db = sqlite3.connect(os.path.dirname(__file__) + "/bbdd/productos.db")
cursor = db.cursor()

create_table_query = """
DROP TABLE IF EXISTS producto;

CREATE TABLE producto (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    precio REAL
);
"""

cursor.executescript(create_table_query) # Ejecuta 1 o más instrucciones SQL seguidas

cursor.execute("INSERT INTO producto(nombre, precio) VALUES(?, ?)", ("prueba", 4))
print(cursor.lastrowid) # 1 -> Última clave primaria autogenerada

cursor.executemany( # Inserción múltiple
    "INSERT INTO producto(nombre, precio) VALUES(?, ?)",
    [
        ("Mesa", 90),
        ("Lámpara", 14.5),
        ("Estantería", 90),
    ],
)

cursor.execute(
    "UPDATE producto SET nombre = ?, precio = ? WHERE id = ?",
    ("Modificado", 99, 1)
)
cursor.execute(
    "UPDATE producto SET precio = precio * 2 WHERE id = ?",
    (2,)
)
cursor.execute("DELETE FROM producto WHERE id = ?", (4,))

db.commit() # Guardar últimos cambios

productos = cursor.execute("SELECT * FROM producto").fetchall()
print(productos)

producto = cursor.execute("SELECT * FROM producto WHERE id = ?", (2,)).fetchone()
print(producto)

db.close()