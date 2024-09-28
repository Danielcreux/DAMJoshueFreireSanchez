'''
    Programa CRUD completo
    v0.1 Joshué Daniel Freire
    El objetivo de este programa es construir el CRUD completo contra MySQL
'''
import mysql.connector

servidor = "localhost"
usuario ="miempresa"
contrasena = "miempresa"
base_de_datos = "miempresa"


conexion = mysql.connector.conect(
    host=servidor,
    database=base_de_datos,
    user=usuario,
    password=contrasena
    )

print("#############")
print("Programa completo sobre clientes")
print("#############")

while True:

    print("Selecciona una opción")
    print("1-Crear nuevo cliente")
    print("2-Leer clientes existentes")
    print("3-Actualizar clientes existentes")
    print("4-Eliminar cliente")
    print("5-Salir del programa")

    opcion = input("Seleccionar una de las opciones:")
    print("Has seleccionado la opcion:", opcion)

    if opcion == "1":
        print("Vamos a insertar un nuevo cliente")
        nombre = input("Introduce un nuevo nombre:")
        apellidos = input("introduce los nuevos apellidos:")
        email = input("Introduce el email:")
        poblacion = input("Introduce la población:")
        fecha de nacimiento = input("Introduce la fecha de nacimiento")
       
        
    elif opcion == "2":
        print("Vamos a listar los clientes")
    elif opcion == "3":
        print("Vamos a actualizar a un cliente")
    elif opcion == "4":
        print("Vamos a eliminar a un cliente")
    elif opcion == "5":
        exit()
    else:
        print("Lo que has escogido no es una opción válida")
