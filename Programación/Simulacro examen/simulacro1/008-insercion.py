class Cliente:
    def __init__(self,nuevoidentificador,nuevonombre,nuevosapellidos,nuevoemail):
        self.identificador = nuevoidentificador
        self.nombre = nuevonombre
        self.apellido = nuevosapellidos
        self.email = nuevoemail

class Productos:
    def __init__(self,nuevoid,nuevonombre,nuevadescripcion,nuevoprecio):
        self.id = nuevoid
        self.nombre = nuevonombre
        self.descripcion = nuevadescripcion
        self.precio = nuevoprecio
        
clientes = []
productos = []

print("Programa de consola")
print("v0.1 por Joshue Daniel")

while True:
    print("#########################")
    print("Selecciona entidad")
    print("1.-Clientes")
    print("2.-Productos")

    entidad = input("Indica la opcion seleccionada:")

    print("Selecciona operacion")
    print("1.-Insertar un nuevo registro")
    print("2.- Listar registros")
    print("3.- Actualizar registro")
    print("4.- Eliminar registro")

    opcion = input("Selecciona una de estas operaciones:")

    if opcion == "1":
        print("Insertamos un nuevo registro")
        identificador = input("Introduce el id del nuevo cliente")
        nombre = input("Introduce el nombre del nuevo cliente")
        apellidos = input("Introduce los apellidos del nuevo cliente")
        email = input("Introduce el email del nuevo cliente")
        clientes.append(Cliente(identificador,nombre,apellidos,email))
        
    elif opcion == "2":
        print("Listamos los registros")
    elif opcion == "3":
        print("Actualizamos el registro")
    elif opcion == "4":
        print("Eliminar el registro")
        


