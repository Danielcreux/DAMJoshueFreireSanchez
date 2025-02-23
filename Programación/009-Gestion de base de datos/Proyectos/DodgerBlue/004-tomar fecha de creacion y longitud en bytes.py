import os
from datetime import datetime

ruta = "C:/xampp/htdocs/programacion/DAMJoshueFreireSanchez/Programación"

for directorio_raiz,subcarpetas,archivos in os.walk(ruta):
    for archivo in archivos:
        ruta_completa = os.path.join(directorio_raiz, archivo)
        print(ruta_completa)

        #Obtener el tiempo de última modifciación
        tiempo_modificacion = os.path.getmtime(ruta_completa)
        fecha_modificacion = datetime.fromtimestamp(tiempo_modificacion)

        #Obtener el tamaño en bytes
        tamano_bytes = os.path.getsize(ruta_completa)

        #Mostrar información
        print(f"Ruta: {ruta_completa}")
        print(f"Última modificación : {fecha_modificacion}")
        print(f"Tamaño (bytes) : {tamano_bytes}")
        print("-" * 40)
        
