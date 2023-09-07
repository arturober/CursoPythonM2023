from flask import Blueprint, jsonify, request
from db import db
from models import Categoria
from schemas import CategoriaSchema, validate_json

categorias = Blueprint('categorias', __name__)

@categorias.get("")
def get_categorias():
    select = db.select(Categoria)
    categorias = db.session().execute(select).scalars().all()
    return jsonify(categorias)

@categorias.get("/<int:id>")
def get_categoria(id: int):
    categoria = db.get_or_404(Categoria, id)
    return jsonify(categoria)

@categorias.post("")
@validate_json(CategoriaSchema)
def insert_categoria():
    json = request.json
    categoria = Categoria(nombre=json["nombre"])
    db.session().add(categoria)
    db.session().commit()
    return jsonify(categoria), 201  # 201 -> Created
