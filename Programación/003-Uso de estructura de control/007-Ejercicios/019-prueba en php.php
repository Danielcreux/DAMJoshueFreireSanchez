<?php
// Obtener el tiempo inicial
$fechainicio = microtime(true);

$iteraciones = 100000000;
$numero = 1.00000000065;

for ($i = 0; $i < $iteraciones; $i++) {
    $numero *= 1.000000045;
}

// Obtener el tiempo final
$fechafinal = microtime(true);

// Calcular el tiempo transcurrido
$tiempoTranscurrido = $fechafinal - $fechainicio;

echo "Tiempo transcurrido: " . $tiempoTranscurrido . " segundos\n";
?>
