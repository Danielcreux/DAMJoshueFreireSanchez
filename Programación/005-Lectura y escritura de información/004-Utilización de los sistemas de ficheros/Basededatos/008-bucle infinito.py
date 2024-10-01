import os                                                                               #Importa la libreria que nos permite interactuar con el sistema operativo
                                                                                         

try:                                                                                    #Intento realizar una operacion
    os.makedirs("basededatos")                                                          #Intento crear la carpeta base de datos
except:                                                                                 #En el caso que no pueda 
    print("La carpeta de base de datos ya existe,continuemos...")                       #No des error y solo continua                  

print("Bienvenidos a mi querido diario v0.2")                                           #Imprime un mensaje de bienvenida
while(True):                                                                            #entro en un bucle infinito
    print("Selecciona una de las siguiente opciones")                                   #informo al usuario que va a tener que elegir una opcion
    print("1-Introducir un nuevo registro")                                             #le informo de la opcion 1
    print("2-Leer registros existente")                                                 #le informo de la opcion 2
    opcion = input("Selecciona una de las siguientes opciones:")                        #Atrapo su opción elegida y la meto en una variable
    print("La opcion que has seleccionado es:", opcion)                                 #Imprimo la variable por pantalla

    if opcion == "1":                                                                   #Si es cierto que el usuario ha cogido la opcion 1
        print("Has elegido introducir un nuevo registro")                               #Le informo que ha cogido la opcion 1
        archivo = open("basededatos/miqueridodiario.txt",'w')                           #Abro la base de datos en modo añadir
        fecha = input("Introduce la fecha:")                                            #Le pido la fecha
        mensaje = input("Introduce el mensaje")                                         #Le pido el mensaje
        archivo.write(fecha+"|"+mensaje+"\n")
        archivo.close()
    elif opcion == "2":
        print("Has elegido leer los registros")
        archivo = open("basededatos/miqueridodiario.txt",'r')
        lineas = archivo.readlines()
        for linea in linea:
            print(linea)
    else:
        print("La opcion que has elegido no es valida")
        


