from funciones import manejar_clientes, manejar_productos


while True:
            print("\n#######################")
            print("Programa CRUD")
            print("Nueva versión")
            print("#######################")
            print("Seleccione la entidad:")
            print("1 - Cliente")
            print("2 - Producto")
            entidad = input("Insertar opción a escoger: ")

            if entidad == "1":
                manejar_clientes()
            elif entidad == "2":
                manejar_productos()
            else:
                print("Saliendo del programa")
                break
        


