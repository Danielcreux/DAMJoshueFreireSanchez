import requests
import time

url = "http://localhost:8080/programacion/DAMJoshueFreireSanchez/Lenguaje%20de%20Marcas/003-Manipulaci%C3%B3n%20de%20documentos%20web/Proyecto/Apple/055-organizar/front/"
for _ in range(0,1000):
    try:
        response = requests.get(url)
        #Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            #print("Contenido de la página:")
            #print(response.text) #Imprime el contenido de la página
            print("OK")
            #pass
        else:
            print(f"Error en la solicitud: {response.status_code}")
    except requests.execptions.RequestException as e:
        print(f"Error al cargar la URL: {e}")

    #time.sleep(1)
