import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="miemepresa",
    password="miempresa",
    database="miempresa"
)


cursor = connection.cursor()

print("Programa de gestión de empresa v0.1")                            #Mensaje de bienvenida
print("por Joshué Daniel")

print("Selecciona una tabla de la base de datos:")                      #Se invita a seleccionar una opción

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
print("Vamos a trabajar con la entidad:",tablas[int(opcion)])           #Comprobamos que todo va bien
peticion = "SELECT * FROM"  +tablas [int(opcion)]
print("La petición que voy a tirar contra la base de datos es:" +peticion)

