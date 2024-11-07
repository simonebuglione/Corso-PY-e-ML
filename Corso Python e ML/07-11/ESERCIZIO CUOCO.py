"""creare una classe base PersonaleCucina e diverse classi derivate che rappresentano differenti ruoli all'interno della cucina di un ristorante. l'obiettivo è utilizzare l'ereditarietà per condividere alcune caratteristiche comuni mentre si distinguono le responsabilità e le azioni specifiche di ogni ruolo.

1. Classe PersonaleCucina:
Attributi:
-nome (stringa)
-età (intero)
Metodi:
-Lavora() (metodo generico che può essere sovrascritto per specificare il tipo di lavoro svolto)
2. Classi Derivate:
Chef:
-Attributi aggiuntivi come specialità (tipo di cucina in cui è specializzato)
-Metodi come prepara_menu() che dettaglia come lo chef crea nuovi piatti e ModuleNotFoundError
SousChef:
-Metodi come gestisci_inventario() per gestire l'inventario della cucina e assistere lo chef 
Cuocolinea:
-Metodi come cucina_piatto(nome_piatto) che specifica la preparazione di un piatto specifico nella linea di produzione"""

import random
from abc import ABC, abstractclassmethod


#classe padre 
class PersonaleCucina(ABC):
    membri_ristorante =[]
    def __init__ (self, nome, eta):
        self.nome=nome
        self.eta=eta

#metodo astratto che verrà sovrascritto nelle classi derivate
    @abstractclassmethod
    def Lavora(self):
        pass

    @classmethod
    def visualizza_membri(cls):
        for membro in cls.membri_ristorante:
            print(f"{membro.nome}, {membro.eta}, anni, lavoro: {membro.lavora()}")


#classe chef che eredita da personalecucina
class Chef(PersonaleCucina):
    def __init__ (self, nome, eta, specialita):
        super().__init__(nome, eta)
        self.specialita=specialita


    def Lavora(self):
        return f"{self.name}, lo chef sta preparando piatti di {self.specialita}"

    def prepara_menu(self):
        return f"{self.name} sta preparando il nuovo menu"

#classe souschef che eredita da personalecucina
class SousChef(PersonaleCucina):
    def __init__(self, nome, eta):
        super().__init__(nome,eta)

    def Lavora(self):
        return f"{self.nome}, sta gestendo l'inventario"
    
#classe cucoco linea che ereditaa da personalecucina
class CuocoLinea(PersonaleCucina):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

    def Lavora(self):
        return f"{self.nome}, il cuoco di linea sta cucinando un piatto"
        
    def cucina_piatto(self, nome_piatto):
        return f"{self.nome} sta preaparando il piatto {nome_piatto}"
        

#classe cliente, creo nuova classe per la gestione di clienti
class Cliente:
    def __init__(self, nome, budget):
        self.nome =nome
        self.budget=budget
        self.ordinazioni=[] #qui vanno i piatti ordinati
        self.recensione={} #qui le recensioni sui piatti ordinati

    def ordina_piatto(self, ristorante, nome_piatto):
       if self.budget > 0:
          if ristorante.prendi_ordinazione(self,nome_piatto):
             self.ordinazioni.append(nome_piatto)
             print(f"{self.nome} ha ordinato il piatto {nome_piatto}")
          else:
                print(f"{nome_piatto} non è disponibile")
       else: 
            print(f"{self.nome} non ha più soldi per poter ordinare altri piatti")

#funzione lascia recensione
def lascia_recensione(self, piatto, voto):
    if 1<= voto <= 10:
        self.recensione[piatto]=voto
        print(f"{self.nome} ha lasciato una recensione: ha votato il piatto {piatto} con voto {voto}")
    else:
        print("Voto non valido, deve essere tra 1 e 10")

#classe ristorante (qui polimorfismo con gestione di menu e ordinaz)
class Ristorante:
    def __init__(self):
        self.menu=[] #menu inizialmente vbuoto
        self.ordinazioni=[] #ordinazioni clienti
        self.personale=[] #lista del personale
        self.piatti_serviti=[] #piatto servito

    def aggiungi_personale(self,membro):
        self.personale.append(membro)
        print("{membro.nome} è stato aggiunto al personale")
    
    def aggiungi_piatti_menu(self,piatti):
        self.menu.append(piatti)

    def prendi_ordinazione(self, cliente, piatto):
        if piatto in self.menu and cliente.budget > 0:
            piatto_preparato = False
            for membro in self.personale:
                if isinstance(membro, Chef) and piatto == "Piatto Chef":
                    self.ordinazioni.append(piatto)
                    cliente.budget -= random.randint(10,100) #budget casuale tra 10 e 100
                    print(f"{membro.nome} ha preparato il piatto {piatto} per {cliente.nome}")
                    return True
                if isinstance (membro, SousChef) and piatto == "Piatto SousChef":
                    self.ordinazioni.append(piatto)
                    cliente.budget-= random.randit(10, 100)
                    print(f"{membro.nome} ha preparato il piatto {piatto} per {cliente.nome}")
                    return True
                
                if isinstance (membro, CuocoLinea) and piatto == "Piatto CuocoLinea":
                    self.ordinazioni.append(piatto)
                    cliente.budget-= random.randit(10, 100)
                    print(f"{membro.nome} ha preparato il piatto {piatto} per {cliente.nome}")
                    return True
            return False
        return False
    
    def mostra_menu(self):
        for piatti in self.menu:
            print(f"Menu: {piatti}")

    def mostra_ordinazioni(self):
        print ("Ordinazioni:")
        for ordinazione in self.ordinazioni:
            print (ordinazione)

    def visualizza_personale(self):
        print("Membri del personale:")
        for membro in self.personale:
            print(f"{membro.nome}, {membro.eta} anni")



#test creazione ristorante, piatti, clienti e interazioni
ristorante=Ristorante()

#aggiungo piatti al menun
ristorante.aggiungi_piatti_menu(["Piatto Chef", "Piatto SousChef", "Piatto CuocoLinea"])

#creo il personale
chef=Chef("Pippo", 35, "Cucina mediterranea")
sous_chef=SousChef("Sara", 28)
cuoco_linea=CuocoLinea("Gigi", 24)

#aggiungo personale al ristorante
ristorante.aggiungi_personale(chef)
ristorante.aggiungi_personale(sous_chef)
ristorante.aggiungi_personale(cuoco_linea)

#creo dei clienti
cliente1=Cliente("Alex", 50)
cliente2= Cliente("Maria", 30)

#i clienti ordinano
cliente1.ordina_piatto(ristorante, "Piatto Chef")
cliente2.ordina_piatto(ristorante, "Piatto souschef")

#i clienti lasciano una recensione
cliente1.lascia_recensione("Piatto chef", 9)
cliente2.lascia_recensione ("Piatto souschef",7)

#mostro lo stato del ristorante
ristorante.mostra_menu()
ristorante.mostra_ordinazioni()
ristorante.visualizza_personale()
