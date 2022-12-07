from pymongo import MongoClient

personaje = MongoClient('localhost',27017)

db = personaje['personajes_flask']