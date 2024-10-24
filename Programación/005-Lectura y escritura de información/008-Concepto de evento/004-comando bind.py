import tkinter as tk

ventana = tk.Tk()

def saluda(event):
    print("Yo te saludo")
    
boton = tk.Button(
    ventana,text="Pulsame")
boton.pack(padx=50,pady=50)

boton.bind("<Button-1>",saluda)
