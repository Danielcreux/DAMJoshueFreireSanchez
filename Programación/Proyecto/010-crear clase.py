import mysql.connector

class ConectorBD:
    def ___init___(self)
        self.conexion = mysql.connector.connect(
                host='localhost'.
                database='programacion',
                user='programacion',
                password='programacion'
            )
        self.cursor = conexion.cursor(dictionary = True)
 
    def dameTablas(self): 
        peticion = "SHOW TABLES"
        cursor.execute(peticion)
        registro = self.cursor.fetchall()
        return registro



    def leerTabla(self):
        peticion = "SELECT * FROM clientes"
        cursor.execute(peticion)
        registro = self.cursor.fetchall()
        return registro

    conexion1 = ConnectorBD()
    print(conexion1.dameTablas())

