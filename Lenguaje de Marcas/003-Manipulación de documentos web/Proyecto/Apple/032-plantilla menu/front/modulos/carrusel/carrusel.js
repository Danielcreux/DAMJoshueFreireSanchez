let puntos = document.querySelectorAll(".punto")            //Selecciono los puntos
puntos.forEach(function(punto,index){                       //Para cada uno de los puntos
    punto.onclick = function(){                             //cuando haga click en un punto
        let carrusel1 = document.querySelector("#carrusel1") //cojo el carrusel
        carrusel1.classList.remove("animado1")              //Paro la animación
        carrusel1.style.left = 0 -index*1024+"px"           //Le pongo a mano al desfase en base al punto en el cual he hecho click
    }
})