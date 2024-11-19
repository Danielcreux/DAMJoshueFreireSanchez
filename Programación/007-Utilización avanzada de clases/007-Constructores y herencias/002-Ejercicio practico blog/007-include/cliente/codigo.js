window.onload=function(){
    console.log("Javasricpt funciona")
    fetch("../servidor/damearticulos.php")
    .then (function(response){
        return response.json()
    })
    .then(function(datos){
       let contenedor=documentquerySelector("main")
       datos.forEach(function(dato){
           contenedor.innerHTML +=  `
               <article>
                    <h3>`+dato.titulo+`</h3>
                    <time>`+dato.fecha+`</time>
                    <p>`+dato.contenido+`</p>
               </article>
            ;
       })
    })
}