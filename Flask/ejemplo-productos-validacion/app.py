from functools import wraps
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric
from marshmallow import Schema, ValidationError, fields, validate

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)


def validate_json(schema):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            try:
                data = request.json
                schema_instance = schema()
                validated_data = schema_instance.load(data)
                request.validated_data = validated_data  # Almacena los datos validados
                return view_func(*args, **kwargs)
            except ValidationError as error:
                return (
                    jsonify(
                        {
                            "error": "Datos de entrada no válidos",
                            "messages": error.messages,
                        }
                    ),
                    400,
                )

        return wrapper

    return decorator


@dataclass
class Producto(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255))
    precio: Mapped[float] = mapped_column(Numeric(10, 2))


class ProductoSchema(Schema):
    nombre = fields.Str(
        required=True,
        error_messages={
            "required": "El nombre es obligatorio",
            "type": "El campo no tiene un formato de string",
        },
        validate=validate.Length(min=4, error="El nombre debe tener al menos 4 letras"),
    )
    precio = fields.Number(
        required=True,
        error_messages={
            "required": "El precio es obligatorio",
            "type": "El campo no tiene un formato numérico",
        },
        validate=validate.Range(min=0, error="El precio no puede ser negativo"),
    )


with app.app_context():
    db.create_all()


@app.get("/productos")
def get_productos():
    select = db.select(Producto)
    productos = db.session().execute(select).scalars().all()
    return jsonify(productos)


@app.get("/productos/<int:id>")
def get_producto(id: int):
    producto = db.get_or_404(Producto, id)
    return jsonify(producto)


@app.post("/productos")
@validate_json(ProductoSchema)
def insert_producto():
    json = request.json
    producto = Producto(nombre=json["nombre"], precio=json["precio"])
    db.session().add(producto)
    db.session().commit()
    return jsonify(producto), 201  # 201 -> Created


@app.put("/productos/<int:id>")
@validate_json(ProductoSchema)
def update_producto(id: int):
    producto = db.get_or_404(Producto, id)
    json = request.json
    producto.nombre = json["nombre"]
    producto.precio = json["precio"]
    db.session().commit()
    return jsonify(producto)


@app.delete("/productos/<int:id>")
def delete_producto(id: int):
    producto = db.get_or_404(Producto, id)
    db.session().delete(producto)
    return "", 204


app.run()
