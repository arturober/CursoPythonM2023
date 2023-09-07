import os
from flask import Flask, send_file
from db import db
from routes import rutas_productos, rutas_categorias

app = Flask(__name__)

@app.get('/imagenes/<filename>')
def serve_image(filename):
    print( filename)
    image_path = os.path.dirname(__file__) + '/imagenes/' + filename
    return send_file(image_path, mimetype='image/jpeg') 

# Todas las rutas que empiecen por /productos se gestionan aquí
# Si pongo el url_prefix, tengo que quitarlo en las rutas
# Hay que registrar las rutas antes de inicializar db!!!
app.register_blueprint(rutas_categorias, url_prefix='/categorias')
app.register_blueprint(rutas_productos, url_prefix='/productos')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///categoria-productos.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/productos"


db.init_app(app)

with app.app_context():
    db.create_all()

app.run()
