function recogeCarrusel2() { 
    fetch("../back/?tabla=carrusel2")
    .then(response => response.json())  
    .then(datos => {
        console.log(datos); // Para depuración

        let carrusel2 = document.querySelector("#carrusel2");

        // Limpiar contenido previo para evitar duplicados
        carrusel2.innerHTML = "";
       

        datos.forEach((dato, index) => {
            let article = document.createElement("article");

            let button = document.createElement("button");
            button.innerHTML = dato.boton;

            let p = document.createElement("p");
            p.innerHTML = dato.texto;

            article.style.background = `url(data:image/png;base64,${dato.imagen})`;
            article.style.backgroundSize = "cover";

            article.appendChild(button);
            article.appendChild(p);

            // Alternar entre carrusel1 y carrusel2
            if (index % 2 === 0) {
                carrusel2.appendChild(article);
            } else {
                carrusel2.appendChild(article);
            }
        });
    })
    .catch(error => console.error("Error cargando el carrusel:", error));
    });
}

// Ejecutar las funciones cuando cargue la página
document.addEventListener("DOMContentLoaded", () => {
    recogeCarrusel2();
});
