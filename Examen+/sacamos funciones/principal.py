import pickle  # importo la librería que permite leer y escribir bloques de memoria
from clasecliente import *
from bienvenida import *
from menu import *
from funciones.funcion import *

agenda = []  # Creo una agenda vacía  

while True:  # Bucle infinito para el menú de navegación
    bienvenida()
    
    menu()

    opcion = input("Selecciona una opción: ")  # Capturo la opción del usuario
    print("Has escogido la opción:", opcion)  # Muestro la opción seleccionada

    if opcion == "1":
        insertar()      # Si el usuario escoge la opción 1   
    elif opcion == "2":  # Si el cliente escoge la opción 2
        listar()  
    elif opcion == "3":  # Si el cliente escoge la opción 3
        guardar()  
    elif opcion == "4":
        cargar()        # Si el cliente escoge la opción 4
    else:
      print("Opción no válida. Por favor, selecciona una opción del menú.")


















































































































                 
  
