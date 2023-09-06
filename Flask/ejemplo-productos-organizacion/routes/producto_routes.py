from flask import Blueprint, jsonify, request
from db import db
from models import Producto
from schemas import validate_json, ProductoSchema

productos = Blueprint('productos', __name__)

@productos.get("/")
def get_productos():
    select = db.select(Producto)
    productos = db.session().execute(select).scalars().all()
    return jsonify(productos)


@productos.get("/<int:id>")
def get_producto(id: int):
    producto = db.get_or_404(Producto, id)
    return jsonify(producto)


@productos.post("/")
@validate_json(ProductoSchema)
def insert_producto():
    json = request.json
    producto = Producto(nombre=json["nombre"], precio=json["precio"])
    db.session().add(producto)
    db.session().commit()
    return jsonify(producto), 201  # 201 -> Created


@productos.put("/<int:id>")
@validate_json(ProductoSchema)
def update_producto(id: int):
    producto = db.get_or_404(Producto, id)
    json = request.json
    producto.nombre = json["nombre"]
    producto.precio = json["precio"]
    db.session().commit()
    return jsonify(producto)


@productos.delete("/<int:id>")
def delete_producto(id: int):
    producto = db.get_or_404(Producto, id)
    db.session().delete(producto)
    return "", 204

