import pickle

# Clase Cliente
class Cliente:
    def __init__(self, id, nombre, apellidos, email):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre} {self.apellidos}, Email: {self.email}"


# Clase Producto
class Producto:
    def __init__(self, id, nombre, descripcion, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Precio: {self.precio}"


# Funciones para manejar persistencia
def guardar_datos(nombre_archivo, datos):
    with open(nombre_archivo, 'wb') as f:
        pickle.dump(datos, f)


def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []


# Archivos de persistencia
ARCHIVO_CLIENTES = 'clientes.pkl'
ARCHIVO_PRODUCTOS = 'productos.pkl'

# Carga de datos al iniciar el programa
clientes = cargar_datos(ARCHIVO_CLIENTES)
productos = cargar_datos(ARCHIVO_PRODUCTOS)


# Funciones CRUD
def crear_cliente():
    id = input("Ingrese ID del cliente: ")
    nombre = input("Ingrese nombre del cliente: ")
    apellidos = input("Ingrese apellidos del cliente: ")
    email = input("Ingrese email del cliente: ")
    cliente = Cliente(id, nombre, apellidos, email)
    clientes.append(cliente)
    guardar_datos(ARCHIVO_CLIENTES, clientes)
    print("Cliente creado con éxito.")


def listar_clientes():
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for cliente in clientes:
            print(cliente)


def actualizar_cliente():
    id = input("Ingrese el ID del cliente a actualizar: ")
    for cliente in clientes:
        if cliente.id == id:
            cliente.nombre = input("Ingrese el nuevo nombre: ")
            cliente.apellidos = input("Ingrese los nuevos apellidos: ")
            cliente.email = input("Ingrese el nuevo email: ")
            guardar_datos(ARCHIVO_CLIENTES, clientes)
            print("Cliente actualizado con éxito.")
            return
    print("Cliente no encontrado.")


def eliminar_cliente():
    id = input("Ingrese el ID del cliente a eliminar: ")
    global clientes
    clientes = [cliente for cliente in clientes if cliente.id != id]
    guardar_datos(ARCHIVO_CLIENTES, clientes)
    print("Cliente eliminado con éxito.")


def crear_producto():
    id = input("Ingrese ID del producto: ")
    nombre = input("Ingrese nombre del producto: ")
    descripcion = input("Ingrese descripción del producto: ")
    precio = float(input("Ingrese precio del producto: "))
    producto = Producto(id, nombre, descripcion, precio)
    productos.append(producto)
    guardar_datos(ARCHIVO_PRODUCTOS, productos)
    print("Producto creado con éxito.")


def listar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        for producto in productos:
            print(producto)


def actualizar_producto():
    id = input("Ingrese el ID del producto a actualizar: ")
    for producto in productos:
        if producto.id == id:
            producto.nombre = input("Ingrese el nuevo nombre: ")
            producto.descripcion = input("Ingrese la nueva descripción: ")
            producto.precio = float(input("Ingrese el nuevo precio: "))
            guardar_datos(ARCHIVO_PRODUCTOS, productos)
            print("Producto actualizado con éxito.")
            return
    print("Producto no encontrado.")


def eliminar_producto():
    id = input("Ingrese el ID del producto a eliminar: ")
    global productos
    productos = [producto for producto in productos if producto.id != id]
    guardar_datos(ARCHIVO_PRODUCTOS, productos)
    print("Producto eliminado con éxito.")



