from funciones import *
from flask import Flask, request                                            # Importamos la librería Flask para hacer un micro servidor web
from flask_cors import CORS                                                 # Importo CORS para no tener problemas de conexiónde un lado a otro

aplicacion = Flask(__name__)
CORS(aplicacion)                                                            # Le aplico CORS para no tener esos problemas de conexión

servidor = "localhost"                                                      # Creo una variable en la que apunto a mi servidor
usuario = "examenprogramacion"                                                            # Creo una variable para definir el usuario
contrasena = "examenprogramacion"                                                         # Creo una variable para definir la contraseña del usuario
base_de_datos = "examenprogramacion"                                                      # Creo una variable para definiar la base de datos a la que me conecto

@aplicacion.route('/damearticulos')                                                      # Defino la ruta en la que el servidor va a escuchar
def inicio():                                                               # Defino lo que se ejecuta en esa ruta                                            # A la lista de entradas, le añado una entrada
    return seleccionaCapitulos()                                                        # Devuelvo la lista de entradas, ahora con las entradas correctas     

aplicacion.run()
