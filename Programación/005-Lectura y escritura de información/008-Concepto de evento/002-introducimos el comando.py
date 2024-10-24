import tkinter as tk

ventana = tk.TK()

def saluda():
    print("Yo te saludo")
    
tk.Button(ventana,text="Pulsame",command = saluda).pack(padx=50,pady=50)
