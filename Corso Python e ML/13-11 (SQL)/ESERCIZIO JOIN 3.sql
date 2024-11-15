-- Si vuole conoscere la lista di repubbliche con aspettativa di vita maggiore dei 70 anni

SELECT 
    Name AS Nazione,
    LifeExpectancy AS AspettativaDiVita
FROM 
    Country
WHERE 
    GovernmentForm LIKE '%Republic%'
    AND LifeExpectancy > 70;
