import pickle   # importo la librería que permite leer y escribir bloques de memoria
from claseCliente import *
from mensajebienvenida import *

agenda = []  # Creo una agenda vacía
        
bienvenida()

while True:  # Bucle infinito para el menú de navegación

    menu()

    opcion = input("Selecciona una opción: ")  # Capturo la opción del usuario
    print("Has escogido la opción:", opcion)  # Muestro la opción seleccionada

    if opcion == "1":  # Si el usuario escoge la opción 1
        print("\nVamos a insertar un nuevo cliente")
        nombre = input("Introduce el nuevo nombre: ")
        apellidos = input("Introduce los nuevos apellidos: ")
        email = input("Introduce el nuevo email: ")
        direccion = input("Introduce la nueva dirección: ")

        nuevocliente = Cliente(nombre, apellidos, email, direccion)  # Creo una instancia de Cliente
        agenda.append(nuevocliente)  # Agrego el cliente a la agenda
        
    elif opcion == "2":  # Si el cliente escoge la opción 2
        print("\nListado de registros:")
        for cliente in agenda:  # Itero por cada cliente en la agenda
            print("------------------")
            print("Nombre:", cliente.nombre)
            print("Apellidos:", cliente.apellidos)
            print("Email:", cliente.email)
            print("Dirección:", cliente.direccion)
        
    elif opcion == "3":  # Si el cliente escoge la opción 3
        with open("agenda.txt", 'wb') as archivo:  # Abro un archivo binario en modo escritura
            pickle.dump(agenda, archivo)  # Guardo la agenda en el archivo
            print("\nLa agenda ha sido guardada en un archivo")
        
    elif opcion == "4":  # Si el cliente escoge la opción 4
        try:
            with open("agenda.txt", 'rb') as archivo:  # Abro el archivo en modo lectura
                agenda = pickle.load(archivo)  # Cargo el contenido del archivo en la agenda
                print("\nLa agenda ha sido cargada con éxito")
        except FileNotFoundError:
            print("\nNo se ha encontrado el archivo de la agenda. Por favor, guarda primero un registro.")
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
