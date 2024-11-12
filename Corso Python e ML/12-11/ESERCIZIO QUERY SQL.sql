--Scrivete una query SQL che inserisca un nuovo utente nella tabella" customers".

DESCRIBE customers;


INSERT INTO customers
(customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, country)
VALUES
(1002, 'Simone Buglione', 'Buglione', 'Simone', '12345678', 'Via Roma 1', 'Napoli', 'Italia');


SELECT * FROM customers WHERE customerNumber = 1002;
