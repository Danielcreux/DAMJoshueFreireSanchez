import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'miemepresa',
    password = 'miempresa',
    database = 'miempresa'
)
cursor = connection.cursor(dictionary = True)

print("Programa de gestión de empresa v0.1")
print("por Joshué Daniel")

print("Selecciona una tabla de la base de datos:")

peticion = "SHOW TABLES;"

cursor.execute(peticion)
