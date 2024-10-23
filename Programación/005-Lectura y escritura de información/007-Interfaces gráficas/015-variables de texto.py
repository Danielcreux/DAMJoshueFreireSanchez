import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500+40+40")
ventana.title("El programa de Joshué")

contenidocampo1 = tk.StringVar()            #Defino una variable de tipo tk para almacenar la info de un campo
    
def ejecutaAlgo():
    print("veo que le has dado al botón")
    contenido_del_campo = contenidocampo1.get()
    print(contenido_del_campo)
    global texto                          
    texto.config(text="Este texto te lo escribo desde python")
    
texto = tk.Label(
    ventana,
    text="Hola mi primer programa"
    )                                           #Aqui creo un texto en memoria
texto.pack(padx=10,pady=10)                 #Ahora añado el texto a la interfaz

tk.Entry(ventana,textvariable=contenidocampo1
         ).pack(padx=10,pady=10)

tk.Button(
    ventana,
    text="Pruébame",
    command=ejecutaAlgo
    ).pack(padx=10,pady=10)

ventana.mainloop()
