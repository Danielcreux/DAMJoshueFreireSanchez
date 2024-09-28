from flask import flask
from flask_cors import CORS
import mysql.connector

aplicacion = flask(__name__)
CORS(aplicacion)

conexion = mysql.connector.connect(
    host=servidor,
    database=base_de_datos,
    user=usuario,
    password=contrasena
    )

@aplicacion.route('/')
def inicio():
    entradas = []
        peticion = "SELECT * FROM entradas ORDER BY DESC;"
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(peticion)
        filas = cursor.fetchall()
        for fila in filas:
            entradas.append(fila)
            return entradas

    return entradas
if __name__ == '__main__':
    aplicacion.run()
