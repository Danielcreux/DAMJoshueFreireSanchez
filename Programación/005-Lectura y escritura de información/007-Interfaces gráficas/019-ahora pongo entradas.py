import tkinter as tk

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Calculadora v0,1")

operando1=tk.IntVar()
operando2=tk.IntVar()

def calcula():
    print("Voy a calcular algo")
tk.Label(
    ventana,
    text="Introduce el operando 1"
    ).pack(
        padx=10,
        pady=10
        )

tk.Entry(
    ventana,
    textvariable = operando1
    ).pack(
        padx=10,
        pady=10
        )

tk.Label(
    ventana,
    text="Introduce el operando 2"
    ).pack(
        padx=10,
        pady=10
        )

tk.Entry(
    ventana,
    textvariable = operando2
    ).pack(
        padx=10,
        pady=10
        )
tk.Label(
    ventana,
    text="Pulsa el botón para obtener el resultado"
    ).pack(
        padx=10,
        pady=10
        )

tk.Button(
    ventana,
    command="resultado"
    ).pack(
        padx=10,
        pady=10
        )

tk.Label(
    ventana,
    text="Este es el resultado"
    ).pack(
        padx=10,
        pady=10
        )

ventana.mainloop()
