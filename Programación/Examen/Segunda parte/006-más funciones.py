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

def Irpf():
    print("IVA")
    global operando1                    #Traigo las variables dentro de la funcion
    global resultado
    global irpf
    print(operando1.get())
    numeroresultado = None 
    print("Irpf")
    numeroresultado = operando1.get()* 15 / 100
    resultado.config(text=numeroresultado)

def Total():
    print("Total")
    global operando1                    #Traigo las variables dentro de la funcion
    global resultado
    global total
    print(operando1.get())
    numeroresultado = None 
    print("total")
    numeroresultado = operando1.get() - Irpf.get() + Iva.get()
    resultado.config(text=numeroresultado)



tk.Label(ventana,text="Introduce la base imponible").pack(padx=20,pady=4) #creo una etiqueta
tk.Entry(ventana,textvariable=operando1).pack(padx=20,pady=4)             #creo un campo
tk.Label(ventana,text="Iva").pack(padx=20,pady=4) #creo una etiqueta
resultado=tk.Label(ventana,text="-")       #creo un campo para el IVA 
resultado.pack(padx=20,pady=4)

tk.Label(ventana,text="Irpf").pack(padx=20,pady=4) #creo una etiqueta

resultado=tk.Label(ventana,text="-")       #creo un campo para el IRPF
resultado.pack(padx=20,pady=4)


tk.Label(ventana,text="Calcula").pack(padx=20,pady=4) #creo una etiqueta
tk.Button(ventana,text="Vamos alla",command= Iva).pack(padx=20,pady=4)       #creo un boton



resultado=tk.Label(ventana,text="-")       #creo un campo para el IRPF
resultado.pack(padx=20,pady=4)

resultado=tk.Label(ventana,text="-")       #creo un campo para el Total
resultado.pack(padx=20,pady=4)
