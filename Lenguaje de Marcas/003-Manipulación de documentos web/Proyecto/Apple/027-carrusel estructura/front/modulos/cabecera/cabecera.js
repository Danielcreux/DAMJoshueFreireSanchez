console.log("Soy el JS de la cabecera")
let secciones = [
    'Store',
    'imac',
    'ipad',
    'ipod',
    'xxx',
    'YYY',
    'ZZZ'
]
let cabecera = document.querySelector("header nav ul")
secciones.forEach(function(seccion){
 cabecera.innerHTML +=  `
        <li>
            <a href="">`+seccion+`</a>
        </li>
  `
})