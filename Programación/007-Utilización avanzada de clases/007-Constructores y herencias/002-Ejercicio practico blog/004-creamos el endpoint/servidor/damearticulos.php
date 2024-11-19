<?php
    ini_set('display_errors',1);
    ini_set('display_startup_errors',1);
    error_reporting(E_ALL);        
    $conexion = mysqli_connect(
    "locahost",
    "blog",
    "blog",
    "blog",
    );                                                          //Me conecto a la base de datos
    $peticion = "SELECT*FROM entradas;";                        //Creo una petición
    $resultado = mysqli_query($conexion,$peticion);             //Ejecuto la petición contra el servidor
    $json= [];                                             //Creo un array vacio
    while($fila=mysqli_fetch_array($resultado,MYSQLI_ASSOC)){   //Para cada uno de los resultados
        $json[]= $fila;                                    //Hago un push del array
    } 
    header('Content-Type: application/json');                   //El documento va ser JSon
    echo json_encode($json);                                //Saco el formato de forma compatible con json
?>
 