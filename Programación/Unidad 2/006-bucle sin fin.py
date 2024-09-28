'''
    Programa agenda
    (c) 2024 Joshue Freire
'''
# Bienvenida ################

TITULO = "Programa agenda"
AUTOR = "Joshue Freire"
print(TITULO, "por", AUTOR)

# Estructura de control de ejecución infinita #######

while True:

    # Menú principal ###########

    print("\nEscoge una opción")
    print("1.- Insertar")
    print("2.- Listar")
    print("3.- Actualizar")
    print("4.- Eliminar")
    print("5.- Salir del programa") 

    # El usuario debe escoger una opción #########

    opcion = input("Selecciona una opción (1-5): ")
    print("Has seleccionado la opción:", opcion)

    # Seleccione la operación a realizar ########

    if opcion == "1":
        print("Vamos a insertar un nuevo cliente")
    elif opcion == "2":
        print("Vamos a listar los clientes")
    elif opcion == "3":
        print("Vamos a actualizar un cliente")
    elif opcion == "4":
        print("Vamos a eliminar a un cliente")
    elif opcion == "5":
        print("Saliendo del programa...")
        exit()
    

        
