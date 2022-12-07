import os

# Declara parámetros de conexión
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')