import os  #sirve para trabajar con el sistema tambien shutils#

try:
    os.makedirs("basededatos")
except:
    print("La carpeta de base de datos ya existe,continuemos...")

