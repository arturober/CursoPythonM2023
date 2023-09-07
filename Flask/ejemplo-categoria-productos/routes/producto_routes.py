from flask import Blueprint, jsonify, request
from PIL import Image
import io, base64, os

from db import db
from models import Producto
from schemas import validate_json, ProductoSchema

productos = Blueprint('productos', __name__)

def guarda_imagen(json):
    imagen_str = json["imagen"].split(",")[1] if json["imagen"].startswith("data") else json["imagen"]
    img = Image.open(io.BytesIO(base64.decodebytes(bytes(imagen_str, "utf-8"))))
    ruta = f"imagenes/{json['nombre']}.jpg"
    img.convert('RGB').save(f"{os.path.dirname(__file__)}/../{ruta}")
    return ruta

@productos.get("")
def get_productos():
    select = db.select(Producto)
    productos = db.session().execute(select).scalars().all()
    return jsonify(productos)


@productos.get("/<int:id>")
def get_producto(id: int):
    producto = db.get_or_404(Producto, id)
    return jsonify(producto)


@productos.post("")
@validate_json(ProductoSchema)
def insert_producto():
    json = request.json
    ruta = guarda_imagen(json)

    producto = Producto(nombre=json["nombre"], precio=json["precio"], imagen=request.host_url+ruta)
    db.session().add(producto)
    db.session().commit()
    return jsonify(producto), 201  # 201 -> Created


@productos.put("/<int:id>")
@validate_json(ProductoSchema)
def update_producto(id: int):
    producto = db.get_or_404(Producto, id)
    json = request.json
    if not json["imagen"].startswith("http"): # base64
        ruta = guarda_imagen(json)
        producto.imagen = request.host_url+ruta
    
    producto.nombre = json["nombre"]
    producto.precio = json["precio"]
    db.session().commit()
    return jsonify(producto)


@productos.delete("/<int:id>")
def delete_producto(id: int):
    producto = db.get_or_404(Producto, id)
    db.session().delete(producto)
    db.session().commit()
    return "", 204

