"""crea un array Numpy utilizzando arange e verifica il tipo di dato(dtype) e la forma (shape) dell'array.

Esercizio:
1.Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
2. Verifica il tipo di dato dell'array e stampa il risultato.
3. Cambia il tipo di dato dell'array e stampa il risultato.
4. Stampa la forma dell'array."""


import numpy as np

#uso np.arrange per creare un array
array=np.arange(10,50) #metto 50 perchè restituisce un numero in meno

#verifico il tipo di dato array e stampa il risultato
print("tipo di dato array dopo il cambiamento:", array.dtype)

#cambia il tipo di dato aarray(es float) e stampa il risultato
array_float=array.astype(np.float64) #converto numeri interi in decimali
print("tipo di dato array dopo il cambiamenot:", array_float.dtype)

#stampa forma array
print("forma array:", array.shape);


#CON OGGETTI:
#definisco una classe che gestisce array
class ArrayManipulator:
    def __init__(self,start, stop):
        self.array=np.arrange(start,stop)
        
    #metodo per ottenere tipo di dato array
    def get_dtype(self):
        return self.array.dtype
    
    #metodo per cambiare tipo di dato array
    def change_dtype(self, new_dtype):
        self.array= self.array.astype(new_dtype)

    #metodo per ottendere forma array
    def get_shape(self):
        return self.array.shape
    

    
    
    #creo istanza classse arraymanipulator
    manipulator = ArrayManipulator(10, 50)

    #verifica tipo dato array
    print("tipo dato array:", manipulator.get_dtype()) #tipo iniziale

    #cambia tipo dato array a float64
    manipulator.change_dtype(np.float64)
    print("tipo dato array dopo il cambiamento:", manipulator.get_dtype()) #tipo dopo il cambiamento

    #stampo forma array
    print("forma array:", manipulator.get_shape())#forma array