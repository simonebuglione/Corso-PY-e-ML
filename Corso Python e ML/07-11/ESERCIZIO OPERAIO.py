"""Classe operaio con due figli con due classi astratte come secondo genitore. c'è operaio con cazzuola e martello che daranno specifiche al genitore. Gli unici metodi unici glieli darà la classe astratta. Muratore avrà gli stessi metodi del padre

Classe padre: init e stampa dati, tutti e due i figli avranno questi due metodi più i metodi presi dal secondo genitore, ovvero la classe astratta, ci saranno due classi, cazzuola e martello"""


from abc import ABC, abstractclassmethod

#classe astratta per la rappresentazione di uno strumento
class Strumento(ABC):
    @abstractclassmethod
    def usa_strumento(self):
        pass

#classe concreta per il martello
class Martello(Strumento):
    def usa_strumento(self):
        return "Usando il martello per martellare"
    
#classe concreta cazzuola
class Cazzuola(Strumento):
    def usa_strumento(self):
        return "usando la cazzuola per stendere il cemento"
    
#classe padre lavoratore generico
class Lavoratore:
    def __init__ (self, nome, cognome):
        self.nome = nome
        self.cognome =cognome

    def stampa_dati(self):
        print(f"Nome: {self.nome}, Cognome: {self.cognome}")

#classe figlia che rappresenta un operaio
class Operaio(Lavoratore):
    def __init__ (self, nome, cognome, strumento):
        super().__init__(nome, cognome)
        self.strumento =strumento
    
    def stampa_dati(self):
        super().stampa_dati()
        print(f"Strumento utilizzato: {self.strumento.usa_strumento()}")
       
#classe figlia muratore
class Muratore(Operaio):
    def __init__ (self, nome, cognome, strumento):
        super().__init__(nome, cognome, strumento)

    def stampa_dati(self):
        super().stampa_dati()
        print("Ciao sono un muratore e costruisco case")
    
#creo oggetti
martello=Martello()
cazzuola=Cazzuola()

operaio=Operaio("Pippo", "Rossi", martello)
muratore= Muratore("Gigi", "Gialli", cazzuola)

#stampa degli oggetti
print("Dati operaio:")
operaio.stampa_dati()

print("Dati Muratore:")
muratore.stampa_dati()