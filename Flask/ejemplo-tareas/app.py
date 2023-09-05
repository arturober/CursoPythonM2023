from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric, Boolean
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tareas.db"

db.init_app(app)

@dataclass
class Tarea(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descripcion: Mapped[str] = mapped_column(String(255))  
    realizada: Mapped[bool] = mapped_column(Boolean())
    
with app.app_context():
    db.create_all()
    
@app.get('/tareas')
def get_tareas():
    select = db.select(Tarea)
    tareas = db.session().execute(select).scalars().all()
    return jsonify(tareas)

@app.get('/tareas/<int:id>')
def get_tarea(id: int):
    tarea = db.get_or_404(Tarea, id)
    return jsonify(tarea)

@app.post('/tareas')
def insert_tarea():
    json = request.json
    tarea = Tarea(descripcion=json["descripcion"], realizada=json["realizada"])
    db.session().add(tarea)
    db.session().commit()
    return jsonify(tarea), 201 # 201 -> Created

@app.put('/tareas/<int:id>')
def update_tarea(id: int):
    tarea = db.get_or_404(Tarea, id)
    json = request.json
    tarea.descripcion = json["descripcion"]
    tarea.realizada = json["realizada"]
    db.session().commit()
    return jsonify(tarea)

@app.delete('/tareas/<int:id>')
def delete_tarea(id: int):
    tarea = db.get_or_404(Tarea, id)
    db.session().delete(tarea)
    return "", 204

app.run()
