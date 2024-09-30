SELECT 
n1 AS 'El numero propio dicho',
COUNT(n1) AS 'Numero de veces que se ha repetido ese numero'
FROM  `euromillones`
GROUP BY (n1)  
;