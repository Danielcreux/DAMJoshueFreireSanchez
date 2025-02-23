import subprocess
import tkinter as tk

def calculaNumero():
    resultado = subprocess.run(
            ['./controlador.out',numero.text.get()],
            capture_output=True,
            text=True,
            check=True
    )
    resultadotexto = resultado.stdout.strip()                   #Lanzo el paquete de informaicon contra c++
    retroalimentacion.config(text=resultado.stdout.strip())      #Recojo el resultado que os da c++
                                                                                              
ventana = tk.Tk()

numero = tk.StringVar()

tk.Entry(ventana,textvariable=numero).pack(padx=10,pady=10)
tk.Button(ventana,text="Vamo a por ello",command=calculaNumero).pack(padx=10,pady=10)
retroalimentacion = tk.Label(ventana,text="?")
retroalimentacion.pack(padx=10,pady=10)

ventana.mainloop()


