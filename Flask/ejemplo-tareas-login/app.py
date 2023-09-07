from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from db import db
from routes import rutas_tareas, rutas_auth
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(rutas_tareas, url_prefix='/tareas')
app.register_blueprint(rutas_auth, url_prefix='/auth')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tareas-login.db"

db.init_app(app)

with app.app_context():
    db.create_all()

app.run()
