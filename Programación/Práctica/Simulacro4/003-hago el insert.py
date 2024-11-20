import mysql.connector                      #importo libreria de mysql

conexion = mysql.connector.connect(
    host='localhost',
    user='examenprogramacion',
    password='examenprogramacion',
    database='examenprogramacion'
    )                                       #Me conecto a la base de datos 

while True:
    print("Escoge una opcion:")
    print("1-Leer registros")
    print("2-Insertar un registro")
    opcion = input("Escoge una opcion:")
    

    if opcion == "1":
        cursor = conexion.cursor(dictionary=True)    #Creo un cursor y me aseguro que la info me la de en JSON
        peticion = "SELECT * FROM capitulos"         #Pido todos los capitulos
        cursor.execute(peticion)                    #Ejecuto la peticion 
        filas = cursor.fetchall()                   #saco las filas
        print(filas)                                #imprimo las filas
    elif opcion=="2":
        cursor = conexion.cursor(dictionary=True)    #Creo un cursor y me aseguro que la info me la de en JSON
        titulo=input("Introduce el titulo del capitulo:")
        subtitulo=input("Introduce el subtitulo del capitulo:")
        imagen=input("Introduce la imagen  del capitulo:")
        video=input("Introduce el video del capitulo:")
        texto=input("Introduce el texto del capitulo:")
        peticion = f"""
        INSERT INTO capitulos
        VALUES(
            NULL,
            '{titulo}',
            '{subtitulo}',
            '{imagen}',
            '{video}',
            '{texto}'
        )"""                                           #Pido todos los capitulos
        cursor.execute(peticion)                    #Ejecuto la peticion 
        filas = cursor.fetchall()                   #saco las filas
        print(filas)                                #imprimo las filas
        conexion.commit()
        

        

