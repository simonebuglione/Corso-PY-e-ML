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


from abc import ABC, abstractclassmethod


#classe padre 
class PersonaleCucina(ABC):
    lista_nomi =[]
    def __init__ (self, nome, eta):
        self.nome=nome
        self.eta=eta

#metodo astratto che verrà sovrascritto nelle classi derivate
    @abstractclassmethod
    def Lavora(self):
        pass


#classe chef che eredita da personalecucina
class Chef(PersonaleCucina):
    def __init__ (self, nome, eta, specialita):
        super().__init__(nome, eta)


def Lavora(self):
    return f"{self.name}, lo chef sta preparando piatti di {self.specialita}"

def prepara_menu(self):
    return f"{self.name} sta preparando il nuovo menu"

#classe souschef che eredita da personalecucina
class SousChef(PersonaleCucina):
    def __init__(self, nome, eta):
        super().__init__(nome,eta)

    def lavora(self):
        return f"{self.nome}, sta gestendo l'inventario"
    
#classe cucoco linea che ereditaa da personalecucina
class CuocoLinea(PersonaleCucina):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)

        def Lavora(self):
            return f"{self.nome}, il cuoco di linea sta cucinando un piatto"
        
        def cucina_piatto(self, nome_piatto):
            return f"{self.nome} sta preaparando il piatto {nome_piatto}"
        
        