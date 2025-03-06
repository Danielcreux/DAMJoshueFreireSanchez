import os
import time
from datetime import datetime
import shutil

try:                                                                        #Intento
    os.mkdir("/Users/Valentina/Documents/Joshue/backups/" )                 #Crear la carpeta de backups
except:                                                                     #En el caso que de error
    print("la carpeta ya existe,continuamos...")                            #Saco un mensaje por consola

ahora = datetime.now()                                                      #Atrapo el tiempo actual
fecha = ahora.strftime("%Y-%m-%d-%H-%M-%S")                                 #Lo formateo en un formato humanamente entendible
epoch = str(round(time.time()))                                             #Obtengo la era unix
fechacompuesta = fecha+"_"+epoch                                            #Creo una fecha compuesta
print(fechacompuesta)                                                       #Imprimo la fecha 
#os.mkdir("/Users/Valentina/Documents/Joshue/backups/"+fechacompuesta)       #Creo un directorio con la fecha compuesta
origen = "C:/xampp/htdocs/programacion/DAMJoshueFreireSanchez/Lenguaje de Marcas/003-Manipulación de documentos web/Proyecto/Apple/091-Cargo un articulo al blog"
destino = "/Users/Valentina/Documents/Joshue/backups/"+fechacompuesta+"/basededatos"
shutil.copytree(origen, destino) 
 
