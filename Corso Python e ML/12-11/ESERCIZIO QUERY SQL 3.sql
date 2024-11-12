--Scrivete una query SQL che restituisca tutti gli utenti dalla tabella"customers" il cui nome inizia con la S e vivono in California.



SELECT DISTINCT state FROM customers; --per vedere come è scritto California


SELECT * FROM customers
WHERE customerName LIKE 'S%' AND state = 'CA';

SELECT * FROM customers LIMIT 10;
