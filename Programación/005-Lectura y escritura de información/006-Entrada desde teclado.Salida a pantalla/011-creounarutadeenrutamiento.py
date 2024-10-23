#Windows: pip install flask
from flask import Flask                             #Importo la librería que me permite crear un miniservidor web                       

app = Flask(__name__)                               #Creo el servidor Web

@app.route('/')                                     #Creo un escuchador para que esté pendiente de cuando alguien entra en la raíz
def inicio():                                        #Defino una función se puede llamar como yo quiera
    contenido = '<p>Esta es la página de inicio<p>'  #Preparo un contenido
    return contenido                                 #Lanzo el contenido al navegador web   

app.run(debug=True)                              #Arranco el servidor 
    
mensaje = {"resultado":"ok"}
print(mensaje)
