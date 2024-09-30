SELECT
nombre,
apellidos,
TIMESTAMPDIFF(YEAR,fechadenacimiento, CURDATE()) AS edad,
TIMESTAMPDIFF(YEAR,fechadenacimiento, CURDATE()) >=30 AS mayorquetreinta
FROM 
miempresa.clientes;