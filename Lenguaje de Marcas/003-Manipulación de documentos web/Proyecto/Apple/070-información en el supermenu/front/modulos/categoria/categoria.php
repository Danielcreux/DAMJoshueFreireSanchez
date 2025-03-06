<main>
    <?php 
		include "modulos/bloque/bloque.php"; 
		$bloque1 = new BloqueCompleto(
					"Titulo bloque 1",
					"Subtitulo Bloque 1",
					"texto bloque 1",
					"",
					"");
		echo $bloque1->getBloque();
		
		$bloque2 = new BloqueCaja(
					"Titulo bloque 2",
					"Subtitulo Bloque 2",
					"texto bloque 2",
					"",
					"");
		echo $bloque2->getBloque();
		
		$bloque3 = new BloqueCaja(
					"Titulo bloque 3",
					"Subtitulo Bloque 3",
					"texto bloque 3",
					"",
                    "");
                   
		echo $bloque3->getBloque();	
        
        $bloque4 = new BloqueCaja(
					"Titulo bloque 4",
					"Subtitulo Bloque 4",
					"texto bloque 4",
					"",
                    "",
                    [
                        "background" =>  "red",
                        "border-radius" => "23px" 
                    ]
            
				);
					
		echo $bloque4->getBloque();	
	?>
