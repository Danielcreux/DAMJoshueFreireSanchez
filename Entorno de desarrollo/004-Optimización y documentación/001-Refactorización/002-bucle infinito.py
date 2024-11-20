print("Bienvenida a mi agenda")
print("agenda v0.1 por Joshué Freire")

while True:
    print("Menú principal")
    print("1.-Insertar un registro")
    print("2.-Leer registro")
    print("3.-Actualizar un registro")
    print("4.-Eliminar registros")

    entrada = input("Selecciona una opcion:")

    if entrada == "1":
        print("Vamos a insertar un registro")
    elif entrada == "2":
        print("Vamos a listar registros")
    elif entrada == "3":
        print("Vamos a actualizar un registros")
    elif entrada == "4":
        print("Vamos a eliminar registros")
