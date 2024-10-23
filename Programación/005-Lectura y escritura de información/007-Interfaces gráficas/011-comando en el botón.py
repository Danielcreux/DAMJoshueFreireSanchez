import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500+40+40")
ventana.title("El programa de Joshué")

tk.Label(ventana,text="Hola mi primer programa").pack(padx=10,pady=10)

tk.Entry(ventana).pack(padx=10,pady=10)

tk.Button(ventana,text="Pruébame",command=ejecutaAlgo).pack(padx=10,pady=10)

ventana.mainloop()
