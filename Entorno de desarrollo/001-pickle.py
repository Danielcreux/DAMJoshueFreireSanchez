import pickle

class Cliente:
    def __init__(self,nuevonombre,nuevosapellidos,nuevoemail,nuevadireccion):
        self.nombre = nuevonombre
        self.apellidos = nuevosapellidos
        self.email = nuevoemail
        self.direccion = nuevadireccion

agenda = []
        
print("##################################")
print("Programa agenda v0.1 por Jose Vicente Carratalá")
print("##################################")

while True:
    
    print("Menú de navegación")
    print("1.-Introduce un registro")
    print("2.-Listado de registros")
    print("3.-Guardar registros")

    opcion = input("Selecciona una opcion:")
    print("Has cogido la opcion:",opcion)

    if opcion == "1":
        print("Vamos a insertar un nuevo cliente")
        
        nombre = input("Introduce el nuevo nombre:")
        apellidos = input("Introduce los nuevos apellidos:")
        email = input("Introduce el nuevo email:")
        direccion = input("Introduce la nueva direccion:")

        nuevocliente = Cliente(nombre,apellidos,email,direccion)

        agenda.append(nuevocliente)
        
    elif opcion == "2":
        for cliente in agenda:
            print("------------------")
            print("nombre:",cliente.nombre)
            print("apellidos:",cliente.apellidos)
            print("email:",cliente.email)
            print("direccion:",cliente.direccion)
        
        print(agenda)
        
