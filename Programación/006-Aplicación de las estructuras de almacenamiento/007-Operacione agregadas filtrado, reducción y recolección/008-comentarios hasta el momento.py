import sqlite3                                              #Importo la libreria de conexión de bases de datos 

conexion = sqlite3.connect('empresa.db')                    #Abro una base de datos existente o la creo si no existe

cursor = conexion.cursor()                                  #Creo un cursor dentro de la base de datos

cursor.execute('''
    CREATE TABLE
    IF NOT EXISTS clientes
    (
        Identificador INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        apellidos TEXT,
        email TEXT,
        direccion TEXT
    )
''')                                                        #Ejecuto una petición de creación de la tabla en el caso que no exista

cursor.execute('''
    INSERT INTO clientes
    VALUES (
        NULL,
        'Joshue Daniel',
        'Freire Sánchez',
        'jdinfo@hotmail.com',
        'La casa de Joshue'
    )
''')                                                        #Inserto un nuevo registro 

conexion.commit()                                           #Ejecuto las peticiones

conexion.close()                                            #Cerramos los recursos que previamente hemos abierto
