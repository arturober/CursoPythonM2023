from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric, Boolean

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

@dataclass
class Producto(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(255))
    precio: Mapped[float] = mapped_column(Numeric(10,2))
      
with app.app_context():
    db.create_all()
    
@app.get('/productos')
def get_productos():
    select = db.select(Producto)
    productos = db.session().execute(select).scalars().all()
    return jsonify(productos)

@app.get('/productos/<int:id>')
def get_producto(id: int):
    producto = db.get_or_404(Producto, id)
    return jsonify(producto)

@app.post('/productos')
def insert_producto():
    json = request.json
    producto = Producto(nombre=json["nombre"], precio=json["precio"])
    db.session().add(producto)
    db.session().commit()
    return jsonify(producto), 201 # 201 -> Created

@app.put('/productos/<int:id>')
def update_producto(id: int):
    producto = db.get_or_404(Producto, id)
    json = request.json
    producto.nombre = json["nombre"]
    producto.precio = json["precio"]
    db.session().commit()
    return jsonify(producto)

@app.delete('/productos/<int:id>')
def delete_producto(id: int):
    producto = db.get_or_404(Producto, id)
    db.session().delete(producto)
    return "", 204

app.run()
