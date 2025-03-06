import subprocess
import tkinter as tk
                         
ventana = tk.Tk()

archivo = open("modelo.txt",'r')
linea = archivo.readlines()
campos = linea.split(",")
print(campos)

for campo in campos:
    tk.Label(ventana,text="Introduce un nuevo valor para "+campo+": ").pack(padx=10,pady=10)
    tk.Entry(ventana).pack(padx=10,pady=10)
ventana.mainloop()


