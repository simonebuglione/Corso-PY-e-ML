-- Si vogliono recuperare dal database "world" la lingua e la nazione di ogni città.


FROM 
    City
JOIN 
    Country ON City.CountryCode = Country.Code
JOIN 
    CountryLanguage ON Country.Code = CountryLanguage.CountryCode
