import mysql.connector                      #importo libreria de mysql

conexion = mysql.connector.connect(
    host='localhost',
    user='examenprogramacion',
    password='examenprogramacion',
    database='examenprogramacion'
    )                                       #Me conecto a la base de datos 
 
cursor = conexion.cursor(dictionary=True)    #Creo un cursor y me aseguro que la info me la de en JSON

peticion = "SELECT * FROM capitulos"         #Pido todos los capitulos
 
cursor.execute(peticion)                    #Ejecuto la peticion 

filas = cursor.fetchall()                   #saco las filas

print(filas)                                #imprimo las filas 
