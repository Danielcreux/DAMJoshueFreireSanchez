from flask import flask
from flask_cors import CORS

aplicacion = flask(__name__)
CORS(aplicacion)

@aplicacion.route('/')
def inicio():
    entradas = []
    entradas.append({
        "titulo":"Mi primera entrada",
        "fecha":"2024-09-26",
        "contenido":"Este es el contenido de mi entrada"

    })
    return entradas
if __name__ == '__main__':
    aplicacion.run()
