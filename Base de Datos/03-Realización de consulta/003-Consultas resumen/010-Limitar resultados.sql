SELECT 
n2 AS 'El numero propio dicho',
COUNT(n2) AS 'Numero de veces que se ha repetido ese numero'
FROM  `euromillones`
GROUP BY (n2)
ORDER BY COUNT(n2) DESC 
LIMIT 1  
;