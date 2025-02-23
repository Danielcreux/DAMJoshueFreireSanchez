<?php

	$servidor = "localhost";				// Defino el servidor
	$contrasena = "oldlice";		// Defino la contraseña de ese usuario
	$usuario = "oldlice";			// Defino el usuario con permiso
	$base = "oldlice";		// Defino la contraseña de ese usuario

	$conexion = new mysqli(
		$servidor, 
		$usuario, 
		$contrasena, 
		$base
	);												// Creo una conexión de tipo MySQL

?>
