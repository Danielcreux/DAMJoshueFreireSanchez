import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="miemepresa",
    password="miempresa",
    database="miempresa"
)


cursor = connection.cursor()

####################Introducción###########################

print("Programa de gestión de empresa v0.1")                            #Mensaje de bienvenida
print("por Joshué Daniel")

print("Selecciona una tabla de la base de datos:")                      #Se invita a seleccionar una opción

###################Menú nuvel 1:entidades########################

peticion = "SHOW TABLES;"                                               #Selecciona de forma dinámica todas las tablas de las bases de datos 

cursor.execute(peticion)                                                #Ejecuto la petición en el servidor de MYSQL 
filas = cursor.fetchall()                                               #Recupero los datos
tablas = []                                                             #Como los datos vienen raros, creo una lista vacía

for fila in filas:                                                      #Para cada una de las filas
    tablas.append(fila[0])                                              #Meto el dato limpio en la lista 
contador = 0                                                            #Creo un contador en cero                    
for tabla in tablas:                                                    #Para cada una de las tablas en la lista
    print(contador,"-",tabla)                                           #La saco por pantalla y le asigno un número
    contador+=1                                                         #Cada vez que paso por aquí subo un número
opcion = input("Selecciona una opcion:")                                #Selecciona una opción
          
print("La petición que voy a tirar contra la base de datos es:" +peticion)

#####################Menú nivel 2 Crud dentro de una entidad#######

print("Vamos a trabajar con la entidad:  " tablas[int(opcion)]+":")     #Comprobación que todo va bien 
print("1.-Introduce un nuevo " +tablas[int(opcion)]+":")                #Imprimo el menú CRUD y este si que es estático
print("2.-Listar " +tablas[int(opcion)]+":")   
print("3.-Introduce un nuevo " +tablas[int(opcion)]+":")
print("4.-Eliminar " +tablas[int(opcion)]+":")


opcionnivel2 = input("Selecciona una opcion:")                          #Selecciona una opción

if opcionnivel2 == "1":                                                 #Atrapo las opciones
    print("Vamos a insertar un nuevo  ",tablas[int(opcion)])
elif opcionnivel2 == "2":                                               #En el caso que sea un listado
    print("Vamos a listar  ",tablas[int(opcion)])                       #Aviso la operación que voy a realizar
    peticion = " SELECT * FROM "  +tablas [int(opcion)]                 #Creo una petición DINÁMICA ######################
    cursor.execute(peticion)                                            #Ejecuto la petición 
    filas = cursor.fetchall()                                           #Cargo el resultado
    for fila in filas:                                                  #Repaso las filas
        print(fila)                                                     #Imprimo las filas 
elif opcionivel2 == "3":
    print("Vamos a actualizar ",tablas[int(opcion)])
elif opcionivel2 == "4":
    print("Vamos a eliminar ",tablas[int(opcion)])    
    
