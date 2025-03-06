
<?php
/* Permite poder movernos en el contenido del panel por medio de botones así tener una mejor orientación  */ 
	if(isset($_GET['pagina'])){
		if($_GET['pagina'] == 0){$_SESSION['pagina'] = 0;}                  //Nos permite vovler a la pagina de inicio
		if($_GET['pagina'] == "siguiente"){$_SESSION['pagina']++;}          //Nos permite ir a la sig pagina 
		if($_GET['pagina'] == "anterior"){$_SESSION['pagina']--;}           //Nos permite ir a la pag anterior 
	}
?>
