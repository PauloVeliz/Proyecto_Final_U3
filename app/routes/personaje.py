from flask import Blueprint,render_template
from app.models.personaje import Personaje
from app.db import db
import requests

personajes_ruta = Blueprint('personajes_ruta',__name__)

@personajes_ruta.route('/')
def index():
    return render_template('index.html')

@personajes_ruta.route('/crear-perfil')
def crear_perfil():
    return render_template('crear_perfil.html')

@personajes_ruta.route('/guardar-personajes')
def guardar_personajes():
    # n es la página del personaje a cargar
    n_pages = 21
    for n in range(1, n_pages + 1):
        url = 'https://rickandmortyapi.com/api/character?page=' + str(n)
        inf_personaje = requests.get(url)

        if inf_personaje.status_code != 200:
            print('No se encontró personaje.')
            continue
        
        inf_personaje_json = inf_personaje.json()

        for personaje in inf_personaje_json['results']:
            if db.personajes.find_one({'id':personaje['id']}) is None:
                db.personajes.insert_one(personaje)

    return 'Se guardaron los datos exitosamente en MongoDB.'

@personajes_ruta.route('/mostrar-personajes')
def mostrar_personajes():
    personajes = db.personajes.aggregate([{'$sort':{'id':-1}}])

    return render_template('mostrar_personajes.html',personajes=personajes)
