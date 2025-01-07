<?php

	echo "Si estas viendo esto es que vamos a hacer login<br>";

    include "utilidades/error.php";                           // Incluyo los mensajes de error
    include "config/config.php";                          // Traigo la conexión a la base de datos

    $peticion = "
        SELECT * FROM usuarios
        WHERE
        email ='".$_POST['email']."'
        AND
        contrasena = '".$_POST['contrasena']."'
        ";                                                                     //Pregunto a la base de datos si hay un usurio

    $resultado = $conexion->query($peticion);                                   //Lanzo la peticion a la base de datos 

    if ($fila = $resultado->fetch_assoc()) {                                    //Si es cierto que hay al menos un usuario
        echo 
         '<a href="escritorio.php">Pulsa y vamos al escritorio</a>';            //Permitirme ir al escritorio
    }else{                                                                      //En caso contrario 
        echo "Intento de acceso incorrecto";                                    //Dime que el intento es incorrecto
    }


?>

