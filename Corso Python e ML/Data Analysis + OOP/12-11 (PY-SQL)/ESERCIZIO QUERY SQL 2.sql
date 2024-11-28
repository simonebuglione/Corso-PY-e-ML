--Scrivete una query SQL che elimini tutti gli ordini nella tabella "orders" con lo stato "Cancelled".


DELETE FROM orderdetails
WHERE orderNumber IN (SELECT orderNumber FROM orders WHERE status = 'Cancelled'); --per aggirare l'errore della query esterna

DELETE FROM orders
WHERE status = 'Cancelled';
