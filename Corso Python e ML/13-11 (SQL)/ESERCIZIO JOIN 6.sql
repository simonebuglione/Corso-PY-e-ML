-- Create una vista chiamata CapitalCities che mostri il nome dello stato, il nome della sua capitale e la lingua ufficiale

CREATE VIEW CapitalCities AS
SELECT 
    Country.Name AS CountryName,
    City.Name AS CapitalName,
    CountryLanguage.Language AS OfficialLanguage
FROM 
    Country
JOIN 
    City ON Country.Capital = City.ID
JOIN 
    CountryLanguage ON Country.Code = CountryLanguage.CountryCode
WHERE 
    CountryLanguage.IsOfficial = 'T';
