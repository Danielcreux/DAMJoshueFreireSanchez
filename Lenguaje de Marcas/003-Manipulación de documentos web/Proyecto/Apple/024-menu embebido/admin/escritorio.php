<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="estilo/escritorio.css">
    </head>
    <body>
        <header></header>
        <main>
            <nav>
                <ul>
                    <?php
                       $productos = ['ipad','iphone','imac','airpods'];
                    foreach($productos as $clave=>$valor){
                        echo "<li>".$valor."</li>";
                    }



                    ?>
                </ul>
            </nav>
            <section>
            </section>
        </main>
    </body>

</html>