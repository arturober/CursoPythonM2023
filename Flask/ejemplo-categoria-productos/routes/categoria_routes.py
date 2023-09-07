from flask import Blueprint, jsonify, request
from db import db
from models import Categoria
from schemas import CategoriaSchema, validate_json, CategoriaConProductosSchema

categorias = Blueprint("categorias", __name__)


@categorias.get("")
def get_categorias():
    select = db.select(Categoria)
    categorias = db.session().execute(select).scalars().all()
    schema = CategoriaSchema(many=True)  # many es que vamos a devolver una lista
    return jsonify(schema.dump(categorias))


@categorias.get("/<int:id>")
def get_categoria(id: int):
    categoria = db.get_or_404(Categoria, id)
    schema = CategoriaConProductosSchema()
    return jsonify(schema.dump(categoria))


@categorias.post("")
@validate_json(CategoriaSchema)
def insert_categoria():
    json = request.json
    categoria = Categoria(nombre=json["nombre"])
    db.session().add(categoria)
    db.session().commit()
    schema = CategoriaSchema()
    return jsonify(schema.dump(categoria)), 201  # 201 -> Created
