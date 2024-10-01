#Windows: pip install mysql-connector-python
import mysql.connector
from flask import flask
from flask_cors import CORS                 #permite conectarnos desde html               
#pip install flask-cors - pip3 install flask-cors

aplicacion = Flask(__name__)
CORS(aplicacion)

servidor = "localhost"                      #Creo una variable en la que apunto el servidor
usuario = "miempresa"                       #Creo una variable para definir el usuario
contrasena = "miempresa"                    #Creo una variable para definir la contraseña del usuario
base_de_datos = "miempresa"                 #Creo una variable para definir la base de datos a la que me conecto

conexion = mysql.connector.connect(
    host=servidor,
    database=base_de_datos,
    user=usuario,
    password=contrasena
)                                           #Establezco una conexión con la base de datos con los datos seleccionados

@aplicacion.route('/')                                  #Creo un escuchador para que esté pendiente cuando alguien entra
def inicio():                                           #Defino una función se puede llamar como yo quier
                                             
    peticion = "SELECT * FROM clientes;"        #Preparo una petición

    cursor = conexion.cursor()                  #Una petición en Python requiere un cursor

    cursos.execute(peticion)                    #En el cursor, ejecuto la peticion que he dejado preparado arriba
    filas = cursor.fetchall()                   #En una variable llamadas filas , almaceno los resutados 
    contenido = []                              #Creo una lista vacía donde pondré a los clientes
    for fila in filas:                          #Como filas representa a todas, yo quiero coger una a una
        contenido.append(fila)                  #Utilizando el comando append añado cada uno de los elementos                           
        return contenido                        #Lanzo el contenido al navegador web

aplicacion.run(debug=True)                      #Arranco el servdor web
