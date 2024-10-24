class Cliente:                                                                  #Defino una clase cliente
    def __init__(self,nuevoid,nuevonombre,nuevosapellidos,nuevoemail):
        self.identificador = nuevoid
        self.nombre = nuevonombre
        self.apellido = nuevosapellidos
        self.email = nuevoemail

class Productos:                                                               #Defino una clase producto
    def __init__(self,nuevoid,nuevonombre,nuevadescripcion,nuevoprecio):
        self.id = nuevoid
        self.nombre = nuevonombre
        self.descripcion = nuevadescripcion
        self.precio = nuevoprecio
        
clientes = []                                                                  #Creo una lista vacia que es donde voy a guardar a los clientes
productos = []                                                                 #Creo una lista vacia que es donde voy a guardar a los productos

print("Programa de consola")                                                   #Imprimo mensaje de bienvenida
print("v0.1 por Joshue Daniel")                                                #Imprimo el autor

while True:                                                                    #Entro en un bucle infinito
    print("#########################")                                         #Imprimo un separador visual
    print("Selecciona entidad")                                                #Invito a seleccionar una entidad
    print("1.-Clientes")
    print("2.-Productos")

    entidad = input("Indica la opcion seleccionada:")                           #Atrapo el valor de entidad

    print("Selecciona operacion")                                               #Ahora muestro el menu de operaciones
    print("1.-Insertar un nuevo registro")
    print("2.- Listar registros")
    print("3.- Actualizar registro")
    print("4.- Eliminar registro")

    opcion = input("Selecciona una de estas operaciones:")                      #Atrapo la opcion del usuario                     

    if opcion == "1":
        print("Insertamos un nuevo registro")                                   #Empezamos insertando un registro 
        identificador = input("Introduce el id del nuevo cliente:")              #Imprimo un mensaje
        nombre = input("Introduce el nombre del nuevo cliente:")                 #Introduzco los datos que pido
        apellidos = input("Introduce los apellidos del nuevo cliente:")
        email = input("Introduce el email del nuevo cliente:")                      #Creo una nueva instancia
        clientes.append(Cliente(identificador,nombre,apellidos,email))                                                 #Añado la instancia a la lista clientes        

    elif opcion == "2":
        print("Listamos los registros")
        contador = 0
        for cliente in clientes:
            print("-------------")
            print("id:"+cliente.identificador)
            print("nombre:"+cliente.nombre)
            print("apellidos:"+cliente.apellidos)
            print("email:"+cliente.email)
            contador += 1
          
    elif opcion == "3":
        print("Actualizamos el registro")
    elif opcion == "4":
        print("Eliminar el registro")
        


