'''
    Programa agenda
    (c) 2024 Joshue Freire
'''
#Bienvenida ################

TITULO = "Programa agenda"
AUTOR = "Joshue Freire"
print(TITULO,"por",AUTOR)

#Menu principal ###########

print("Escoge una opcion")
print("1.-Insertar")
print("2.-Listar")
print("3.-Actualiza")
print("4.-Eliminar")

#El usuario debe escoger una opcion #########

opcion = input("Selecciona una opcion (1-4):")
print("Has selecciona la opcion:",opcion)

# Seleccione la operacion a realizar ########

if opcion == "1":
    print("Vamos a insertar un nuevo cliente")
elif opcion == "2":
    print("vamos a listar los clientes")
elif opcion == "3":
    print("Vamos a actualizar un cliente")
elif opcion == "4":
    print("Vamos a eliminar a un cliente")
    
