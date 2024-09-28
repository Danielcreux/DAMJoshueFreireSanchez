import os  #sirve para trabajar con el sistema tambien shutils#

try:
    os.makedirs("basededatos")
except:
    print("La carpeta de base de datos ya existe,continuemos...")

print("Bienvenidos a mi querido diario v0.2")
print("Selecciona una de las siguiente opciones")
print("1-Introducir un nuevo registro")
print("2-Leer registros existente")
opcion = input("Selecciona una de las siguientes opciones:")
print("La opcion que has seleccionado es:", opcion)

if opcion == "1":
    print("Has elegido introducir un nuevo registro")
    archivo = open("basededatos/miqueridodiario.txt",'w')
    fecha = input("Introduce la fecha:")
    mensaje = input("Introduce el mensaje")
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
    

