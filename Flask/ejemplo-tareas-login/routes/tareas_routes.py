from flask import Blueprint, jsonify, request
from db import db
from models import Tarea

tareas = Blueprint('tareas', __name__)

@tareas.get('')
def get_tareas():
    select = db.select(Tarea)
    tareas = db.session().execute(select).scalars().all()
    return jsonify(tareas)

@tareas.get('/<int:id>')
def get_tarea(id: int):
    tarea = db.get_or_404(Tarea, id)
    return jsonify(tarea)

@tareas.post('')
def insert_tarea():
    json = request.json
    tarea = Tarea(descripcion=json["descripcion"], realizada=json["realizada"])
    db.session().add(tarea)
    db.session().commit()
    return jsonify(tarea), 201 # 201 -> Created

@tareas.put('/<int:id>')
def update_tarea(id: int):
    tarea = db.get_or_404(Tarea, id)
    json = request.json
    tarea.descripcion = json["descripcion"]
    tarea.realizada = json["realizada"]
    db.session().commit()
    return jsonify(tarea)

@tareas.delete('/<int:id>')
def delete_tarea(id: int):
    tarea = db.get_or_404(Tarea, id)
    db.session().delete(tarea)
    db.session().commit()
    return "", 204