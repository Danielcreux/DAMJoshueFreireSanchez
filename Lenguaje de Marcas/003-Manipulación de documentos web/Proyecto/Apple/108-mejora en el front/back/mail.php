<?php
// Establece el tipo de contenido como JSON para la respuesta
header("Content-Type: application/json");

error_reporting(0); // Desactiva la visualización de errores
ini_set('display_errors', 0); // Desactiva la visualización de errores

// Verifica si los campos necesarios están presentes
if (!isset($_POST['nombre']) || !isset($_POST['email']) || !isset($_POST['asunto']) || !isset($_POST['mensaje'])) {
    echo json_encode(["error" => "Todos los campos son obligatorios."]);
    exit;
}

// Recoge los datos del formulario
$nombre = htmlspecialchars($_POST['nombre']);
$email = htmlspecialchars($_POST['email']);
$asunto = htmlspecialchars($_POST['asunto']);
$mensaje = htmlspecialchars($_POST['mensaje']);

// Valida el correo electrónico
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo json_encode(["error" => "El correo electrónico no es válido."]);
    exit;
}

// Componer el correo
$to = "jd2000_fs@hotmail.com"; // Cambia a tu dirección de correo
$subject = "Nuevo mensaje de contacto: $asunto";
$body = "Nombre: $nombre\nEmail: $email\n\nMensaje:\n$mensaje";
$headers = "From: $email\r\nReply-To: $email\r\n";

// Guarda los datos en un archivo JSON
$archivo = fopen("mail/" . date('U') . ".json", "w");
if ($archivo) {
    fwrite($archivo, json_encode($_POST, JSON_PRETTY_PRINT));
    fclose($archivo);
} else {
    echo json_encode(["error" => "No se pudo guardar el archivo JSON."]);
    exit;
}

// Intenta enviar el correo
if (mail($to, $subject, $body, $headers)) {
    $data = [
        "nombre" => $nombre,
        "email" => $email,
        "asunto" => $asunto,
        "mensaje" => $mensaje,
        "fecha" => date("Y-m-d H:i:s"),
        "epoch" => time()
    ];

    // Responde con los datos en formato JSON
    echo json_encode(["success" => "El correo se envió correctamente.", "data" => $data]);

} else {
    echo json_encode(["error" => "Hubo un problema al enviar el correo."]);
}
?>
