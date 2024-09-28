import os  #sirve para trabajar con el sistema tambien shutils#

try:
    os.makedirs("basededatos")
except:
    print("La carpeta de base de datos ya existe,continuemos...")

print("Bienvenidos a mi querido diario v0.2")
print("Selecciona una de las siguiente opciones")
print("1-Introducir un nuevo registro")
print("2-Leer registros existente")


