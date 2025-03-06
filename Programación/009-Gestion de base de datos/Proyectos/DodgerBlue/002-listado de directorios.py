import os

ruta = "C:/xampp/htdocs/programacion/DAMJoshueFreireSanchez/"

carpetas = os.listdir(ruta)

for carpeta in carpetas:
    print(carpeta)
