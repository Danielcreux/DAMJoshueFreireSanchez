<main>
    <?php
    include "modulos/bloque/bloque.php";
    
    $conexion = mysqli_connect(
			"localhost", 
			"proyectoapple", 
			"proyectoapple", 
			"proyectoapple"
		);		
	
		$producto = mysqli_real_escape_string($conexion, $_GET['prod']);
        $peticion = "
        SELECT * 
        FROM bloquesproductos
        WHERE productos_titulo = '$producto'
        ;";																				// Creo una petición
		//echo $peticion;
		$resultado = mysqli_query($conexion, $peticion);						// Ejecuto la petición contra el servidor
																						// Creo un array vacio
		while($fila = mysqli_fetch_array($resultado, MYSQLI_ASSOC)){		// Para cada uno de los resultados
			if($fila['tipobloque_tipo'] == "1"){
				$bloque = new BloqueCompleto(
					$fila['titulo'], 
					$fila['subtitulo'], 
					$fila['texto'],'',
					$fila['fondo']
				);
    			echo $bloque->getBloque();										// Lanzo el html del bloque
			}else if($fila['tipobloque_tipo'] == "2"){							// Si el bloque es de tipo 2
				$bloque = new BloqueCajaYoutube(
					$fila['titulo'], 
					$fila['subtitulo'],
					"",
					"",
					"",
					[]
					
					);																		// Creo una nueva instancia
    			echo $bloque->getBloque($fila['texto']);											// Lanzo el html del bloque
			}
		 }
    ?>
</main>
	<script>
	<?php include "producto.js"?>
</script>
<style>
	<?php include "producto.css"?>
</style>
