import tkinter as tk                       #Importo la libreria


ventana = tk.Tk();                         #Creo una ventana

operando1= tk.IntVar()                     #Esta variable almacena un entero

def factura():
    global operando1                    #Traigo las variables dentro de la funcion
    global resultado
    global iva
    global irpf
    global total
    print(operando1.get())
    totalresultado = None
    ivaresultado = None
    irpfresultado = None
    print("Iva")
    ivaresultado  = operando1.get()* 21 / 100
    iva.config(text=ivaresultado )
    print("Irpf")
    irpfresultado = operando1.get()* 15 / 100
    irpf.config(text= irpfresultado)
    print("Total")
    totalresultado = operando1.get() - irpfresultado + ivaresultado
    total.config(text=totalresultado)
    
    


tk.Label(ventana,text="Introduce la base imponible").pack(padx=20,pady=4) #creo una etiqueta
tk.Entry(ventana,textvariable=operando1).pack(padx=20,pady=4)             #creo un campo
tk.Label(ventana,text="Iva").pack(padx=20,pady=4) #creo una etiqueta
iva=tk.Label(ventana,text="-")       #creo un campo para el IVA 
iva.pack(padx=20,pady=4)

tk.Label(ventana,text="Irpf").pack(padx=20,pady=4) #creo una etiqueta
irpf=tk.Label(ventana,text="-")       #creo un campo para el IRPF
irpf.pack(padx=20,pady=4)


tk.Label(ventana,text="Calcula").pack(padx=20,pady=4) #creo una etiqueta
tk.Button(ventana,text="Vamos alla",command=factura).pack(padx=20,pady=4)       #creo un boton


tk.Label(ventana,text="Total").pack(padx=20,pady=4) #creo una etiqueta
total=tk.Label(ventana,text="-")       #creo un campo para el Total
total.pack(padx=20,pady=4)


ventana.mainloop();  
