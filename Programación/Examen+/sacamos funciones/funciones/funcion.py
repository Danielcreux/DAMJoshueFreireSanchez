def insertar():
  print("\nVamos a insertar un nuevo cliente")
  nombre = input("Introduce el nuevo nombre: ")
  apellidos = input("Introduce los nuevos apellidos: ")
  email = input("Introduce el nuevo email: ")
  direccion = input("Introduce la nueva dirección: ")
  nuevocliente = cliente(nombre, apellidos, email, direccion)                 # Creo una instancia de Cliente
  agenda.append(nuevocliente)                                                  # Agrego el cliente a la agenda

def listar():
    print("\nListado de registros:")
    for cliente in agenda:                                                       # Itero por cada cliente en la agenda
        print("Nombre:", cliente.nombre)
        print("Apellidos:", cliente.apellidos)
        print("Email:", cliente.email)
        print("Dirección:", cliente.direccion)

def guardar():
    with open("agenda.txt", 'wb') as archivo:                                                   # Abro un archivo binario en modo escritura
      pickle.dump(agenda, archivo)                                                  # Guardo la agenda en el archivo
    print("\nLa agenda ha sido guardada en un archivo")

def cargar():
    try:
      with open("agenda.txt", 'rb') as archivo:                                      # Abro el archivo en modo lectura
        agenda = pickle.load(archivo)                                            # Cargo el contenido del archivo en la agenda
        print("\nLa agenda ha sido cargada con éxito")
    except FileNotFoundError:
        print("\nNo se ha encontrado el archivo de la agenda. Por favor, guarda primero un registro.")

