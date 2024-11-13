def calcula(aaa,bbb,operacion):
    resutlado = None
    if operacion == "suma":
        resultado = operando1 + operando2
    elif operacion == "resta":
         resultado = operando1 - operando2
    elif operacion == "multiplicacion2":
         resultado = operando1 * operando2
    elif operacion == "division":
         resultado = operando1 / operando2

    return resultado 
    
print(calcula(4,3,"suma"))
