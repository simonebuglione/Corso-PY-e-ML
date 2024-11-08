"""usare la classe piano cartesiano e ogni piano deve essere 
composto da più punti, minimo 3 punti compongono un 
piano cartesiano, creare un sistema che permetta di stampare 
un piano cartesiano in versione scritta, non grafico vero e 
proprio. gestire istanziazione senza ereditarietà.
Crea una classe chiamata Punto. Questa classe dovrebbe avere:
Due attributi: x e y, per rappresentare le coordinate del 
punto nel piano.
Un metodo muovi che prenda in input un valore per dx e un 
valore per dy e modifichi le coordinate del punto di questi 
valori. 
Un metodo distanza_da_origine che restituisca la distanza dal 
punto dall'origine (0,0) del piano."""

import math

class Punto:
    def __init__(self, x, y): #attributi x e y
        self.x = x
        self.y = y

    def muovi(self, dx, dy):
        #muove il punto di dx lungo l'asse x e di dy lungo l'asse y
        self.x += dx
        self.y += dy


    def distanza_da_origine(self):
        #calcola la distanza del punto dall'origine (0,0)
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        #restituisce una rappresentazione testuale del punto
        return f"({self.x}, {self.y})"


class PianoCartesiano:
    def __init__(self, punti):
        if len(punti) < 3:
            raise ValueError("il piano cartesiano deve contenere almeno 3 punti")
        self.punti = punti

    def stampa(self):
        #stampa della rappresentazione testuale del piano cartesiano
        print("Piano Cartesiano:")
        for punto in self.punti:
            print(punto)




#esempio di utilizzo delle classi

#creo alcuni punti
p1 =Punto(1, 2)
p2 =Punto(3, 4)
p3 =Punto(-2, -1)

#creo un piano cartesiano con i punti
piano = PianoCartesiano([p1, p2, p3])

#stampa del piano cartesiano
piano.stampa()

#test metodi della classe punto
p1.muovi(1, -1)
print(f"Dopo il movimento: {p1} ha distanza dall'origine {p1.distanza_da_origine()}")
