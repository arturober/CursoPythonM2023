from functools import wraps
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric, Boolean
from flask_cors import CORS
from marshmallow import Schema, ValidationError, fields, validate

app = Flask(__name__)
CORS(app)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tareas.db"

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
class Tarea(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descripcion: Mapped[str] = mapped_column(String(255))
    realizada: Mapped[bool] = mapped_column(Boolean())


class TareaSchema(Schema):
    id = fields.Integer() # id es opcional
    descripcion = fields.Str(
        required=True,
        error_messages={
            "required": "La descripción es obligatoria",
            "type": "El campo no tiene un formato de string",
        },
        validate=validate.Length(
            min=6, error="La descripción debe tener al menos 6 letras"
        ),
    )
    realizada = fields.Boolean(
        required=True,
        error_messages={
            "required": "El campo 'realizada' es obligatorio",
            "type": "El campo no es un booleano",
        },
    )

with app.app_context():
    db.create_all()


@app.get("/tareas")
def get_tareas():
    select = db.select(Tarea)
    tareas = db.session().execute(select).scalars().all()
    return jsonify(tareas)


@app.get("/tareas/<int:id>")
def get_tarea(id: int):
    tarea = db.get_or_404(Tarea, id)
    return jsonify(tarea)


@app.post("/tareas")
@validate_json(TareaSchema)
def insert_tarea():
    json = request.json
    tarea = Tarea(descripcion=json["descripcion"], realizada=json["realizada"])
    db.session().add(tarea)
    db.session().commit()
    return jsonify(tarea), 201  # 201 -> Created


@app.put("/tareas/<int:id>")
@validate_json(TareaSchema)
def update_tarea(id: int):
    tarea = db.get_or_404(Tarea, id)
    json = request.json
    tarea.descripcion = json["descripcion"]
    tarea.realizada = json["realizada"]
    db.session().commit()
    return jsonify(tarea)


@app.delete("/tareas/<int:id>")
def delete_tarea(id: int):
    tarea = db.get_or_404(Tarea, id)
    db.session().delete(tarea)
    db.session().commit()
    return "", 204


app.run()
