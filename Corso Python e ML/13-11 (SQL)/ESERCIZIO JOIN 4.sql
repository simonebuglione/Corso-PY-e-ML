-- Si vuole recuperare dal database WORLD le lingue parlate per nazione con la rispettiva percentuale di utilizzo;

-- create un vista sulla base di questa query

DESCRIBE Country;
DESCRIBE CountryLanguage;


CREATE VIEW CountryLanguagesView AS
SELECT 
    Country.Code AS CountryCode,
    Country.Name AS CountryName,
    CountryLanguage.Language,
    CountryLanguage.IsOfficial,
    CountryLanguage.Percentage
FROM 
    Country
JOIN 
    CountryLanguage ON Country.Code = CountryLanguage.CountryCode;

