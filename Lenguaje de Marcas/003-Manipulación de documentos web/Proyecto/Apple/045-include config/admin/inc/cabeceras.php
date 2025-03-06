<?php

include "../error.php";
	
include "../config.php";

$peticion = "SHOW COLUMNS FROM destacados";
$resultado = $conexion->query($peticion);

while ($fila = $resultado->fetch_assoc()) {
  echo "<td>".$fila['Field']."</td>";
}


$conexion->close();
?>
