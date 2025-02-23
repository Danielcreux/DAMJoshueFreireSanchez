<?php 
/*
Archivo principal de la aplicación que consiste en el escritorio a partir del cual el usuario administrador puede realizar cualquier operación con la información contenida en la base de datos 

*/
  session_start();
  if(!isset($_SESSION['login'])){
      header("Location: index.html");
  }
  include "inc/calculapagina.php";  
//include "utilidades/error.php"?>

<!doctype html>
<html>
	<head>
        <title>FabriCraft</title>
		<link rel="Stylesheet" href="estilo/escritorio.css">
         <link rel="icon" href="impresion.svg" type="image/svg+xml">
	</head>
	<body>
		<header>
            <h1><img src="impresion.svg" id="logo">
                Joshué | FabriCrafts</h1>
            <div id="cerrarsesion">
                <a href="logout.php">🚪</a>
                
			</div>
        </header>
				<main>
			<nav>
				<ul>
					<li class="destacado">Tablas:</li>
					<?php include "inc/menu.php"?>
					<li class="destacado">Documentos:</li>
					<?php include "inc/listadodocumentos.php"?>
				</ul>
			</nav>
			<section>
				<?php include "inc/tabla.php"?>
                <?php include "inc/documentos.php"?>
                <?php include "inc/documento.php"?>
				<?php include "inc/formulario.php"?>
			</section>
		</main>
		<script src="js/codigo.js"></script>
	</body>
</html>