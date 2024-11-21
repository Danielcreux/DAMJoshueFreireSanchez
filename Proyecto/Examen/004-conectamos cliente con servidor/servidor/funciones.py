import mysql.connector                                  # Importo el conector de MySQL

conexion = mysql.connector.connect(
    host="localhost",           
    user="examenprogramacion",        
    password="examenprogramacion",   
    database="examenprogramacion"    
)                                                       # Me conecto a la base de datos

def seleccionaExpertos():
    cursor = conexion.cursor(dictionary = True)             # Creo un cursor y me aseguro de que la info me viene en JSON
    peticion = "SELECT * FROM expertos"                    # Pido todo de expertos 
    cursor.execute(peticion)                                # Ejecuto la peticion
    filas = cursor.fetchall()                               # Saco las filas
    return filas                                            # Imprimo las filas

def seleccionaExperto(Identificador):
    try:
        Identificador = int(Identificador)
        cursor = conexion.cursor(dictionary = True)                    # Creo un cursor y me aseguro de que la info me viene en JSON
        peticion = f""" SELECT * FROM expertos
        WHERE Identificador = {Identificador}
        """                                                     # Pido todos los expertos 
        cursor.execute(peticion)                                # Ejecuto la peticion
        filas = cursor.fetchall()                               # Saco las filas
        if filas != []:
            return filas                                            # Imprimo las filas
        else:
            return False
    except:
            return False

def insertaExperto(Nombre,Resumen,Imagen,Video,Texto):
    cursor = conexion.cursor(dictionary = True)                 # Creo un cursor y me aseguro de que la info me viene en JSON
    peticion = f"""
    INSERT INTO expertos
    VALUES (
        NULL,
        '{Nombre}',
        '{Resumen}',
        '{Imagen}',
        '{Video}',
        '{Texto}'
    )"""                                                    # Inserto un nuevo experto
    cursor.execute(peticion)                                # Ejecuto la peticion
    filas = cursor.fetchall()                               # Saco las filas
    conexion.commit()
    return True

def eliminaExperto(Identificador):
    cursor = conexion.cursor(dictionary = True)                 # Creo un cursor y me aseguro de que la info me viene en JSON
    peticion = f"""
    DELETE FROM expertos
    WHERE Identificador = {Identificador}
    """     
    cursor.execute(peticion)                                # Ejecuto la peticion
    filas = cursor.fetchall()                               # Saco las filas
    conexion.commit()
    return True

def actualizaCampo(cadena,valor,Identificador):
    cursor = conexion.cursor(dictionary = True) 
    peticion = f"""
        UPDATE  expertos
        SET 
            {cadena} = '{valor}'
            
        WHERE
        Identificador = {Identificador}
        """                                                    # Inserto un nuevo experto 
    cursor.execute(peticion)                                # Ejecuto la peticion
    filas = cursor.fetchall()                               # Saco las filas
    print(filas)                                            # Imprimo las filas
    conexion.commit()
    
def actualizaExperto(Identificador,Nombre,Resumen,Imagen,Video,Texto):
                    # Creo un cursor y me aseguro de que la info me viene en JSON
    if Nombre != "":
        actualizaCampo("Nombre",Nombre,Identificador)
    if Resumen != "":
        actualizaCampo("Resumen",Resumen,Identificador)
    if Imagen != "":
        actualizaCampo("Imagen",Imagen,Identificador)
    if Video != "":
        actualizaCampo("Video",Video,Identificador)
    if Texto != "":
        actualizaCampo("Texto",Texto,Identificador)
    return True

        
