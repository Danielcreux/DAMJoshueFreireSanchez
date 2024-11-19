import tkinter as tk                       #Importo la libreria

ventana = tk.Tk();                         #Creo una ventana

operando1= tk.IntVar()                     #Esta variable almacena un entero
operando2= tk.IntVar()                      #Esta variable almacena un entero
operacion= tk.StringVar()                   #Esta variable almacena una cadena


def calcula():
    print("Vamos a calcular")
    global operando1
    global operando2                        #Traigo las variables dentro de la funcion
    global operacion
    global resultado
    print(operando1.get())
    numeroresultado = None
    if operacion.get() == "+":  
        print("suma")
        numeroresultado = operando1.get()+ operando2.get()
        resultado.config(text=numeroresultado)
    elif operacion.get() == "-":
        print("resta")
        numeroresultado = operando1.get()- operando2.get()
        resultado.config(text=numeroresultado)
    elif operacion.get() == "*":
        print("multiplicación")
        numeroresultado = operando1.get()* operando2.get()
        resultado.config(text=numeroresultado)
    elif operacion.get() == "/":
        print("división")
        numeroresultado = operando1.get()/ operando2.get()
        resultado.config(text=numeroresultado)
    else:
        resultado.config(text="No permitido")


tk.Label(ventana,text="Introduce el primer operando").pack(padx=20,pady=4) #creo una etiqueta
tk.Entry(ventana,textvariable=operando1).pack(padx=20,pady=4)                                    #creo un campo

tk.Label(ventana,text="Introduce el segundo operando").pack(padx=20,pady=4) #creo una etiqueta
tk.Entry(ventana,textvariable=operando2).pack(padx=20,pady=4)                                     #creo un campo

tk.Label(ventana,text="Escoge una operación").pack(padx=20,pady=4) #creo una etiqueta
tk.Entry(ventana,textvariable=operacion).pack(padx=20,pady=4)                                     #creo un campo

tk.Label(ventana,text="Pulsa para ejecutar").pack(padx=20,pady=4) #creo una etiqueta
tk.Button(ventana,text="Vamos alla!",command= calcula).pack(padx=20,pady=4)       #creo un boton

tk.Label(ventana,text="El resultado aparecerá aquí").pack(padx=20,pady=4) #creo una etiqueta
resultado=tk.Label(ventana,text="X")       #creo un campo
resultado.pack(padx=20,pady=4)

ventana.mainloop();  
 
