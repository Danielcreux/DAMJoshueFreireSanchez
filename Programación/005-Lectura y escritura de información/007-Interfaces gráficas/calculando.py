import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Calculadora v0,1")

operando1 = tk.IntVar()
operando2 = tk.IntVar()

def calcula():
    print("Voy a calcular algo")
    op1 = operando1.get()
    op2 = operando2.get()
    calculo = op1 + op2
    etiquetaresultado.config(text=str(calculo))

# Etiqueta y entrada para el operando 1
tk.Label(
    ventana,
    text="Introduce el operando 1"
).pack(
    padx=10,
    pady=10
)

tk.Entry(
    ventana,
    textvariable=operando1
).pack(
    padx=10,
    pady=10
)

# Etiqueta y entrada para el operando 2
tk.Label(
    ventana,
    text="Introduce el operando 2"
).pack(
    padx=10,
    pady=10
)

tk.Entry(
    ventana,
    textvariable=operando2
).pack(
    padx=10,
    pady=10
)

# Botón para calcular
tk.Button(
    ventana,
    text="¡Calcular!",
    command=calcula
).pack(
    padx=10,
    pady=10
)

# Etiqueta para mostrar el resultado
etiquetaresultado = tk.Label(
    ventana,
    text="Este es el resultado"
)
etiquetaresultado.pack(
    padx=10,
    pady=10
)

ventana.mainloop()
