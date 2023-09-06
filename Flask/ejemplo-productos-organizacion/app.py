from flask import Flask
from db import db
from routes import rutas_productos

app = Flask(__name__)

# Todas las rutas que empiecen por /productos se gestionan aquí
# Si pongo el url_prefix, tengo que quitarlo en las rutas
# Hay que registrar las rutas antes de inicializar db!!!
app.register_blueprint(rutas_productos, url_prefix='/productos')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

with app.app_context():
    db.create_all()

app.run()
