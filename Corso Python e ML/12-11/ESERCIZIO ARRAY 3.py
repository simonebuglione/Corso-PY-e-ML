"""Create 1 array unidimensionale con 50 valori randomici compresi tra 1 e 1.000 e fate i seguenti calcoli:

- Calcolo della media; 
- Calcolo della moda;
- Calcolo della deviazione standard; 
- Trasformatelo in un array 5 X 10"""

import numpy as np
from scipy import stats

#Create 1 array unidimensionale con 50 valori randomici compresi tra 1 e 1.000
array_1d=np.random.randint(1,1000,50)

#calcolo media
media=np.mean(array_1d)

#calcolo moda
moda=stats.mode(array_1d, keepdims=True).mode[0] #keepdims serve a mantenere la dim originale dell'array anche dopo il calcolo della moda

#dev standard
dev_stand=np.std(array_1d)

#Trasformatelo in un array 5 X 10
array_trasformato=array_1d.reshape(5,10)


#stampa risultati
print("Array unidimensionale:", array_1d)
print("Media:", media)
print("Moda:", moda)
print("Deviazione standard:", dev_stand)
print("Array 5x10:", array_trasformato)