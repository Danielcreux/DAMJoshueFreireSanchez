console.log("Soy el JS de los destacados")
let destacados = [
    'Uno',
    'Dos',
    'Tres',
    'Cuatro',
    'Cinco',
    'Seis'
]                                                                               //Creo un array de elementos
let contenedordestacados = document.querySelector("#destacados")                //Selecciono un contenedor
let plantilladestacados = document.querySelector("#destacado")                  //Seleccion el elemento plantilla
destacados.forEach(function(destacado){                                         //Para cada destacado
     let instancia= plantilladestacados.content.cloneNode(true);                //Clono la plantilla
     instancia.querySelector("h3").textContent= destacado                       //Cambio el texto de cada instancia 
     contenedordestacados.appendChild(instancia)                                //Le añado al contenedor 
})