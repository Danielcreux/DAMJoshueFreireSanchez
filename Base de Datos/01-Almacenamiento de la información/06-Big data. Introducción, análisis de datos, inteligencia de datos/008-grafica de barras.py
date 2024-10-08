import sqlite3
import matplotlib.pyplot as plt

conexion = sqlite3.connect('registros.db')
conexion.text_factory = lambda x: str(x,'utf-8','replace')
cursor = conexion.cursor()

cursor.execute('''
    SELECT
    COUNT(anio) as año,
    anio
    FROM logs
    GROUP BY anio
    ;
''')

filas = cursor.fetchall()

etiquetas = []
datos = []

for fila in filas:
    etiquetas.append(fila[1])
    datos.append(fila[0])

#Crear gráfico de barras
plt.bar(etiquetas, datos)

#Etiquetas y título del gráfico
plt.xlabel('Año')
plt.ylabel('Cantidad')
plt.title('Cantidad de registros por año')

#Guardar gráfico
plt.savefig('barras_bigdata.png')

plt.close() 
