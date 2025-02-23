<?php

/* Configuramos el acceso a la base de datos */

	$servidor = "localhost";				// Defino el servidor
	$usuario = "oldlice";			        // Defino el usuario con permiso
	$contrasena = "oldlice";		       // Defino la contraseña de ese usuario
	$base = "oldlice";				       // Defino la base de datos

	$conexion = new mysqli(
		$servidor, 
		$usuario, 
		$contrasena, 
		$base
	);												// Creo una conexión de tipo MySQL

?>
