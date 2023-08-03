import sqlite3
import os
from modelo.producto import Producto
from dao.producto_dao import ProductoDao

db = sqlite3.connect(os.path.dirname(__file__) + "/../bbdd/productos.db")

productoDao = ProductoDao(db)

productos = productoDao.get_all()
print(productos)

producto = productoDao.get(1)
print(producto)

# pInsert = Producto(nombre = "Insert", precio = 100)
# productoDao.insert(pInsert)
# print(pInsert)

# producto.nombre = "Otra modificación"
# producto.precio = 1
# productoDao.update(producto)

# productoDao.delete(4)
