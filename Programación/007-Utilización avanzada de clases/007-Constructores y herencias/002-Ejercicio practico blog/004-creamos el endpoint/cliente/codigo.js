window.onload=function(){
    console.log("Javasricpt funciona")
    fetch("../servidor/damearticulos.php")
    .then (function(response){
        return response.json()
    })
    .then(function(datos){
        console.log(datos)
    })
}