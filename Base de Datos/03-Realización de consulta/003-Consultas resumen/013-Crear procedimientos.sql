DELIMITER //

CREATE PROCEDURE miprocedimiento(IN a INT)
BEGIN
    SELECT  
        a AS 'El numero propio dicho',
        COUNT(a) AS 'Numero de veces que se ha repetido ese numero'
    FROM `euromillones`
    GROUP BY n1
    ORDER BY COUNT(n1) DESC
    LIMIT 1;
END //

DELIMITER ;
