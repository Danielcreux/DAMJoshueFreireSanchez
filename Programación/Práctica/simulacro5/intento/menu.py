
from funciones import *

def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. CRUD Clientes")
        print("2. CRUD Productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_crud_clientes()
        elif opcion == '2':
            menu_crud_productos()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


def menu_crud_clientes():
    while True:
        print("\n=== CRUD Clientes ===")
        print("1. Crear Cliente")
        print("2. Listar Clientes")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_cliente()
        elif opcion == '2':
            listar_clientes()
        elif opcion == '3':
            actualizar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")


def menu_crud_productos():
    while True:
        print("\n=== CRUD Productos ===")
        print("1. Crear Producto")
        print("2. Listar Productos")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_producto()
        elif opcion == '2':
            listar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")


# Iniciar programa
if __name__ == '__main__':
    menu()
