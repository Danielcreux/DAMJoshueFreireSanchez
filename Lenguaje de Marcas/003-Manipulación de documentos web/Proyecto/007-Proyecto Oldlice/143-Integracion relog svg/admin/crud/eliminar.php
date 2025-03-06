<?php
/* Nos permite eliminar lo que no deseamos en nuestra base de datos  */
// Este archivo inserta los campos que vienen del formulario

include "../utilidades/error.php";                           // Incluyo los mensajes de error
include "../config/config.php";                             // Traigo la conexión a la base de datos

$peticion = "                                               
	DELETE FROM ".$_GET['tabla']."
	WHERE Identificador = ".$_GET['Identificador']."
";                                                           //Realizamos la peticion 

$resultado = $conexion->query($peticion);                    //Mostramos la petición 

?>

<meta http-equiv="refresh" content="1; url=../escritorio.php">  

