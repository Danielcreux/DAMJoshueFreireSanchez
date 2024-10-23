class Persona:
    def __init__(self):
         self.nombre = None
         self.apellidos = None
         self.email = None
         self.telefono = None
         self.edad = None
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
    def getNombre(self):
        return self.nombre
    def setNombre(self,nuevonombre):
        self.nombre = nuevonombre


    def getEdad(self):
        return self.edad
    def setEdad(self,nuevaedad):
         if nuevaedad == self.edad + 1:
                self.edad = nuevaedad
         else:
            print("operación no permitida")
 
class Empleado(Persona):
     def __init__(self):
         super ()
                
class Cliente(Persona):
     def __init__(self):
         super()

Cliente1 = Cliente()
Cliente1.setNombre("Jose Vicente")
print(Cliente1.getNombre())

empleado1 = Empleado()
empleado1.setNombre("Juan")
print(empleado1.getNombre())
                
    
   


        
            
