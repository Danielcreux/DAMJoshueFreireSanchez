'''
    Programa agenda en SQlite
    (c) 2024 por Joshué Daniel
    v 0.1 Empezando en clase 
'''

print("############################")
print("      Programa agenda       ")
print("  por Joshue Daniel Freire  ")
print("############################")

while True:
    
    print("Menú principal")
    print("1.-Crear un nuevo registro")
    print("2.-Listado de registros")
    print("3.-Actualización de registros")
    print("4.-Eliminación de registros")

    opcion = input("Selecciona una opcion:")

    if opcion == "1":
        print("Vamos a insertar un registro")
        
        nombre = input("Introduce un nuevo nombre:")
        apellido = input("Introduce un nuevo apellido:")
        email = input("Introduce un nuevo email:")
        direccion = input("Introduce una nueva direccion:")
        
    elif opcion == "2":
        print("Vamos a listar los registros")
    elif opcion == "3":
        print("Vamos a actualizar los registros")
    elif opcion == "4":
        print("Vamos a eliminar un registro")


