import os
import time
from datetime import datetime
try:
    os.mkdir("/Users/Valentina/Documents/Joshue/backups/" )
except:
    print("la carpeta ya existe,continuamos...")

ahora = datetime.now()
fecha = ahora.strftime("%Y-%m-%d-%H-%M-%S")
epoch = str(round(time.time()))
fechacompuesta = fecha+"_"+epoch
print(fechacompuesta)
os.mkdir("/Users/Valentina/Documents/Joshue/backups/"+fechacompuesta)
