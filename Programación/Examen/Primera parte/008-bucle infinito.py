import mysql.connector                      #importo libreria de mysql

conexion = mysql.connector.connect(
    host='localhost',
    user='ciencia',
    password='ciencia',
    database='ciencia'
    )                                       #Me conecto a la base de datos 
while True:
        print("Escoge una opcion:")                 #consola del menu 
        print("1-Leer registros")
        print("2-Insertar un registro")
        print("3-Eliminar un registro")
        print("4-Actualizar registro")
        print("5-Cerrar el programa")

        opcion = input("Escoge una opcion:")



        if opcion == "1":
            print("######################")
            print("Enlistar registro")
            cursor = conexion.cursor(dictionary=True)   #Creo un cursor y me aseguro que la info me la de en JSON
            peticion = "SELECT * FROM expertos"         #Pido todos los capitulos
            cursor.execute(peticion)                    #Ejecuto la peticion 
            filas = cursor.fetchall()                   #saco las filas
            print(filas)                                #imprimo las filas
            conexion.commit()

        elif opcion == "2":
            print("######################")
            print("Insertar registro")
            cursor = conexion.cursor(dictionary=True)             #Creo un cursor y me aseguro que la info me la de en JSON
            titulo=input("Introduce el nombre del experto:")      #Ingreso titulo 
            cargo=input("Introduce el cargo del experto :")       #Ingreso cargo 
            video=input("Introduce el video del experto:")        #Ingreso video
            texto=input("Introduce el texto del experto:")        #Ingreso texto
            peticion = f"""                                       
            INSERT INTO expertos
            VALUES(
                NULL,
                '{titulo}',
                '{cargo}',
                '{video}',
                '{texto}'
            )"""                                        #inserto nuevo experto en base de datos
            cursor.execute(peticion)                    #Ejecuto la peticion 
            filas = cursor.fetchall()                   #saco las filas
            print(filas)                                #imprimo las filas
            conexion.commit()                           #Concluyo peticion

        elif opcion == "3":
            print("######################")
            print("Eliminar experto")
            cursor = conexion.cursor(dictionary=True)    #Creo un cursor y me aseguro que la info me la de en JSON
            Identificador=input("Introduce el identificador del  experto:")
            peticion =f"""
            DELETE FROM expertos
            Where Identificador = {Identificador}
            """                                          #Elimino el experto que no deseo
            cursor.execute(peticion)                     #Ejecuto la peticion 
            filas = cursor.fetchall()                    #saco las filas
            print(filas)                                 #imprimo las filas
            print("Eliminado con exito")
            conexion.commit()                            #concluyo petición

        elif opcion == "4":
            print("######################")
            print("Actualizar experto")
            cursor = conexion.cursor(dictionary=True)    #Creo un cursor y me aseguro que la info me la de en JSON
            Identificador=input("Introduce el identificador del experto para actualizar:")
            titulo=input("Introduce el nuevo titulo del experto:")   #Ingreso titulo 
            cargo=input("Introduce el nuevo subtitulo del experto:")  #Ingreso cargo 
            video=input("Introduce el nuevo video del experto:")        #Ingreso video
            texto=input("Introduce el nuevo texto del experto:")        #Ingreso texto
            if titulo != "":
                    peticion =f"""
                    UPDATE expertos
                    SET
                        titulo = '{titulo}'
                    WHERE
                    Identificador = {Identificador};
                    """                                          #Actualizo el titulo
                    cursor.execute(peticion)                     #Ejecuto la peticion 
                    filas = cursor.fetchall()                    #saco las filas
                    print(filas)                                 #imprimo las filas
                    conexion.commit()                            #concluyo petición                        
            if cargo != "":
                    peticion =f"""
                    UPDATE expertos
                    SET
                        cargo = '{cargo}'
                    WHERE
                    Identificador = {Identificador};
                    """                                          #Actualizo el cargo
                    cursor.execute(peticion)                     #Ejecuto la peticion 
                    filas = cursor.fetchall()                    #saco las filas
                    print(filas)                                 #imprimo las filas
                    conexion.commit()                            #concluyo petición 
            if texto != "":
                    peticion =f"""
                    UPDATE expertos
                    SET
                        texto = '{texto}'
                    WHERE
                    Identificador = {Identificador};
                    """                                          #Actualizo el texto
                    cursor.execute(peticion)                     #Ejecuto la peticion 
                    filas = cursor.fetchall()                    #saco las filas
                    print(filas)                                 #imprimo las filas
                    conexion.commit()                            #concluyo petición
                    
        elif opcion == "5":
           conexion.close()
           print("El programa ha finalizado")
           break
        
    
    

        

        





