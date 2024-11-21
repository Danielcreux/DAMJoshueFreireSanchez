import mysql.connector                      #importo libreria de mysql

conexion = mysql.connector.connect(
    host='localhost',
    user='ciencia',
    password='ciencia',
    database='ciencia'
    )                                       #Me conecto a la base de datos 

print("Escoge una opcion:")                 #consola del menu 
print("1-Leer registros")
print("2-Insertar un registro")
print("3-Eliminar un registro")
print("4-Actualizar registro")
print("5-Cerrar el programa")
opcion = input("Escoge una opcion:")

if opcion == "1":
        cursor = conexion.cursor(dictionary=True)   #Creo un cursor y me aseguro que la info me la de en JSON
        peticion = "SELECT * FROM expertos"         #Pido todos los capitulos
        cursor.execute(peticion)                    #Ejecuto la peticion 
        filas = cursor.fetchall()                   #saco las filas
        print(filas)                                #imprimo las filas
