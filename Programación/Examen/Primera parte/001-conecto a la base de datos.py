import mysql.connector                      #importo libreria de mysql

conexion = mysql.connector.connect(
    host='localhost',
    user='ciencia',
    password='ciencia',
    database='ciencia'
    )                                       #Me conecto a la base de datos 
