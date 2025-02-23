console.log("Soy el JS de la cabecera")
let secciones = [
    'Store',
    'iMac',
    'iPad',
    'iPod',
    'xxx',
    'YYY',
    'ZZZ'
]
let cabecera = document.querySelector("header nav ul")
let plantilla = document.querySelector("#elementomenu")
secciones.forEach(function(seccion){
     let instancia= plantilla.content.cloneNode(true);
     instancia.querySelector("a").textContent=seccion
     cabecera.appendChild(instancia)
})