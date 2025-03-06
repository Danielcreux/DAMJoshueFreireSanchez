# Base de datos 
## Creación de la base de datos de vuestro proyecto oldlace / darkslateblue / thistle (y utilidades similares)

- Base de datos donde se almacenará toda la información de nuestra página web

****

 ![ALT base](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/3424c6a19522a09c8ccfeb29b574596eaf60b740/Base%20de%20Datos/imagenes/Captura.PNG)

1.Mediante comandos Sql creamos nuestra base de datos dandole los privilegios
2.Se crea el usuario dandole todos los privilegios 
 ```
CREATE DATABASE oldlice;

CREATE USER 'oldlice'@'localhost' IDENTIFIED BY 'oldlice';

GRANT ALL PRIVILEGES ON oldlice.* TO 'oldlice'@'localhost';}

FLUSH PRIVILEGE;

 ```
### Adaptación y modificación de la base de datos a vuestras necesidades

- Quieres que tu negocio tenga acceso directo a tus redes para poder tener más cerca a tus clientes

  ****

  ![ALT adapatación](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/3424c6a19522a09c8ccfeb29b574596eaf60b740/Base%20de%20Datos/imagenes/Captura3.PNG)

1. En este apartado vemos como necesitamos en nuestro front mostrar las redes sociales
2. Al momento de que el cliente seleccione la red social será redirigido al perfil

****
  ![ALT redes sociales](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/3424c6a19522a09c8ccfeb29b574596eaf60b740/Base%20de%20Datos/imagenes/Captura2.PNG)

### Demostración de guardado de datos en otros formatos como JSON (pedidos desde la web frontal)

- Procesamos tus pedidos de una manera sencilla

****
  ![ALT pedidos](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/3424c6a19522a09c8ccfeb29b574596eaf60b740/Base%20de%20Datos/imagenes/Captura4.PNG)

1.Vemos como el pedido que realizamos es un json el cual se va almacenar para poder gestionar las compras que se van realizando
 ```
json = {
		"cliente":{
			"nombre":nombre,
			"apellidos":apellidos,
			"email":email
		},
		"pedido":{
			"fecha":fechahumana,
			"numerodepedido":numeropedido
		},
		"productos":JSON.parse(localStorage.getItem("carrito"))
	}
 ```
2. vemos como el carrito se almacena tal cual se ha solicitado en el apartado anterior 

![ALT carrito](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/3424c6a19522a09c8ccfeb29b574596eaf60b740/Base%20de%20Datos/imagenes/Captura5.PNG)

### Utilización de peticiones cruzadas entre tablas (JOIN)
- Nuestro admin reconocerá a que producto nos estamos refiriendo
  
****
  ![ALT peticiones](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/3424c6a19522a09c8ccfeb29b574596eaf60b740/Base%20de%20Datos/imagenes/Captura7.PNG)

1. Desde el código de producto realizamos una petición cruzada conectandose con nuestra base de datos de bloques

 ```
$producto = mysqli_real_escape_string($conexion, $_GET['prod']);
        $peticion = "
        SELECT * 
        FROM bloquesproductos
        WHERE productos_titulo = '$producto'
        ;";																				// Creo una petición
		//echo $peticion;
		$resultado = mysqli_query($conexion, $peticion);						// Ejecuto la petición contra el servidor
 ```
2. El cual nos permitirá reflejarlo al momento de realizar un pedido en donde podemos ver como el bloque nos determina a que producto nos referimos sin necesidad que se refleje solo la identificación de nuestra base de datos

![ALT identificacion](https://github.com/Danielcreux/DAMJoshueFreireSanchez/blob/3424c6a19522a09c8ccfeb29b574596eaf60b740/Base%20de%20Datos/imagenes/Captura6.PNG)


### Utilización de vistas (por ejemplo en jocarsa | thistle)
### Utilización de procedimientos almacenados (por ejemplo en jocarsa | thistle)
