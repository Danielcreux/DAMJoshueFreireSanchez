import sqlite3


conexion = sqlite3.connect('registros.db')
conexion.text_factory = lambda x: str(x,'utf-8','replace')
cursor = conexion.cursor()

cursor.execute('''
    SELECT
    COUNT(extra3) as numero,
    extra3
    FROM logs
    GROUP BY extra3
    ORDER BY numero DESC
    ;
''')

filas = cursor.fetchall()


for fila in filas:
    print(fila)

