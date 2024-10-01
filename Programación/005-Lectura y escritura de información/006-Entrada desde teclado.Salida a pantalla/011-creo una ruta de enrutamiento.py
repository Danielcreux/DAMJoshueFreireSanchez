#Windows: pip install flask
from flask import Flask                                 #Importo la libreria que me permite crear un miniservidor web

aplicacion = Flask(__name__)                            #Creo el servidor web

@aplicacion.route('/')                                  #Creo un escuchador para que esté pendiente cuando alguien entra
def inicio():                                           #Defino una función se puede llamar como yo quiera
    contenido = '<p>Esta es la página de inicio</p>'    #Preparo un contenido
    return contenido                                    #Lanzo el contenido al navegador web    

if __name__ == '__main__':                              #Arranco el servidor
    app.run(debug=True)
    
mensaje = {"resultado":"Ok"}
print(mensaje)
