import tkinter as tk

class cliente():
    def __init__(self):
        self.nombre="" 
        self.apellidos=""

def pulsaboton():
    print("Has pulsado el boton")

ventana = tk.Tk()                 #Creo una ventana

tk.Label(ventana,text="Introduce un nombre").pack(padx=10,pady=10)
tk.Entry(ventana).pack(padx=10,pady=10)

tk.Label(ventana,text="Introduce un apellido").pack(padx=10,pady=10)
tk.Entry(ventana).pack(padx=10,pady=10)

tk.Button(
    ventana,text="Púlsame",
    command = pulsaboton).pack(padx=50,pady=50)      #Creo un boton

ventana.mainloop()                #Atrapo la ejecucion