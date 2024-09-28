#Windows: pip install flask
from flask import Flask                                 #Importo la libreria que me permite crear un miniservidor web

aplicacion = Flask(__name__)                            #Creo el servidor web

@aplicacion.route('/')                                  #Creo un escuchador para que esté pendiente cuando alguien entra
def inicio():                                           #Defino una función se puede llamar como yo quiera
    contenido = {"resultado":"ok"}                       #Preparo un contenido
    return contenido                                    #Lanzo el contenido al navegador web    

aplicacion.run(debug=True)
