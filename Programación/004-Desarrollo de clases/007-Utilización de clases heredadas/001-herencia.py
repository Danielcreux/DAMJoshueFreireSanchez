class Persona:
    def __init__(self, nombre, apellidos, email, telefono, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono
        self.edad = edad
    
    def dameDatos(self):
        print(
            f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, "
            f"Email: {self.email}, Teléfono: {self.telefono}"
        )


class Empleado(Persona):
    def __init__(self, nombre, apellidos, email, telefono, edad, puesto):
        super().__init__(nombre, apellidos, email, telefono, edad)
        self.puesto = puesto
    
    def dameDatos(self):
        super().dameDatos()
        print(f"Puesto: {self.puesto}")


class Cliente(Persona):
    def setEdad(self, nuevaedad):
        if nuevaedad == self.edad + 1:
            self.edad = nuevaedad
        else:
            print("Operación no permitida")


# Crear instancias y probar
cliente1 = Cliente("Jose Vicente", "Carratalá", "info@jocarsa.com", 6535646, 20)
empleado1 = Empleado("Ana María", "López", "ana@empresa.com", 1234567, 30, "Gerente")

# Usar métodos
cliente1.dameDatos()
print(f"Edad inicial del cliente: {cliente1.edad}")
cliente1.setEdad(21)
print(f"Edad actualizada del cliente: {cliente1.edad}")

empleado1.dameDatos()
