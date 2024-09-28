class Persona:
    def__init__(self,
                 nuevonombre,
                 nuevoapellidos,
                 nuevoemail,
                 nuevotelefono
                 ):
         self.nombre = nuevonombre
         self.apellidos = nuevosapellidos
         self.email = nuevoemail
         self.telefono = nuevotelefono
         set.edad = nuevaedad
    

class Empleado(Persona):
     def__init__(self):
         super ()
                
class Cliente(Perosna):
     def__init__(self):
         super()
                
    def dameDatos(self):
        print(
            "Nombre:",
            self.nombre,
            "- Apellidos:",
            self.apellidos,
            "-Email:",
            self.email,
            "-Telefono:",
            self.telefono)
    def getNombre(self)
        return self.nombre
    def setNombre(self,nuevonombre):
        self.nombre = nuevonombre


       def getEdad(self)
        return self.edad
    def setEdad(self,nuevoedad):
         if nuevaedad = self.edad + 1:
            self.edad = nuevaedad
        else:
            print("operación no permitida")


        
            
