# joshue-navy
## Libreria PHP para convertir automaticamente Markdown a Html

Mediante esta libreria es posible convertir archivos de markdown directamente en HTML

### Escenarios de uso

* Documentacion de aplicaciones
* Creacion de documentos en linea
* Escribir libros 

### Instrucciones de uso 

1. Descarga la libreria desde Github
   	1. Accede a la url: [Enlace al repositorio de github](URL= "https://github.com/Danielcreux/joshue-navy/")
   	2. Utiliza el botón para descargar repositorio completo
3. Situa la libreria cerca de tu proyecto
4. Incluye la libreria en tu proyecto con **include** o **require**
5. Llama a la libreria para convertir tu documento (*Sigue el ejemplo que te indicamos a continuación*)

### URL para conseguir la libreria:
Puede conseguir la libreria desde:
[Enlace al repositorio de github](URL= "https://github.com/Danielcreux/joshue-navy/")

### Ejemplos de uso

Para insertar el codigo dentro de tu proyecto, debes hacerlo mediante el comando **include**:

```include "joshue-navy.php";```

Ejemplo completo de uso:

```
<?php
	include "joshue-navy.php";
	$markdownFile = "muestra.md";
	$markdownContent = file_get_contents($markdownFile);
	$htmlContent = markdownToHtml($markdownContent);
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Conversión Markdown a HTML</title>
</head>
<body>
<?php
echo $htmlContent;
?>
</body>
```
</html>
