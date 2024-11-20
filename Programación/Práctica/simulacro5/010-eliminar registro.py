import pickle

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
    print("5.-Guardar registro")
    print("6.-Cargar")
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
        contador = 0
        for clientes in cliente:
            print("-------------")
            print("identificador:"+clientes.identificador)
            print("nombre:"+clientes.nombre)
            print("apellidos:"+clientes.apellido)
            print("email:"+clientes.email)
            contador += 1
            
    elif entidad == "3":
        print("Actualizamos el registro")
        idlista = input("Selecciona el elemento de la lista de Python:")              #Imprimo un mensaje
        identificador = input("Introduce el id del cliente modificado:")
        nombre = input("Introduce el nombre del cliente modificado:")                                                                            #Introduzco los datos que pido
        apellidos = input("Introduce el apellido del cliente modificado:")
        email = input("Introduce el email del nuevo cliente:")                      #Creo una nueva instancia
        cliente[int(idlista)].identificador = identificador
        cliente[int(idlista)].nombre = nombre
        cliente[int(idlista)].apellidos = apellidos
        cliente[int(idlista)].email = email

    elif entidad == "4":
        print("Eliminar el registro")
        idlista = input("Seleccione el elemento de la lista de Python:")
        cliente.pop(int(idlista))

   
    
    
 
