def bienvenida ():
print("Bienvenido a mi agenda")
print("Agenda v0.1 por Joshué Daniel Freire")

def muestramenu():
    print("Menú principal")
    print("1.-Insertar un registro")
    print("2.-Leer registros")
    print("1.-Actualizar un registro")
    print("1.-Eliminar registros")

def insertar():
     print("Vamos a insertar un registro")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")

def listar():
     print("Vamos a listar registros")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")

def actualizar():
     print("Vamos a actualizar registros")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")

def eliminar():
     print("Vamos a eliminar registros")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")
     print("acción")

    
    
bienvenida()

while True:
    
    muestraMenu()
    
    entrada = input("Seleccion una opcion:")

     if entrada == "1":
         insertar()
     elif entrada == "2":
         listar()
     elif entrada == "3":
         actualizar()
     elif entrada == "4":
         eliminar()
