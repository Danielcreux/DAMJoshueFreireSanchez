import pickle                                                                       # importo la libreria que me permite leer y escribir bloques de memoria

class Cliente:                                                                      #Creo una clase
    def __init__(self,nuevonombre,nuevosapellidos,nuevoemail,nuevadireccion):       #Creo un constructor con parametros
        self.nombre = nuevonombre                                                   #A las propiedades les paso los parametros del constructor
        self.apellidos = nuevosapellidos
        self.email = nuevoemail
        self.direccion = nuevadireccion

agenda = []                                                                         #Creo una agenda que de momento esté vacía
        
print("##################################")
print("Programa agenda v0.1 por Jose Vicente Carratalá")                            #Creo un mensaje de bienvenida
print("##################################")

while True:                                                                         #Escribo un bucle infinito
    
    print("Menú de navegación")                                                     #Imprimo un menú de navegación
    print("1.-Introduce un registro")
    print("2.-Listado de registros")
    print("3.-Guardar registros")
    print("4.-Leer registros")

    opcion = input("Selecciona una opcion:")                                        #Atrapo la opción del usuario
    print("Has cogido la opcion:",opcion)                                           #Le digo al usuario la opción que ha escogido

    if opcion == "1":                                                               #En el caso que el usuario escoja la opción 1
        print("Vamos a insertar un nuevo cliente")                                  #Le digo que vamos a insertar un cliente
        
        nombre = input("Introduce el nuevo nombre:")                                #Atrapo los datos que me proporciona el usuario
        apellidos = input("Introduce los nuevos apellidos:")
        email = input("Introduce el nuevo email:")
        direccion = input("Introduce la nueva direccion:")

        nuevocliente = Cliente(nombre,apellidos,email,direccion)                    #Creo una nueva instancia de la clase Cliente

        agenda.append(nuevocliente)                                                 #La anexo a la agenda 
        
    elif opcion == "2":                                                             #En el caso que el cliente escoja la opcion 2
        for cliente in agenda:                                                      #Para cada uno de los clientes de la agenda
            print("------------------")                                             #Imprimo cada uno de los clientes de forma bonita 
            print("nombre:",cliente.nombre)
            print("apellidos:",cliente.apellidos)
            print("email:",cliente.email)
            print("direccion:",cliente.direccion)
        
    elif opcion == "3":                                                             #En el caso que el cliente escoja la opcion 3
        archivo = open("agenda.bin",'wb')                                           #Abro un archivo binario en modo escritura binaria 
        pickle.dump(agenda,archivo)                                                 #Vierto el contenido de la agenda en el interior de ese archivo
        print("La agenda ha sigo guardada en un archivo")                           #Imprimo un mensaje de aviso
        archivo.close()                                                             #Cierro el archivo

    elif opcion == "4":                                                             #En el caso que el cliente escoja la opcion 4
        archivo = open("agenda.bin",'rb')                                           #Abro un archivo binario en modo escritura binaria
        agenda = pickle.load(archivo)                                               #En la agenda vierto el contenido del archivo del disco duro 
        archivo.close()                                                             #Cierro el archivo
        
    
        

