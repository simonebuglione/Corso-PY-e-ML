"""Create 2 array bidimensionali numpy 4x4 con valori interi casuali ed eseguite le seguenti operazioni:

- Restituite la somma di tutti gli elementi dei singoli array che si trovano nell'ultima riga dalla seconda colonna in poi;
- Unite i 2 array secondo l'asse 1."""


import numpy as np

#creo 2 array bidimensionali numpy 4x4 con valori int casuali
array_1=np.random.randint(0, 100,(4, 4))
array_2=np.random.randint (0, 100,(4, 4))

#somma di tutti gli elementi dei singoli array che si trovano nell'ultima riga dalla seconda colonna in poi
somma_ultima_riga_1=array_1[-1,1:].sum()
somma_ultima_riga_2=array_2[-1,1:].sum()

#Unite i 2 array secondo l'asse 1
array_uniti=np.concatenate((array_1, array_2), axis=1)


#stampa risultati
print("Array 1", array_1)
print("Array 2", array_2)
print("Somma ultima riga di array 1(dalla seconda in poi)", somma_ultima_riga_1)
print("Somma ultima riga di array 2(dalla seconda in poi)", somma_ultima_riga_2)
print("Array uniti", array_uniti)