"""Creare una classe base Animale e diverse classi derivate che rappresentano diversi tipi di animali in uno zoo.
Ogni classe derivata avrà attributi e metodi specifici che riflettono le caratteristiche e comportamenti unici degli animali che rappresentano.

-Classe Animale:
Attributi:
-nome (stringa che descrive il nome dell'animale)
-eta (intero che rappresenta l'età dell'animale)
Metodi:
-fai_suono(): un metodo che sstampa un suono generico dell'animale.

-Classi Figlie:
Creare almeno tre classi Figlie di Animale ES: Leone, Giraffa, e Pinguino.
Ogni classe avrò attributi e metodi specifici:
-Per esempio, la classe Leone potrebbe avere un metodo caccia() che stampa un messaggio su come il leone sta cacciando."""



#classe base animale
class Animale:
    def __init__(self, nome, eta):
        self.nome = nome  
        self.eta = eta    

    #metodo per stampare un suono generico dell'animale
    def fai_suono(self):
        print("L'animale fa un suono")



#classe derivata leone
class Leone(Animale):
    def __init__(self, nome, eta):
        #super chiede alla classe derivata di chiedere alla classe base di dare quello che serve, come i suoi metodi e attributi
        super().__init__(nome, eta)  
    def fai_suono(self):
        print("Il leone ruggisce")

    def caccia(self):
        print(f"{self.nome} sta cacciando nella savana")

#classe derivata giraffa
class Giraffa(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def fai_suono(self):
        print("La giraffa emette un suono sottile")

    def mangia_foglie(self):
        print(f"{self.nome} sta mangiando foglie dagli alberi")


#classe derivata pinguino
class Pinguino(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def fai_suono(self):
        print("Il pinguino squittisce")

    def nuota(self):
        print(f"{self.nome} sta nuotando nell'oceano")

#classe Zoo
class Zoo:
    def __init__(self):
        self.animali = []  #lista per memorizzare gli animali

    def aggiungi_animale(self):
        tipo = input("che tipo di animale vuoi creare?(Leone/Giraffa/Pinguino): ").strip().lower()
        nome = input("Inserisci nome animale:")
        eta = int(input("Inserisci età animale:"))

        if tipo == "leone":
            animale =Leone(nome, eta)
        elif tipo == "giraffa":
            animale =Giraffa(nome, eta)
        elif tipo == "pinguino":
            animale =Pinguino(nome, eta)
        else:
            print("tipo di animale non valido")
            return
        
        self.animali.append(animale)  #aggiunge l'animale alla lista

    def stampa_animali(self):
        for animale in self.animali:
            print(f"Nome: {animale.nome}, Età: {animale.eta}, Suono: ", end="")
            animale.fai_suono()  #stampa il suono dell'animale
            
            #chiamata ai metodi specifici per stampare le azioni
            if isinstance(animale, Leone):
                animale.caccia()  #stampa che il leone sta cacciando
            elif isinstance(animale, Giraffa):
                animale.mangia_foglie()  #stampa che la giraffa mangia foglie
            elif isinstance(animale, Pinguino):
                animale.nuota()  #stampa che il pinguino sta nuotando

#utilizzo della classe Zoo
zoo = Zoo()
numero_animali = int(input("Quanti animali vuoi creare?"))

for _ in range(numero_animali):
    zoo.aggiungi_animale()

zoo.stampa_animali()

