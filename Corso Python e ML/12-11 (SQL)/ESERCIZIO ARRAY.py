"""Crea 2 array numpy:

- Un array unidimensionale di numeri casuali compresi tra 0 e 1;
- Un array bidimensionale di dimensione 3x3 con valori interi casuali."""



import numpy as np

#array unidimensionale di numeri casuali tra 0 e 1
array_1d=np.random.rand(50)


#array bidimensionale 3x3 con valori int casuali
array_2d = np.random.randint(0, 100, (3, 3))

print("Array 1D:", array_1d)
print("Array 2D:\n", array_2d)


