
class clientes:
     def __init__(self,nuevoidentificador,nuevonombre,nuevosapellidos,nuevoemail):       #definir clase cliente
        self.identificador = nuevoidentificador
        self.nombre = nuevonombre
        self.apellido = nuevosapellidos
        self.email = nuevoemail
        
class productos:
    def __init__(self,nuevoid,nuevoarticulo, nuevadescripcion,nuevoprecio):              #definir clase producto
        self.id= nuevoid
        self.articulo   = nuevoarticulo
        self.descripcion  = nuevadescripcion
        self.precio    = nuevoprecio

cliente=[]                                                                      #crear lista vacia para enlistar clientes
productos=[]                                                                    #crear lista vacia para enlistar productos
                 
while True:
    print("#######################")                               #Bienvenido a la consola
    print("Programa Crud")
    print("Nueva version")
    print("#######################")
    print("Seleccione la entidad:")                               #En que clase nos queremos adentrar
    print("1-Cliente:")
    print("2-Producto:")
    opcion = input("Insertar opcion a escoger:")                  #Atrapo la opcion del usuario
    
    print("#######################")
    
    print("Seleccione lo que desea realizar:")                  #Esto ya es parte del menú CRUD
    print("1-Insertar registros")
    print("2-leer registros")
    print("3-actualizar registros")
    print("4-Eliminar registro")
    print("#######################")
    entidad = input("Inserte que operacion:")                      #Atrapo la opcion del usuario


    if entidad == "1":                                              #Al seleccionar la opcion 1
         print("#######################")
        print("Insertamos un nuevo registro")
        identificador = input("Introduce el id del nuevo cliente")
        nombre = input("Introduce el nombre del nuevo cliente")
        apellidos = input("Introduce los apellidos del nuevo cliente")
        email = input("Introduce el email del nuevo cliente")
        cliente.append(clientes(identificador,nombre,apellidos,email))    #El ingreso que hacemos en la lista vacía
        
        
    elif entidad == "2":
        print("Listamos los registros")
    elif entidad == "3":
        print("Actualizamos el registro")
    elif entidad == "4":
        print("Eliminar el registro")


    
    
 
