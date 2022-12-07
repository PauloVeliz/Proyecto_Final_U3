from flask import Flask
from app.config import Config
from flask_bootstrap import Bootstrap
from app.routes.personaje import personajes_ruta

# Función de fábrica
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    app.register_blueprint(personajes_ruta)
    return app
