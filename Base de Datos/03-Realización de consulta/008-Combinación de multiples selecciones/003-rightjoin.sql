SELECT * FROM empleados
RIGHT JOIN direcciones
on empleados.Identificador = direcciones.empleados_nombre;