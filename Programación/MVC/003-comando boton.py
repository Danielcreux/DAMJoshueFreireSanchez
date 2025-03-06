import tkinter as tk

def pulsaboton():
    print("Has pulsado el boton")

ventana = tk.Tk()                 #Creo una ventana

tk.Button(
    ventana,text="Púlsame",
    command = pulsaboton).pack(padx=50,pady=50)      #Creo un boton

ventana.mainloop()                #Atrapo la ejecucion