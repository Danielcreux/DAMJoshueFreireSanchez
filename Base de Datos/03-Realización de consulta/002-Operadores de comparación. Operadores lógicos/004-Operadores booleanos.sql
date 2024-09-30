SELECT
nombre,
apellidos,
TIMESTAMPDIFF(YEAR,fechadenacimiento, CURDATE()) AS edad,
TIMESTAMPDIFF(YEAR,fechadenacimiento, CURDATE()) >=30 AS mayorquetreinta,
TIMESTAMPDIFF(YEAR,fechadenacimiento, CURDATE()) >=30 
&&   TIMESTAMPDIFF(YEAR,fechadenacimiento, CURDATE()) < 40 AS treintañero
FROM 
miempresa.clientes;