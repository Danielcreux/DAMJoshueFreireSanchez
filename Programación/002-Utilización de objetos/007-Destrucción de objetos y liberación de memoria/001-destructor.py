class Cliente:
    
    def __init__(self, nuevonombre, nuevosapellidos, nuevoemail, nuevotelefono):  
        self.nombre = nuevonombre
        self.apellidos = nuevosapellidos
        self.email = nuevoemail
        self.telefono = nuevotelefono  
        
    def dameDatos(self):
        print(
            "-Nombre:", self.nombre,  
            "-Apellidos:", self.apellidos,
            "-Email:", self.email,
            "-Teléfono:", self.telefono)
        
# Creación de instancias con todos los argumentos, incluido teléfono
cliente1 = Cliente("Joshué", "Freire", "info@joshue.com", 634567)
cliente2 = Cliente("Daniel", "Figueroa", "info@Figueroa.com", 456677)

# Llamadas correctas a dameDatos()
cliente1.dameDatos()
cliente2.dameDatos()

#Para cuando querramos agregar más datos    
print(cliente1)
cliente1 = None
print(cliente1)
