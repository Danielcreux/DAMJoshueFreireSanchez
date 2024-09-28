#Windows: pip install flask
from flask import Flask

aplicacion = Flask(__name__)

mensaje = {"resultado":"Ok"}
print(mensaje)
