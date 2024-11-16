class Cliente:
    def __init__(self,nuevoid,nuevonombre,nuevosapellidos,nuevoemail):
        self.id = nuevoid
        self.nombre = nuevonombre
        self.apellido = nuevoapellidos
        self.email = nuevoemail

class Productos:
    def __init__(self,nuevoid,nuevonombre,nuevadescripcion,nuevoprecio):
        self.id = nuevoid
        self.nombre = nuevonombre
        self.descripcion = nuevadescripcion
        self.precio = nuevoprecio

cliente1 = Cliente(1,"Joshue Daniel","Freire","info@joshue.com")   #Probar siempre el programa

