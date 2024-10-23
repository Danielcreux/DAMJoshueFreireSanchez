import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500+40+40")
ventana.title("El programa de Joshué")

def ejecutaAlgo():
    print("veo que le has dado al botón")
    global texto                          
    texto.config(text="Este texto te lo escribo desde python")
    
texto = tk.Label(
    ventana,
    text="Hola mi primer programa"
    )                                           #Aqui creo un texto en memoria
texto.pack(padx=10,pady=10)                 #Ahora añado el texto a la interfaz

tk.Entry(ventana).pack(padx=10,pady=10)

tk.Button(
    ventana,
    text="Pruébame",
    command=ejecutaAlgo
    ).pack(padx=10,pady=10)

ventana.mainloop()
