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
producto=[]                                                                  #crear lista vacia para enlistar productos

def seleccion():
         print("#######################")
         print("Seleccione lo que desea realizar:")                  #Esto ya es parte del menú CRUD
         print("1-Insertar registros")
         print("2-leer registros")
         print("3-actualizar registros")
         print("4-Eliminar registro")
         print("5.-Guardar registro")
         print("6.-Cargar")
         print("#######################")
         opcion = input("Inserte que operacion:")                      #Atrapo la opcion del usuario


         if opcion == "1":                                              #Al seleccionar la opcion 1
             print("#######################")
             print("Insertamos un nuevo registro")
             identificador = input("Introduce el id del nuevo cliente")
             nombre = input("Introduce el nombre del nuevo cliente")
             apellidos = input("Introduce los apellidos del nuevo cliente")
             email = input("Introduce el email del nuevo cliente")
             cliente.append(clientes(identificador,nombre,apellidos,email))    #El ingreso que hacemos en la lista vacía
             
             
         elif opcion == "2":
             print("Listamos los registros")
             contador = 0
             for clientes in cliente:
                 print("-------------")
                 print("identificador:"+clientes.identificador)
                 print("nombre:"+clientes.nombre)
                 print("apellidos:"+clientes.apellido)
                 print("email:"+clientes.email)
                 contador += 1
                 
         elif opcion == "3":
             print("Actualizamos el registro")
             idlista = input("Selecciona el elemento de sla lista de Python:")              #Imprimo un mensaje
             identificador = input("Introduce el id del cliente modificado:")
             nombre = input("Introduce el nombre del cliente modificado:")                                                                            #Introduzco los datos que pido
             apellidos = input("Introduce el apellido del cliente modificado:")
             email = input("Introduce el email del nuevo cliente:")                      #Creo una nueva instancia
             cliente[int(idlista)].identificador = identificador
             cliente[int(idlista)].nombre = nombre
             cliente[int(idlista)].apellidos = apellidos
             cliente[int(idlista)].email = email

         elif opcion == "4":
             print("Eliminar el registro")
             idlista = input("Seleccione el elemento de la lista de Python:")
             cliente.pop(int(idlista))

         elif opcion == "5":
             archivo = open("cliente.dat",'wb')
             pickle.dump(cliente,archivo)
             archivo.close()

         elif opcion == "6":
             archivo = open("cliente.dat",'rb')
             cliente  = pickle.load(archivo)
             archivo.close()

def manejar_productos():               
         print("#######################")
         
         print("Seleccione lo que desea realizar:")                  #Esto ya es parte del menú CRUD
         print("1-Insertar productos")
         print("2-leer productos")
         print("3-actualizar productos")
         print("4-Eliminar productos")
         print("5.-Guardar productos")
         print("6.-Cargar")
         
         opcion = input("Inserte que operacion:")                      #Atrapo la opcion del usuario


         if opcion == "1":                                              #Al seleccionar la opcion 1
             print("#######################")
             print("Insertamos un nuevo producto")
             id = input("Introduce el id del nuevo producto:")
             articulo = input("Introduce el nombre del nuevo producto:")
             descripcion = input("Introduce la descripcion del nuevo producto:")
             precio = input("Introduce el precio del nuevo producto:")
             producto.append(productos(id,articulo,descripcion,precio))    #El ingreso que hacemos en la lista vacía
             
             
         elif opcion == "2":
             print("Listamos los producto")
             contador = 0
             for producto in productos:
                 print("-------------")
                 print("identificador:"+productos.ident)
                 print("articulo:"+productos.articulo)
                 print("descripcion:"+productos. descripcion)
                 print("precio:"+productos.precio)
                 contador += 1
                 
         elif opcion == "3":
             print("Actualizamos el registro")
             idlista = input("Selecciona el elemento de la lista de Python:")              #Imprimo un mensaje
             id = input("Introduce el id del producto modificado:")
             articulo = input("Introduce el nombre del producto modificado:")                                                                            #Introduzco los datos que pido
             descripcion = input("Introduce el apellido del producto modificado:")
             precio = input("Introduce el email del nuevo producto:")                      #Creo una nueva instancia
             producto[int(idlista)].id = id
             producto[int(idlista)].articulo = articulo
             producto[int(idlista)].descripcion = descripcion
             producto[int(idlista)].precio = precio

         elif opcion == "4":
             print("Eliminar el producto")
             idlista = input("Seleccione el elemento de la lista de Python:")
             producto.pop(int(idlista))

         elif opcion == "5":
             archivo = open("producto.dat",'wb')
             pickle.dump(producto,archivo)
             archivo.close()
             print("Se he guardado el archivo")

         elif opcion == "6":
             archivo = open("producto.dat",'rb')
             producto  = pickle.load(archivo)
             archivo.close()
             print("Se he cargado el archivo")
         
    
 
