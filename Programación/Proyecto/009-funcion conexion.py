import mysql.connector

def conector():
    conexion = mysql.connector.connect(
                host='localhost',
                database='programacion',
                user='programacion',
                password='programacion'
            )
    return True


def dameTablas():
    conexion = mysql.connector.connect(
                host='localhost',
                database='programacion',
                user='programacion',
                password='programacion'
            )

    cursor = conexion.cursor(dictionary = True)

    peticion = "SHOW TABLES"
    cursor.execute(peticion)

    registros = cursor.fetchall()

    return registro

print(dameTablas())

def leerTabla():
    conexion = mysql.connector.connect(
                host='localhost',
                database='programacion',
                user='programacion',
                password='programacion'
            )

    cursor = conexion.cursor(dictionary = True)

    peticion = "SELECT * FROM clientes"
    cursor.execute(peticion)

    registros = cursor.fetchall()

    return registro

print(dameTablas())
print(leerTabla())
