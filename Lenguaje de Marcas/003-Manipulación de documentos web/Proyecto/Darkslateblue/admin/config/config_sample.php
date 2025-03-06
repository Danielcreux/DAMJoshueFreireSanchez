<?php

	$servidor = "localhost";				// Defino el servidor
	$usuario = "OldlaceUser4$";			// Defino el usuario con permiso
	$contrasena = "TAMEdam123$";		// Defino la contraseña de ese usuario
	$base = "oldlice";				// Defino la base de datos

	$conexion = new mysqli(
		$servidor, 
		$usuario, 
		$contrasena, 
		$base
	);												// Creo una conexión de tipo MySQL

?>
