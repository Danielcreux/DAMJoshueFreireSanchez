window.onload = function() {
    console.log("Javascript funcionando")
    fetch("http://localhost:5000/dameexperto")
    .then(function(response){
        return response.json()
    })
    .then(function(nuevo){
        console.log(nuevo)
        let contenedor2= document.querySelector(".contenido")
        nuevo.forEach(function(dato) {
            contenedor2.innerHTML +=  ` 
                    <div class="contenedor2">
						<img src="https://cienciaycatedral.ubuinvestiga.es/wp-content/uploads/sites/14/2022/07/Antonio-Cano_p.jpg">
						<h4>  ` +dato.nombre+ ` </h4>
                    </div>
                     `

            
        })
    })
}