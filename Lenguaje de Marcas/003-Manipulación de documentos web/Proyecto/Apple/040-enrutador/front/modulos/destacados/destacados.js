fetch("../back/?tabla=destacados")
.then(function(response){
	return response.json()
})
.then(function(datos){
	console.log(datos)																				// Creo un array de elementos
	let contenedordestacados = document.querySelector("#destacados")		// Selecciono un contenedor
	let plantilladestacados = document.querySelector("#destacado")			// Selecciono el elemento plantilla
	datos.forEach(function(dato){										// Para cada destacado
		let instancia = plantilladestacados.content.cloneNode(true);		// Clono la plantilla
		instancia.querySelector("h3").textContent = dato.titulo					/// Cambio el texto de cada instancia
		instancia.querySelector("h4").textContent = dato.texto
		instancia.querySelector("article").style.background = "url(data:image/png;base64,"+dato.imagen+"article"		
		contenedordestacados.appendChild(instancia)	
	})							// Lo añado al contenedor
})
