import tkinter as tk

ventana = tk.TK()

def saluda():
    print("Yo te saludo")
    
boton = tk.Button(
    ventana,text="Pulsame")
boton.pack(padx=50,pady=50)
