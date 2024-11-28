-- Si vuole recuperare il numero di città per nazione dal database "world" mostrando anche il nome della nazione e ordinando il risultato in base al numero di città.

SELECT 
    Country.Name AS Nazione,
    COUNT(City.ID) AS NumeroCittà
FROM 
    Country
LEFT JOIN 
    City ON Country.Code = City.CountryCode
GROUP BY 
    Country.Name
ORDER BY 
    NumeroCittà DESC;