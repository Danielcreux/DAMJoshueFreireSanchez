 <?php
    include"conexionbasededatos.php";

?> 

<!doctype html>
<html>
    <head>
        <meta charset="UTF-8">
        
        <style>
            body,html{
                background:grey;
            }
            header,main,footer{
                width:800px;
                padding:20px;
                margin:auto;
                background:white;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Blog</h1>
            <h2>El blog de Joshué Freire</h2>
        </header>
        <main>
            <?php dameArticulos(); ?>
           
 
        </main>
        <footer>
            <h6>(c( 2024 Joshué Freire</h6>
        </footer>
    </body>
</html>