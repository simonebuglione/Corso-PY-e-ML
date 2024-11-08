"""Esercizio 2 Slicing e F.Indexing

Consegna:

Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale e la matrice invertita modificata.


Obiettivo:

Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, modificare e manipolare sotto-matrici e array, applicando operazioni avanzate come l'inversione delle righe e la sostituzione condizionale degli elementi"""


import numpy as np

class MatriceManipolata:
    def __init__(self, seed=None):
                 #inizializza la classe e crea una matrice 6x6 con numeri random tra 1 e 100
                 np.random.seed(seed) #imposta replicabilità ma in modo deterministico
                 self.matrice_originale=np.random.randint(1,101, size=(6,6))

    def estrai_sottomatrice(self):
            #estrae sottomatrice centrale 4x4 da matrice originale
            self.sotto_matrice_centrale= self.matrice_originale[1:5, 1:5] #1 5 perchè toglie 1, quindi è 1 a 4
            return self.sotto_matrice_centrale
    
    def inverti_righe(self):
            #inverte righe della sotto matrice centrale
            self.sotto_matrice_invertita=self.sotto_matrice_centrale[::-1]
            return self.sotto_matrice_invertita
    
    def estrai_diagonale(self):
            #estrae diagonale principale dalla matrice invertita
            self.diagonale_principale=np.diagonal(self.sotto_matrice_centrale)
            return self.diagonale_principale
    def modifica_matrice(self):
            #sostituisce elementi multipli di 3 con -1 nella matr invertita
            self.matrice_invertita_modificata=self.sotto_matrice_invertita.copy()
            self.matrice_invertita_modificata[self.matrice_invertita_modificata % 3 == 0] = -1 #sostituisco elementi matrice invertita e la modifico
            return self.matrice_invertita_modificata
    
    def stampa_risultati(self):
            #stampa risultati
            print("matrice originale:", self.matrice_originale)
            print("sotto-matrice centrale 4x4:", self.sotto_matrice_centrale)
            print("matrice invertita:", self.sotto_matrice_invertita)            
            print("diagonale principale:", self.diagonale_principale)
            print("matrice invertita modificata:", self.matrice_invertita_modificata)

#esecuzione programma per replicabilità
def eseguire_programma():
    seed=50 
    manipolazione_matrice = MatriceManipolata(seed)

    #esegue operazioni
    manipolazione_matrice.estrai_sottomatrice()
    manipolazione_matrice.inverti_righe()
    manipolazione_matrice.estrai_diagonale()
    manipolazione_matrice.modifica_matrice()


    #stampa risultati
    manipolazione_matrice.stampa_risultati()


#rendo ripetibile il codice
while True:
        eseguire_programma()
        
        #chiede all'utente se vuole ripetere
        risposta= input("vuoi ripetere l'perazione?").strip().lower()
        if risposta != "si":
                print("programma ternimato")
                break
