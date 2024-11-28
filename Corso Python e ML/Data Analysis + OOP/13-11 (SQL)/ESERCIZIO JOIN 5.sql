-- Create una vista chiamata PopulationByContinent che mostri il nome del continente e la popolazione totale per ciascun continente.

CREATE VIEW PopulationByContinent AS
SELECT 
    Continent,
    SUM(Population) AS TotalPopulation
FROM 
    Country
GROUP BY 
    Continent;
    
SELECT * FROM PopulationByContinent;