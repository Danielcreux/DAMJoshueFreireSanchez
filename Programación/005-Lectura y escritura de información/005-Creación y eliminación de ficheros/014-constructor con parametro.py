import pickle

class Cliente:
    def __init__(self,nuevonombre,nuevosapellidos,nuevoemail,nuevadireccion):
        self.nombre = None
        self.apellidos = None
        self.email = None
        self.direccion = None

agenda = []
        
print("##################################")
print("Programa agenda v0.1 por Jose Vicente Carratalá")
print("##################################")

while True:
    
    print("Menú de navegación")
    print("1.-Introduce un registro")
    print("2.-Listado de registros")

    opcion = input("Selecciona una opcion:")
    print("Has cogido la opcion:",opcion)

    if opcion == "1":
        print("Vamos a insertar un nuevo cliente")
        nombre = input("Introduce el nuevo nombre:")
        apellidos = input("Introduce el nuevo apellidos:")
        email = input("Introduce el nuevo email:")
        direccion = input("Introduce el nuevo direccion:")
        
    elif opcion == "2":
        print("Vamos a listar los clientes")

