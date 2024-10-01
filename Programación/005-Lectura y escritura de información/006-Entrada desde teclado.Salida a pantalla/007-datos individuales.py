#Windows: pip install mysql-connector-python
import mysql.connector

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
                                                
peticion = "SELECT * FROM clientes;"        #Preparo una petición

cursor = conexion.cursor()                  #Una petición en Python requiere un cursor

cursos.execute(peticion)                    #En el cursor, ejecuto la peticion que he dejado preparado arriba
filas = cursor.fetchall()                   #En una variable llamadas filas , almaceno los resutados 

for fila in filas:                          #Como filas representa a todas, yo quiero coger una a una
    print(fila)                             #Imprimo cada fila individualmente
    print("##################")             #Separador totalmente cosmético
    print("El identificador es:", fila[0])  #Cada uno de los datos 
    print("El nombre es:", fila[1])
    print("El apellido es:", fila[2])
    print("El email es:", fila[3])
    print("La localidad es:", fila[4])
    print("La fecha de nacimiento es:", fila[5])
