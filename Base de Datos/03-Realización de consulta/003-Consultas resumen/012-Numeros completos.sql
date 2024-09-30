SELECT 
n1 AS 'El numero propio dicho',
COUNT(n1) AS 'Numero de veces que se ha repetido ese numero'
FROM  `euromillones`
GROUP BY (n1)
ORDER BY COUNT(n1) DESC 
LIMIT 1  
;
SELECT 
n2 AS 'El numero propio dicho',
COUNT(n2) AS 'Numero de veces que se ha repetido ese numero'
FROM  `euromillones`
GROUP BY (n2)
ORDER BY COUNT(n2) DESC 
LIMIT 1  
;
SELECT 
n3 AS 'El numero propio dicho',
COUNT(n3) AS 'Numero de veces que se ha repetido ese numero'
FROM  `euromillones`
GROUP BY (n3)
ORDER BY COUNT(n3) DESC 
LIMIT 1  
;
SELECT 
n4 AS 'El numero propio dicho',
COUNT(n4) AS 'Numero de veces que se ha repetido ese numero'
FROM  `euromillones`
GROUP BY (n4)
ORDER BY COUNT(n4) DESC 
LIMIT 1  
;
SELECT 
n5 AS 'El numero propio dicho',
COUNT(n5) AS 'Numero de veces que se ha repetido ese numero'
FROM  `euromillones`
GROUP BY (n5)
ORDER BY COUNT(n5) DESC 
LIMIT 1  
;
SELECT 
e1 AS 'El numero propio dicho',
COUNT(e1) AS 'Numero de veces que se ha repetido ese numero'
FROM  `euromillones`
GROUP BY (e1)
ORDER BY COUNT(e1) DESC 
LIMIT 1  
;
SELECT 
e2 AS 'El numero propio dicho',
COUNT(e2) AS 'Numero de veces que se ha repetido ese numero'
FROM  `euromillones`
GROUP BY (e2)
ORDER BY COUNT(e2) DESC 
LIMIT 1  
;