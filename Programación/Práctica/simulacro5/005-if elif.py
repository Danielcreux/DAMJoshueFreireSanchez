class clientes:
     def __init__(self,nuevoid,nuevonombre,nuevosapellidos,nuevoemail):
        self.identificador = nuevoid
        self.nombre = nuevonombre
        self.apellido = nuevoapellidos
        self.email = nuevoemail
        
class productos:
    def __init__(self,nuevoid,nuevoarticulo, nuevadescripcion,nuevoprecio):
        self.id= nuevoid
        self.articulo   = nuevoarticulo
        self.descripcion  = nuevadescripcion
        self.precio    = nuevoprecio


clientes=[]
productos=[]

while True:
    print("Programa Crud")
    print("Nueva version")
    print("#######################")
    print("Seleccione la entidad:")
    print("1-Cliente:")
    print("2-Producto:")
    opcion = input("Insertar opcion a escoger:")
    
    print("#######################")
    
    print("Seleccione lo que desea realizar:")
    print("1-Insertar registros")
    print("2-Leer registros")
    print("3-actualizar registros")
    print("4-Eliminar registro")
    entidad = input("Inserte que operacion:")

    if entidad == "1":
        print("Insertamos un nuevo registro")
    elif entidad == "2":
        print("Listamos los registros")
    elif entidad == "3":
        print("Actualizamos el registro")
    elif entidad == "4":
        print("Eliminar el registro")


    
    
 
