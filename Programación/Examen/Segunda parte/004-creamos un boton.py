import tkinter as tk                       #Importo la libreria

ventana = tk.Tk();                         #Creo una ventana

operando1= tk.IntVar()                     #Esta variable almacena un entero


tk.Label(ventana,text="Introduce la base imponible").pack(padx=20,pady=4) #creo una etiqueta
tk.Entry(ventana,textvariable=operando1).pack(padx=20,pady=4)                                    #creo un campo

tk.Label(ventana,text="Pulsa para ejecutar").pack(padx=20,pady=4) #creo una etiqueta
tk.Button(ventana,text="Vamos alla!",command= calcula).pack(padx=20,pady=4)       #creo un boton

