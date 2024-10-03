'''
     Programa agenda con colecciones bidimensionales
     (C) 2024 Joshue Freire
'''
import platform
import os
def limpiaPantalla():
    
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    
limpiaPantalla()
print("Programa agenda (c) 2024 Joshue Freire")
agenda = []


while(True):
    print("Selecciona una de las siguientes opciones")
    print("1-Insertar un nuevo registro")
    print("2-Listar los registros")
    print("3-Eliminar un registro")
    opcion = input("Selecciona unas de las opciones:")

    limpiaPantalla()
    print("la opcion que has escogido es:",opcion)

    if(opcion == "1"):
        print("Vamos a insertar un registro")
        nombre = input("\033[32mIntroduce tu nombre:\033[0m")
        apellidos = input("\033[32mIntroduce tu apellido:\033[0m")
        email = input("\033[32mIntroduce tu email:\033[0m")
        telefono = input("\033[32mIntroduce tu telefono:\033[0m")
        agenda.append([nombre,apellidos,email,telefono])
    elif(opcion == "2"):
        print("Vamos a leer registros")
        for registro in agenda:
            print("###################")
            print("\033[31mnombre:\t\t\033[0m",registro[0])
            print("\033[32mapellidos:\t\033[0m",registro[1])
            print("\033[33memail:\t\t\033[0m",registro[2])
            print("\033[34mtelefono:\t\033[0m",registro[3])
            print("####################")
            input("Pulsa una tecla para continuar...")
