"""Crea una classe chiamata punto. questa classe dovrebbe avere: 
Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori.
Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del piano."""

import math

#creo la classe Punto
class Punto:
    #definisco le classi
    def __init__(self, x, y):
        self.x = x  
        self.y = y  

#creo il metodo muovi con imput valori dx e dy   
    def muovi(self, dx, dy):
        #aggiorno le coordinate con dx e dy
        self.x += dx  
        self.y += dy  

   #metodo distanza da origine 
    def distanza_da_origine(self):
        #distanza del punto dall'origine (0,0) del piano usando il teorema di Pitagora
        return math.sqrt(self.x**2 + self.y**2)  


punto1 = Punto(3, 4)  #punto con coordinate (3,4)
print("distanza dall'origine:", punto1.distanza_da_origine())  #distanz dall'origine
punto1.muovi(1, -2)  #muove il punto di (1, -2)
print("nuove coordinate:", punto1.x, punto1.y)  # Stampa le nuove coordinate
print("distanza dall'origine dopo il movimento:", punto1.distanza_da_origine())  #distanza aggiornata
