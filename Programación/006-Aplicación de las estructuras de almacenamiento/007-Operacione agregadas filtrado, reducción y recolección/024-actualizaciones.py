'''
    Programa agenda en SQlite
    (c) 2024 por Joshué Daniel
    v 0.1 Empezando en clase 
'''
import sqlite3

conexion = sqlite3.connect('empresa.db')

cursor = conexion.cursor()

print("############################")
print("      Programa agenda       ")
print("  por Joshue Daniel Freire  ")
print("############################")

while True:
    
    print("Menú principal")
    print("1.-Crear un nuevo registro")
    print("2.-Listado de registros")
    print("3.-Actualización de registros")
    print("4.-Eliminación de registros")

    opcion = input("Selecciona una opcion:")

    if opcion == "1":
        print("Vamos a insertar un registro")
        
        nombre = input("Introduce un nuevo nombre:")
        apellidos = input("Introduce nuevo apellidos:")
        email = input("Introduce un nuevo email:")
        direccion = input("Introduce una nueva direccion:")

        cursor.execute(f'''
        INSERT INTO clientes
        VALUES (
            NULL,
            "{nombre}",
            "{apellidos}",
            "{email}",
            "{direccion}"
                
            );
        ''')                                                        

        conexion.commit()     
        
    elif opcion == "2":
        print("Vamos a listar los registros")
        cursor.execute('''
            SELECT*FROM clientes;
        ''')

        filas = cursor.fetchall()

        for fila in filas:
            print (fila)

    elif opcion == "3":
        print("Vamos a actualizar los registros")

        identificador = input("Indica el registro que quieres actualizar (id):")

        nombre = input("Introduce un nuevo nombre:")
        apellidos = input("Introduce nuevos apellidos:")
        email = input("Introduce un nuevo email:")
        direccion = input("Introduce una nueva direccion:")

        cursor.execute(f'''
            UPDATE clientes
            SET
            nombre = '{nombre}',
            apellidos = '{apellidos}',
            email = '{email}',
            direccion = '{direccion}'
            WHERE Identificador = {identificador};
        ''')

        conexion.commit()
        
    elif opcion == "4":
        print("Vamos a eliminar un registro")
        
        identificador = input("Indica el registro que quieres eliminar (id):")

        cursor.execute(f'''
        DELETE FROM clientes
        WHERE Identificador = {identificador};
        ''')

        conexion.commit() 

conexion.close()
