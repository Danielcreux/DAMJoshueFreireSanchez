function recogeCarrusel() { 
    fetch("../back/?tabla=carrusel")
    .then(response => response.json())  
    .then(datos => {
        console.log(datos); // Para depuración

        let carrusel1 = document.querySelector("#carrusel1");

        // Limpiar contenido previo para evitar duplicados
        carrusel1.innerHTML = "";
       

        datos.forEach((dato, index) => {
            let article = document.createElement("article");

            let button = document.createElement("button");
            button.innerHTML = dato.botonaccion;

            let p = document.createElement("p");
            p.innerHTML = dato.texto;

            article.style.background = `url(data:image/png;base64,${dato.imagen})`;
            article.style.backgroundSize = "cover";

            article.appendChild(button);
            article.appendChild(p);

            // Alternar entre carrusel1 y carrusel2
            if (index % 2 === 0) {
                carrusel1.appendChild(article);
            } else {
                carrusel1.appendChild(article);
            }
        });
    })
    .catch(error => console.error("Error cargando el carrusel:", error));
}

// Agregar funcionalidad a los puntos de navegación
function configurarPuntos() {
    let puntos = document.querySelectorAll(".punto");
    let carrusel1 = document.querySelector("#carrusel1");

    puntos.forEach((punto, index) => {
        punto.onclick = function() {
            carrusel1.classList.remove("animado1"); // Parar la animación
            carrusel1.style.transform = `translateX(${-index * 1024}px)`; // Mover el carrusel
        };
    });
}

// Ejecutar las funciones cuando cargue la página
document.addEventListener("DOMContentLoaded", () => {
    recogeCarrusel();
    configurarPuntos();
});
