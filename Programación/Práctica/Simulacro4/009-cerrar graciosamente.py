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
    print("3-Eliminar un registro")
    print("4-Actualizar registro")
    print("5-Cerrar el programa")
    opcion = input("Escoge una opcion:")
    

    if opcion == "1":
        cursor = conexion.cursor(dictionary=True)    #Creo un cursor y me aseguro que la info me la de en JSON
        peticion = "SELECT * FROM capitulos"         #Pido todos los capitulos
        cursor.execute(peticion)                     #Ejecuto la peticion 
        filas = cursor.fetchall()                    #saco las filas
        print(filas)                                 #imprimo las filas
    elif opcion=="2":
        cursor = conexion.cursor(dictionary=True)            #Creo un cursor y me aseguro que la info me la de en JSON
        titulo=input("Introduce el titulo del capitulo:")   #Ingreso titulo 
        subtitulo=input("Introduce el subtitulo del capitulo:")  #Ingreso subtitulo
        imagen=input("Introduce la imagen  del capitulo:")     #Ingreso imagen
        video=input("Introduce el video del capitulo:")        #Ingreso video
        texto=input("Introduce el texto del capitulo:")        #Ingreso texto
        peticion = f"""
        INSERT INTO capitulos
        VALUES(
            NULL,
            '{titulo}',
            '{subtitulo}',
            '{imagen}',
            '{video}',
            '{texto}'
        )"""                                        #inserto nuevo capitulo en base de datos
        cursor.execute(peticion)                    #Ejecuto la peticion 
        filas = cursor.fetchall()                   #saco las filas
        print(filas)                                #imprimo las filas
        conexion.commit()
    elif opcion == "3":
        cursor = conexion.cursor(dictionary=True)    #Creo un cursor y me aseguro que la info me la de en JSON
        Identificador=input("Introduce el identificador del capitulo:")
        peticion =f"""
        DELETE FROM capitulos
        Where Identificador = {Identificador}
        """                                          #Pido todos los capitulos
        cursor.execute(peticion)                     #Ejecuto la peticion 
        filas = cursor.fetchall()                    #saco las filas
        print(filas)
        conexion.commit()                               #imprimo las filas
    elif opcion == "4":
        cursor = conexion.cursor(dictionary=True)    #Creo un cursor y me aseguro que la info me la de en JSON
        Identificador=input("Introduce el identificador del capitulo para actualizar:")
        titulo=input("Introduce el nuevo titulo del capitulo:")   #Ingreso titulo 
        subtitulo=input("Introduce el nuevo subtitulo del capitulo:")  #Ingreso subtitulo
        imagen=input("Introduce la nueva imagen  del capitulo:")     #Ingreso imagen
        video=input("Introduce el nuevo video del capitulo:")        #Ingreso video
        texto=input("Introduce el nuevo texto del capitulo:")        #Ingreso texto
        if titulo != "":
                peticion =f"""
                UPDATE capitulos
                SET
                    titulo = '{titulo}'
                WHERE
                Identificador = {Identificador};
                """                                          #Pido todos los capitulos
                cursor.execute(peticion)                     #Ejecuto la peticion 
                filas = cursor.fetchall()                    #saco las filas
                print(filas)
                conexion.commit()#imprimo las filas
        if subtitulo != "":
                peticion =f"""
                UPDATE capitulos
                SET
                    subtitulo = '{subtitulo}'
                WHERE
                Identificador = {Identificador};
                """                                          #Pido todos los capitulos
                cursor.execute(peticion)                     #Ejecuto la peticion 
                filas = cursor.fetchall()                    #saco las filas
                print(filas)
                conexion.commit()#imprimo las filas
        if imagen != "":
                peticion =f"""
                UPDATE capitulos
                SET
                    imagen = '{imagen}'
                WHERE
                Identificador = {Identificador};
                """                                          #Pido todos los capitulos
                cursor.execute(peticion)                     #Ejecuto la peticion 
                filas = cursor.fetchall()                    #saco las filas
                print(filas)
                conexion.commit()#imprimo las filas
        if video != "":
                peticion =f"""
                UPDATE capitulos
                SET
                    video = '{video}'
                WHERE
                Identificador = {Identificador};
                """                                          #Pido todos los capitulos
                cursor.execute(peticion)                     #Ejecuto la peticion 
                filas = cursor.fetchall()                    #saco las filas
                print(filas)
                conexion.commit()#imprimo las filas
        if texto != "":
                peticion =f"""
                UPDATE capitulos
                SET
                    texto = '{texto}'
                WHERE
                Identificador = {Identificador};
                """                                          #Pido todos los capitulos
                cursor.execute(peticion)                     #Ejecuto la peticion 
                filas = cursor.fetchall()                    #saco las filas
                print(filas)
                conexion.commit()#imprimo las filas
    elif opcion == "5":
            conexion.close()
            break
        
print("El programa ha finalizado")
        

        

