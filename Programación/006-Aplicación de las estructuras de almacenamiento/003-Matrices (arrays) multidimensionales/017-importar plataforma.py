'''
     Programa agenda con colecciones bidimensionales
     (C) 2024 Joshue Freire
'''
import platform

print(platform.system())

print("Programa agenda (c) 2024 Joshue Freire")
agenda = []


while(True):
    print("Selecciona una de las siguientes opciones")
    print("1-Insertar un nuevo registro")
    print("2-Listar los registros")
    opcion = input("Selecciona unas de las opciones:")

    print("la opcion que has escogido es:",opcion)

    if(opcion == "1"):
        print("Vamos a insertar un registro")
        nombre = input("Introduce tu nombre:")
        apellidos = input("Introduce tu apellido:")
        email = input("Introduce tu email:")
        telefono = input("Introduce tu telefono:")
        agenda.append([nombre,apellidos,email,telefono])
    elif(opcion == "2"):
        print("Vamos a leer registros")
        for registro in agenda:
            print("###################")
            print("nombre:",registro[0])
            print("apellidos:",registro[1])
            print("email:",registro[2])
            print("telefono:",registro[3])
