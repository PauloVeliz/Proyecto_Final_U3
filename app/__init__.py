from flask import Flask
from app.config import Config
from flask_bootstrap import Bootstrap

# Función de fábrica
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    return app
