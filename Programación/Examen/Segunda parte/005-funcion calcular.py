import tkinter as tk                       #Importo la libreria

ventana = tk.Tk();                         #Creo una ventana

operando1= tk.IntVar()                     #Esta variable almacena un entero



tk.Label(ventana,text="Introduce la base imponible").pack(padx=20,pady=4) #creo una etiqueta
tk.Entry(ventana,textvariable=operando1).pack(padx=20,pady=4)                                    #creo un campo

tk.Label(ventana,text="Calcula").pack(padx=20,pady=4) #creo una etiqueta
tk.Button(ventana,text="IVA",command= calcula).pack(padx=20,pady=4)       #creo un boton
resultado=tk.Label(ventana,text="-")       #creo un campo para el IVA 
resultado.pack(padx=20,pady=4)
