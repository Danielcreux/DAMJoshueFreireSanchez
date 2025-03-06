import subprocess
import tkinter as tk

def calculaNumero():
    resultado = subprocess.run(
            ['./controlador.out',numero.text.get()],
            capture_output=True,
            text=True,
            check=True
    )

    print(resultado.stdout.strip())

ventana = tk.Tk()

numero = tk.StringVar()

tk.Entry(ventana,textvariable=numero).pack(padx=10,pady=10)
tk.Button(ventana,text="Vamo a por ello",command=calculaNumero).pack(padx=10,pady=10)

ventana.mainloop()


