
# Titulo de nivel 1


# Titulo de nivel 1

# Programacion
## Evaluación sobre la aplicación jocarsa | darkslateblue
- Interfaz de admin para poder manejar tu sitio web a tu gusto
### Creación de estructura en PHP+HTML embebido

- Un diseño moderno donde será lo más minimilista posible

![ALT diseño](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/82431547131b0692f3173458f4c5a08ece2cb4e4/Lenguaje%20de%20Marcas/003-Manipulaci%C3%B3n%20de%20documentos%20web/Proyecto/Apple/imagenes/Captura.PNG)

****

1. Con la estructura de embebido nos permitimos poder implementar una manera mucho más cómoda de establecer como deseamos un contenedor, sin estar escribiendo codigo indeseable
   
 ```
  <section id="heroes">
  
  	<template id="plantillaheroe">
  		<article class="heroe">
  			<h3>Nombre del producto</h3>
  			<h4>Frase de marketing</h4>
  			<button>Call to action 1</button>
  			<button>Call to action 2</button>
  		</article>
  	</template>
  	
  </section>	
  	<script>
  	<?php include "heroes.js"?>
  </script>
  <style>
  	<?php include "heroes.css"?>
  </style>

 ```
### Creación de un login con usuario y contraseña
- Una interfaz sencilla para poder acceder a tu página de administrador
  
  ![ALT login](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/82431547131b0692f3173458f4c5a08ece2cb4e4/Lenguaje%20de%20Marcas/003-Manipulaci%C3%B3n%20de%20documentos%20web/Proyecto/Apple/imagenes/Captura2.PNG)

****

1.Realizamos una petición a la base de datos mediante php que es la que se encargará de arrojarnos el usuario que tendrá acceso al admin

```
include "config/config.php";								// Cargo los datos de conexión

	$peticion = "
		SELECT * FROM usuarios
		WHERE 
		email = '".$_POST['email']."'
		AND
		contrasena = '".$_POST['contrasena']."'
		";														// Pregunto a la base de datos si hay un usuario y contraseña que coincidan
	$resultado = $conexion->query($peticion);		// LAnzo la petición a la base de datos
```
### Creación de un supercontrolador para implementar CRUD sobre las tablas
- Gestiona con tan solo click si deseas actualizar tu web

   ![ALT CRUD](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/82431547131b0692f3173458f4c5a08ece2cb4e4/Lenguaje%20de%20Marcas/003-Manipulaci%C3%B3n%20de%20documentos%20web/Proyecto/Apple/imagenes/Captura3.PNG)

 ****
 - hemos eliminado los últimos dos destacados los cuales han dejado de aparecer en el front
   
   ![ALT CRUDactualizado](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/82431547131b0692f3173458f4c5a08ece2cb4e4/Lenguaje%20de%20Marcas/003-Manipulaci%C3%B3n%20de%20documentos%20web/Proyecto/Apple/imagenes/Captura4.PNG)
  
 1. Se creo un controlador CRUD el cual nos permite ya sea eliminar o insertar en la base de datos que deseamos que nos aparezca en nuestra página web, lo cual facilita la gestión al momento de actualizar la página
-En el ejemplo se aprecia un fragmento del archivo eliminar y la petición que se lleva a cabo para poder vaciar el contenido

  ```
$peticion = "
	DELETE FROM ".$_GET['tabla']."
	WHERE Identificador = ".$_GET['Identificador']."
"; 

$resultado = $conexion->query($peticion);

```
### Creación de un estilo mínimo pero eficaz sobre el panel de administración
 - Panel de administricación con un estilo intuitivo
   
****

![ALT Estilo](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/82431547131b0692f3173458f4c5a08ece2cb4e4/Lenguaje%20de%20Marcas/003-Manipulaci%C3%B3n%20de%20documentos%20web/Proyecto/Apple/imagenes/Captura5.PNG)

1.Personalización en el panel para poder obtener las datos de la tabla de una manera ordenada
2.En este código vemos como se personaliza mediante css para darle forma a la tabla que nos se presentará los datos que tenemos en el front 

```
table thead tr td{
	color:white;
	padding:10px;
}
table tbody tr:nth-child(odd){
	background:white;
}
```
### Conexión con la base de datos común con el proyecto jocarsa | oldlace
- Base de datos en donde almacenaremos todo lo que queremos presentar en nuestra página web

****

![ALT Base de datos](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/82431547131b0692f3173458f4c5a08ece2cb4e4/Lenguaje%20de%20Marcas/003-Manipulaci%C3%B3n%20de%20documentos%20web/Proyecto/Apple/imagenes/Captura6.PNG)

1. En este código vemos como hemos desarrollado para que se conecte con la base de datos
2. Donde veremos que se ingresa desde el nombre de la base de datos, la contraseña y el usuario con los privilegios que se usó

```
   <?php

	$servidor = "localhost";				// Defino el servidor
	$usuario = "proyectoapple";			// Defino el usuario con permiso
	$contrasena = "proyectoapple";		// Defino la contraseña de ese usuario
	$base = "proyectoapple";				// Defino la base de datos

	$conexion = new mysqli(
		$servidor, 
		$usuario, 
		$contrasena, 
		$base
	);												// Creo una conexión de tipo MySQL

?>
```
