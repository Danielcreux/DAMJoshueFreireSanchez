function difumina(cabecera){
    console.log("Has entrado")                                      //Cuando entro
    document.querySelector("main").classList.add("difuminado")      //Le añado una clase css
    cabecera.style.background = "rgba(255,255,255,0.9)"             //Le pongo transparencia al fondo
}