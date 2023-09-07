from flask import Blueprint, jsonify, request
from db import db
from models import Usuario

auth = Blueprint("auth", __name__)


@auth.post("/login")
def login():
    json = request.json
    select = (
        db.select(Usuario)
        .where(Usuario.email == json["email"])
        .where(Usuario.password == json["password"])
    )
    usuario = db.session().execute(select).scalars().one_or_none()
    if not usuario:
        return {"error": "Usuario y/o contraseña no válidos"}, 401
    return "token"

@auth.post("/registro")
def registro():
    json = request.json
    usuario = Usuario(nombre = json["nombre"], email = json["email"], password = json["password"])
    db.session().add(usuario)
    db.session().commit()
    return "", 204