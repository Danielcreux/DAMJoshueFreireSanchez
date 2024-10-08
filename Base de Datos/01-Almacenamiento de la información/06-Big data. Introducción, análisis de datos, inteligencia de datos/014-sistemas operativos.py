import sqlite3
import matplotlib.pyplot as plt

conexion = sqlite3.connect('registros.db')
conexion.text_factory = lambda x: str(x,'utf-8','replace')
cursor = conexion.cursor()

etiquetas = []
datos = []

cursor.execute('''
    SELECT
    COUNT(navegador) as numero
    FROM logs
    WHERE navegador LIKE '%Windows%'
  
    ;
''')

filas = cursor.fetchall()

etiquetas.append("Windows")
datos.append(filas[0][0])

cursor.execute('''
    SELECT
    COUNT(navegador) as numero
    FROM logs
    WHERE navegador LIKE '%Mac OS%'
  
    ;
''')

filas = cursor.fetchall()

etiquetas.append("Mac")
datos.append(filas[0][0])

cursor.execute('''
    SELECT
    COUNT(navegador) as numero
    FROM logs
    WHERE navegador LIKE '%Linux%'
  
    ;
''')

filas = cursor.fetchall()

etiquetas.append("Linux")
datos.append(filas[0][0])

print(datos)
