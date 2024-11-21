import tkinter as tk                       #Importo la libreria

ventana = tk.Tk();                         #Creo una ventana

operando1= tk.IntVar()                     #Esta variable almacena un entero

def Iva():
    print("IVA")
    global operando1                    #Traigo las variables dentro de la funcion
    global resultado
    global iva
    print(operando1.get())
    numeroresultado = None 
    print("Iva")
    numeroresultado = operando1.get()* 21 / 100
    resultado.config(text=numeroresultado)



tk.Label(ventana,text="Introduce la base imponible").pack(padx=20,pady=4) #creo una etiqueta
tk.Entry(ventana,textvariable=operando1).pack(padx=20,pady=4)                                    #creo un campo

tk.Label(ventana,text="Calcula").pack(padx=20,pady=4) #creo una etiqueta
tk.Button(ventana,text="Total factura",command= Iva,command=).pack(padx=20,pady=4)       #creo un boton
resultado=tk.Label(ventana,text="-")       #creo un campo para el IVA 
resultado.pack(padx=20,pady=4)

resultado=tk.Label(ventana,text="-")       #creo un campo para el IRPF
resultado.pack(padx=20,pady=4)

resultado=tk.Label(ventana,text="-")       #creo un campo para el Total
resultado.pack(padx=20,pady=4)
