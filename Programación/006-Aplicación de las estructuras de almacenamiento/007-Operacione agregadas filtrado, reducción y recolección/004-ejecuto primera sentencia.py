import sqlite3

conexion = sqlite3.connect('empresa.db')

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE clientes
    IF NOT EXISTS
''')
