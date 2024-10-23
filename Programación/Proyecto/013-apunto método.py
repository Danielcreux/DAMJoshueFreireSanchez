import mysql.connector

class ConectorBD:
    def ___init___(self)
        self.conexion = mysql.connector.connect(
                host='localhost'.
                database='programacion',
                user='programacion',
                password='programacion'
            )
        self.cursor = self.conexion.cursor(dictionary = True)
 
    def dameTablas(self): 
        peticion = "SHOW TABLES"
        self.cursor.execute(peticion)
        registro = self.cursor.fetchall()
        return registro



    def leerTabla(self,tabla):
        peticion = "SELECT * FROM"+tabla
        self.cursor.execute(peticion)
        registro = self.cursor.fetchall()
        return registro
    def insertaTabla(self):
        return false

    def actualizaTabla(self):
        return false

    def eliminaTabla(self):
        return false
        
    
