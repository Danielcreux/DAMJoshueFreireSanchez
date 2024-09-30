SELECT * FROM empleados
LEFT JOIN direcciones
on empleados.Identificador = direcciones.empleados_nombre;