--Scrivete una query SQL che restituisca tutti gli utenti dalla tabella"customers" il cui nome inizia con la S e vivono in California.


SELECT * FROM customers
WHERE customerName LIKE 'S%' AND state = 'CA'; --California è identificato con CA

SELECT * FROM customers LIMIT 10;
